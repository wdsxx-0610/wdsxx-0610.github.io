#!/usr/bin/env python3
"""Create the GitHub Pages repo and push this site.

Usage:
    python3 publish.py --user <github-username>      # token read from stdin

The token needs `repo` scope (classic) or Contents+Pages+Administration write
(fine-grained). It is only used for the API calls and the one push; it is never
written to disk or to any git remote URL.
"""
import argparse
import base64
import json
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
SITE = HERE          # GitHub Pages serves the repo root
API = "https://api.github.com"


def api(token, method, path, payload=None, expect=(200, 201, 204)):
    url = f"{API}{path}"
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "homepage-publish")
    if data:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            body = r.read().decode() or "{}"
            return r.status, json.loads(body)
    except urllib.error.HTTPError as e:
        body = e.read().decode() or "{}"
        try:
            parsed = json.loads(body)
        except json.JSONDecodeError:
            parsed = {"raw": body}
        if e.code in expect:
            return e.code, parsed
        raise SystemExit(f"GitHub API {method} {path} -> {e.code}: "
                         f"{parsed.get('message', body)[:400]}")


def run(args, cwd=None, env=None):
    p = subprocess.run(args, cwd=cwd, env=env, capture_output=True, text=True)
    if p.returncode != 0:
        raise SystemExit(f"command failed: {' '.join(args)}\n{p.stdout}\n{p.stderr}")
    return p.stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", required=True, help="GitHub username")
    ap.add_argument("--repo", default=None, help="repo name (default: <user>.github.io)")
    args = ap.parse_args()

    token = sys.stdin.readline().strip()
    if not token:
        raise SystemExit("no token on stdin")

    user = args.user
    repo = args.repo or f"{user}.github.io"
    print(f"→ authenticating as {user}, target repo {user}/{repo}")

    # 1. who am I / is the repo there already?
    status, me = api(token, "GET", "/user")
    login = me.get("login")
    if login and login.lower() != user.lower():
        print(f"  note: token belongs to '{login}', using that as owner")
        user = login
        if repo == f"{args.user}.github.io":
            repo = f"{user}.github.io"

    status, existing = api(token, "GET", f"/repos/{user}/{repo}", expect=(200, 404))
    if status == 404:
        print(f"→ creating public repo {user}/{repo}")
        api(token, "POST", "/user/repos", {
            "name": repo,
            "description": "Personal academic homepage",
            "homepage": f"https://{user}.github.io",
            "private": False,
            "has_issues": False,
            "has_wiki": False,
            "has_projects": False,
            "auto_init": False,
        })
    else:
        print(f"→ repo already exists ({existing.get('visibility')})")

    # 2. rewrite placeholders with the real username
    print("→ filling in username placeholders")
    for rel in ("index.html", "README.md", "build.py"):
        path = HERE / rel
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("__GITHUB_USER__", user), encoding="utf-8")

    # 3. local git repo
    if not (HERE / ".git").exists():
        run(["git", "init", "-b", "main"], cwd=HERE)
    run(["git", "config", "user.name", user], cwd=HERE)
    run(["git", "config", "user.email",
         f"{login or user}@users.noreply.github.com"], cwd=HERE)
    run(["git", "add", "-A"], cwd=HERE)
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=HERE)
    if diff.returncode != 0:
        run(["git", "commit", "-m", "Build personal academic homepage"], cwd=HERE)
    else:
        print("  nothing new to commit")

    # 4. push using an in-memory credential helper (token never lands in .git/config)
    #    An explicit empty credential.helper disables osxkeychain, whose cached
    #    (expired) GitHub token would otherwise be used instead of the askpass value.
    askpass = HERE / ".git-askpass.sh"
    askpass.write_text("#!/bin/sh\ncase \"$1\" in *sername*) echo x-access-token;; *) echo \"$GH_TOKEN\";; esac\n",
                       encoding="utf-8")
    askpass.chmod(0o700)
    env = {
        "PATH": "/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/homebrew/bin",
        "HOME": str(Path.home()),
        "GIT_ASKPASS": str(askpass),
        "GH_TOKEN": token,
        "GIT_TERMINAL_PROMPT": "0",
        "GIT_CONFIG_COUNT": "1",
        "GIT_CONFIG_KEY_0": "credential.helper",
        "GIT_CONFIG_VALUE_0": "",
    }
    remote = f"https://github.com/{user}/{repo}.git"
    remotes = run(["git", "remote"], cwd=HERE).split()
    if "origin" in remotes:
        run(["git", "remote", "set-url", "origin", remote], cwd=HERE)
    else:
        run(["git", "remote", "add", "origin", remote], cwd=HERE)
    print(f"→ pushing to {remote}")
    print(run(["git", "push", "-u", "origin", "main"], cwd=HERE, env=env))

    askpass.unlink(missing_ok=True)

    # 5. enable Pages
    print("→ enabling GitHub Pages (main / root)")
    st, res = api(token, "POST", f"/repos/{user}/{repo}/pages",
                  {"source": {"branch": "main", "path": "/"}}, expect=(201, 409, 422))
    if st == 409:
        api(token, "PUT", f"/repos/{user}/{repo}/pages",
            {"source": {"branch": "main", "path": "/"}}, expect=(204, 200))
        print("  Pages already configured; source set to main/root")
    elif st == 422:
        print(f"  Pages response: {res.get('message')}")

    st, info = api(token, "GET", f"/repos/{user}/{repo}/pages", expect=(200, 404))
    url = info.get("html_url") or f"https://{user}.github.io"
    print(f"\n✅ done\n   repository: https://github.com/{user}/{repo}\n   site:       {url}\n"
          f"   (first deployment usually takes 1–2 minutes)")


if __name__ == "__main__":
    main()
