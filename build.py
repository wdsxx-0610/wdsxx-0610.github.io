#!/usr/bin/env python3
"""Generate index.html for Xiang Li's academic homepage.

Edit the CONTENT block below and re-run:
    python3 build.py
"""
from pathlib import Path

HERE = Path(__file__).parent
SITE = HERE          # GitHub Pages serves the repo root

# --------------------------------------------------------------------------
# CONTENT  (edit here)
# --------------------------------------------------------------------------
GITHUB_USER = "wdsxx-0610"          # replaced with the real username on publish
REPO_NAME   = f"{GITHUB_USER}.github.io"

NAME_EN   = "Xiang Li"
NAME_CN   = "李翔"
ROLE      = "Ph.D. Student (Joint Training)"
AFFIL_1   = "BNU–HKBU United International College"
AFFIL_2   = "Great Bay University"
LOCATION  = "Guangdong, China"
EMAIL     = "vpe029@usask.ca"
ORCID_ID  = "0009-0002-0780-0417"

# Public links — set to None to hide the entry
LINKS = [
    ("ORCID",          f"https://orcid.org/{ORCID_ID}",    "orcid"),
    ("Google Scholar", None,                               "scholar"),
    ("GitHub",         f"https://github.com/{GITHUB_USER}","github"),
    ("ResearchGate",   None,                               "researchgate"),
    ("Email",          f"mailto:{EMAIL}",                 "email"),
]

ABOUT = """
I am a first-year Ph.D. student in a joint training programme between
<strong>BNU&ndash;HKBU United International College</strong> and
<strong>Great Bay University</strong>. I received my M.Sc. in Biological Engineering
from the <strong>University of Saskatchewan</strong> (2026), where I worked with
Prof.&nbsp;Yen-Han Lin on machine learning approaches for redox potential&ndash;controlled
very-high-gravity ethanol fermentation, and my B.Eng. in Biological Engineering from
<strong>Northwest A&amp;F University</strong> (2024).
"""

ABOUT_2 = """
My research sits where <strong>fermentation bioprocess engineering</strong> meets
<strong>machine learning</strong>. I build soft sensors and kinetic models that turn cheap,
continuous online signals &mdash; oxidation&ndash;reduction potential (ORP) in particular &mdash;
into quantitative, forward-looking estimates of metabolic activity, so that a fermentation
can be steered before it fails rather than analysed after it ends.
"""

FACTS = [
    ("Position",  "Ph.D. Student, Year 1"),
    ("Programme", "BNU&ndash;HKBU UIC &times; Great Bay University"),
    ("M.Sc.",     "University of Saskatchewan, 2026 (GPA 4.0/4.0)"),
    ("B.Eng.",    "Northwest A&amp;F University, 2024"),
]

INTERESTS = [
    "Fermentation process control",
    "Kinetic modelling &amp; parameter inference",
    "Deep learning for bioprocesses (AI4Bio)",
    "Soft sensing &amp; state estimation",
    "Bayesian uncertainty quantification",
    "Bioenergy &amp; cleaner biomanufacturing",
]

OPEN_TO = """I am open to research collaborations and discussions on machine learning for
bioprocess monitoring, kinetic modelling, and fermentation process control."""

PUBLICATIONS = [
    {
        "tag": ("published", "Published"),
        "title": "Bayesian inference on fermentation kinetics: Comparative analysis with frequentist approach",
        "authors": "<strong>Xiang Li</strong>, Yen-Han Lin",
        "venue": "<em>Bioresource Technology</em>, 2026, 444, 134012. "
                 "IF 9.0, JCR Q1.",
        "links": [("DOI", "https://doi.org/10.1016/j.biortech.2026.134012"),
                  ("ScienceDirect", "https://www.sciencedirect.com/science/article/pii/S0960852426000933")],
    },
    {
        "tag": ("review", "Under review"),
        "title": "Enhancing cleaner biomanufacturing of ethanol: A temporal deep learning soft sensor for ORP-driven metabolic forecasting in very-high-gravity fermentation",
        "authors": "<strong>Xiang Li</strong>, Yen-Han Lin",
        "venue": "<em>Journal of Cleaner Production</em> &mdash; under review, 2026.",
        "links": [],
    },
    {
        "tag": ("conf", "Poster"),
        "title": "Modified Hyperbolic Secant (MHS) Models for Fermentation Kinetics and Uncertainty",
        "authors": "<strong>Xiang Li</strong>, Yen-Han Lin",
        "venue": "Poster, <em>YABEC 2026</em> (Asian Young Biotechnologists Network), University of Saskatchewan.",
        "links": [],
    },
]

EDUCATION = [
    ("Ph.D. Student, Biological Engineering", "2026 &ndash; present",
     "BNU&ndash;HKBU United International College &amp; Great Bay University, Guangdong, China",
     "Joint training programme. Year 1."),
    ("M.Sc., Biological Engineering", "2025 &ndash; 2026",
     "University of Saskatchewan, Saskatoon, Canada",
     "GPA 4.0/4.0. Supervisor: Prof. Yen-Han Lin. "
     "Thesis: <em>Machine learning approaches for redox potential-controlled very high gravity ethanol fermentation</em>."),
    ("B.Eng., Biological Engineering", "2020 &ndash; 2024",
     "Northwest A&amp;F University, Yangling, China",
     "GPA 3.71/4.0, rank 3/63. "
     "Thesis: <em>Deep learning-based image processing of maize allele-specific chromatin interactions and regulation of imprinted genes</em>."),
]

RESEARCH_VISITS = [
    ("Visiting Student", "Jan. 2026 &ndash; present",
     "Shanghai Jiao Tong University, School of Life Sciences and Biotechnology",
     "Project: deep learning&ndash;based metabolic modelling of filamentous fungi and its industrial application."),
]

INDUSTRY = [
    ("Sales Engineer", "Sep. 2024 &ndash; Dec. 2024",
     "Servicebio Technology Co., Ltd., Zhengzhou, China",
     "Technical support and product application for life-science research reagents."),
]

PROJECTS = [
    ("Deep learning monitoring and forecasting system for ethanol fermentation", "Jun. 2025 &ndash; present",
     "Fused sparse offline measurements with dense online ORP signals to build a high-resolution training set; "
     "developed a real-time state-estimation model (ORPSN, RNN) and a multi-horizon forecasting model "
     "(ORPSC, LSTM encoder&ndash;decoder) for metabolic dynamics.",
     "Achieved high-accuracy soft sensing of ethanol production and glucose consumption rates; "
     "maintained accuracy over an 8-hour forecast horizon, providing a basis for proactive feed-forward control."),
    ("Bayesian inference for fermentation kinetics and uncertainty analysis", "Jan. 2025 &ndash; Dec. 2025",
     "Built Bayesian hierarchical kinetic models for multiple fermentation systems with algorithmic and "
     "literature-informed priors; systematically compared Bayesian and frequentist inference for parameter "
     "identifiability and predictive stability under sparse data.",
     "Resolved non-convergence of conventional methods in small-sample settings, giving robust kinetic parameter "
     "estimates with explicitly quantified uncertainty and improved biological interpretability."),
    ("Allele-specific chromatin interactions and imprinted gene regulation in maize endosperm", "Mar. 2023 &ndash; May 2024",
     "Applied autoencoders and U-Net to denoise and enhance the resolution of Hi-C data from reciprocal crosses of "
     "maize inbred lines B73 and Mo17; constructed allele-specific chromatin interaction maps; partitioned A/B "
     "compartments and identified TADs genome-wide; analysed compartment distributions around imprinted genes.",
     "Built an allele-resolved 3D chromatin architecture of maize endosperm and showed that the compartmental "
     "distribution of imprinted genes has no clear parent-of-origin dependence, indicating that chromatin "
     "reorganisation at the A/B compartment level is not the principal mechanism of imprinting regulation there."),
    ("Metagenomics and culturomics for tobacco biological control", "Nov. 2021 &ndash; Nov. 2022",
     "Screened and validated antagonistic strains and assembled consortia; designed and ran field trials; "
     "performed 16S rRNA amplicon analysis of the tobacco rhizosphere microbiome.",
     "Established a biocontrol strain library with good field efficacy and developed an effective composite "
     "microbial agent."),
]

AWARDS = [
    ("University of Saskatchewan CGPS 75th Recruitment Scholarship", "Jan. 2025"),
    ("National Scholarship for Encouragement (国家励志奖学金), Northwest A&amp;F University", "Nov. 2021"),
    ("First Prize, National Undergraduate Life Sciences Competition (Innovation &amp; Entrepreneurship)", "Nov. 2021"),
    ("Meritorious Winner (top 8%), Mathematical Contest in Modeling, COMAP, USA", "Apr. 2021"),
    ("First-Class Academic Scholarship, College of Life Sciences, Northwest A&amp;F University", "Dec. 2020"),
]

SKILLS = [
    "Python", "PyTorch", "TensorFlow / Keras", "NumPy &amp; pandas",
    "Bayesian inference (MCMC)", "Kinetic modelling",
    "Bioreactor operation &amp; ORP control", "HPLC analysis",
    "R", "Git",
]

# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------

ICONS = {
    "email": '<path d="M2 4h16v12H2V4zm2 1.5v.4l6 3.6 6-3.6v-.4H4zm12 2.1-6 3.6-6-3.6V14h12V7.6z"/>',
    "github": '<path d="M10 .8a9.2 9.2 0 0 0-2.9 17.9c.46.09.63-.2.63-.44v-1.7c-2.56.56-3.1-1.08-3.1-1.08-.42-1.06-1.02-1.35-1.02-1.35-.84-.57.06-.56.06-.56.92.07 1.4.95 1.4.95.82 1.4 2.15 1 2.67.77.08-.6.32-1 .58-1.24-2.04-.23-4.19-1.02-4.19-4.55 0-1 .36-1.83.95-2.47-.1-.23-.41-1.17.09-2.44 0 0 .77-.25 2.53.94a8.8 8.8 0 0 1 4.6 0c1.75-1.19 2.52-.94 2.52-.94.5 1.27.19 2.21.09 2.44.59.64.95 1.46.95 2.47 0 3.54-2.16 4.32-4.21 4.55.33.29.63.85.63 1.72v2.55c0 .25.17.54.64.45A9.2 9.2 0 0 0 10 .8z"/>',
    "orcid": '<path d="M10 0a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM6.4 6.2a1 1 0 1 1 0 2 1 1 0 0 1 0-2zM5.8 9h1.3v6H5.8V9zm3 0h3c1.8 0 3.1 1.2 3.1 3s-1.3 3-3.1 3h-3V9zm1.3 1.1v3.8h1.6c1.2 0 1.9-.75 1.9-1.9s-.7-1.9-1.9-1.9h-1.6z"/>',
    "scholar": '<path d="M10 2 0 7l10 5 10-5-10-5zm0 11.6L3 10.1v4.2c0 1.7 3.1 3.1 7 3.1s7-1.4 7-3.1v-4.2l-7 3.5z"/>',
    "researchgate": '<path d="M10 0a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm-3.4 5.5c.9 0 1.6.25 2.1.75.5.5.75 1.2.75 2.1 0 .6-.14 1.12-.42 1.55-.28.43-.68.75-1.2.95l1.9 3.6H8.2L6.6 11.2H5.6v3.25H3.9V5.5h2.7zm-.5 1.45v2.8h.5c.5 0 .87-.11 1.1-.34.24-.23.36-.6.36-1.08 0-.48-.12-.84-.36-1.06-.23-.22-.6-.32-1.1-.32h-.5zm8.6 1.5c1.1 0 1.9.4 2.4 1.1.3.42.45.95.45 1.6v.5h-3.9c.04.55.2.95.46 1.2.26.26.6.38 1.04.38.35 0 .65-.07.9-.2.25-.14.45-.35.6-.63l.85.55c-.55.9-1.4 1.35-2.5 1.35-.55 0-1.02-.1-1.4-.3-.4-.2-.7-.5-.9-.87-.2-.4-.3-.87-.3-1.4 0-.55.1-1.03.3-1.43.2-.4.5-.7.9-.9.4-.2.85-.3 1.35-.3zm0 1.15c-.35 0-.62.1-.82.3-.2.2-.32.5-.37.88h2.3c-.03-.38-.14-.68-.33-.88-.2-.2-.46-.3-.78-.3z"/>',
    "location": '<path d="M10 1.5a5.5 5.5 0 0 0-5.5 5.5c0 4 5.5 11.5 5.5 11.5S15.5 11 15.5 7A5.5 5.5 0 0 0 10 1.5zm0 7.5a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"/>',
}


def svg(name, cls=""):
    body = ICONS.get(name, ICONS["email"])
    return (f'<svg class="{cls}" width="15" height="15" viewBox="0 0 20 20" '
            f'aria-hidden="true" xmlns="http://www.w3.org/2000/svg">{body}</svg>')


def esc(s):
    return s


def render_links():
    out = []
    for label, url, icon in LINKS:
        if not url:
            continue
        cls = "email" if label == "Email" else ""
        text = EMAIL if label == "Email" else label
        out.append(
            f'<a href="{url}" target="_blank" rel="noopener">'
            f'<span class="ico">{svg(icon)}</span>'
            f'<span class="{cls}">{text}</span></a>'
        )
    return "\n        ".join(out)


def render_publications():
    out = []
    for p in PUBLICATIONS:
        tag_cls, tag_text = p["tag"]
        title = esc(p["title"])
        if p["links"]:
            title = f'<a href="{p["links"][0][1]}" target="_blank" rel="noopener">{title}</a>'
        links = ""
        if p["links"]:
            links = '<p class="links">' + "".join(
                f'<a href="{u}" target="_blank" rel="noopener">{t} &rarr;</a>' for t, u in p["links"]
            ) + "</p>"
        out.append(f"""      <article class="pub">
        <p class="title">{title}<span class="tag {tag_cls}">{tag_text}</span></p>
        <p class="authors">{p["authors"]}</p>
        <p class="venue">{p["venue"]}</p>
        {links}
      </article>""")
    return "\n".join(out)


def render_education():
    out = []
    for what, when, where, note in EDUCATION:
        note_html = f'<div class="note">{note}</div>' if note else ""
        out.append(f"""      <div class="entry">
        <div class="what">{what}</div>
        <div class="when">{when}</div>
        <div class="where">{where}</div>
        {note_html}
      </div>""")
    return "\n".join(out)


def render_entries(items):
    out = []
    for what, when, where, note in items:
        note_html = f'<div class="note">{note}</div>' if note else ""
        out.append(f"""      <div class="entry">
        <div class="what">{what}</div>
        <div class="when">{when}</div>
        <div class="where">{where}</div>
        {note_html}
      </div>""")
    return "\n".join(out)


def render_projects():
    out = []
    for title, when, work, result in PROJECTS:
        out.append(f"""      <div class="entry">
        <div class="what">{title}</div>
        <div class="when">{when}</div>
        <div class="note">
          <ul>
            <li>{work}</li>
            <li><strong>Outcome:</strong> {result}</li>
          </ul>
        </div>
      </div>""")
    return "\n".join(out)


def render_awards():
    return "\n".join(
        f'      <li><span>{a}</span><span class="yr">{y}</span></li>' for a, y in AWARDS
    )


def render_timeline(items):
    return "\n".join(
        f'      <li><span class="yr">{y}</span><span class="txt">{t}</span></li>'
        for y, t in items
    )


def build():
    facts = "\n".join(
        f'        <div><div class="k">{k}</div><div class="v">{v}</div></div>' for k, v in FACTS
    )
    interests = "\n".join(f"        <li>{i}</li>" for i in INTERESTS)
    skills = "\n".join(f"        <span>{s}</span>" for s in SKILLS)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{NAME_EN} &middot; Academic Homepage</title>
<meta name="description" content="{NAME_EN} ({NAME_CN}) — Ph.D. student working on machine learning for fermentation bioprocess monitoring, kinetic modelling and soft sensing.">
<meta name="author" content="{NAME_EN}">
<meta property="og:title" content="{NAME_EN} — Academic Homepage">
<meta property="og:description" content="Machine learning for fermentation bioprocess monitoring, kinetic modelling and soft sensing.">
<meta property="og:type" content="profile">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="style.css">
</head>
<body>

<div class="shell">

  <!-- ============================ SIDEBAR ============================ -->
  <aside class="sidebar">
    <div class="avatar" aria-hidden="true">XL</div>

    <h1>{NAME_EN}<span class="cn">{NAME_CN}</span></h1>

    <p class="role">
      {ROLE}<br>
      {AFFIL_1}<br>
      {AFFIL_2}
    </p>

    <p class="place">{svg("location")} {LOCATION}</p>

    <nav class="nav">
      <a href="#about">About me</a>
      <a href="#research">Research</a>
      <a href="#publications">Publications</a>
      <a href="#cv">CV</a>
    </nav>

    <div class="contact">
      <div class="label">Contact &amp; links</div>
      {render_links()}
    </div>
  </aside>

  <!-- ============================== MAIN ============================= -->
  <main class="main">

    <!-- visible only in print / PDF export -->
    <div class="print-head">
      <h1>{NAME_EN} <span>{NAME_CN}</span></h1>
      <p>{ROLE} &middot; {AFFIL_1} &amp; {AFFIL_2}</p>
      <p>{EMAIL} &middot; {LOCATION}</p>
      <p>ORCID: https://orcid.org/{ORCID_ID} &middot; GitHub: https://github.com/{GITHUB_USER}</p>
    </div>

    <div class="topbar">
      <span class="topbar-name">{NAME_EN} &middot; Curriculum Vitae</span>
      <span class="topbar-actions">
        <a href="XiangLi_CV.pdf" download>Download CV (PDF)</a>
      </span>
    </div>

    <section id="about">
      <h2 class="section-title">About me</h2>
      <p class="lead">{ABOUT.strip()}</p>
      <p>{ABOUT_2.strip()}</p>

      <div class="facts">
{facts}
      </div>

      <div class="callout">
        <p>{OPEN_TO}</p>
      </div>
    </section>

    <section id="research">
      <h2 class="section-title">Research interests<span class="cn">研究方向</span></h2>
      <ul class="interests">
{interests}
      </ul>
    </section>

    <section id="publications">
      <h2 class="section-title">Publications<span class="cn">学术成果</span></h2>
{render_publications()}
    </section>

    <section id="cv">
      <h2 class="section-title">CV<span class="cn">简历</span></h2>

      <div class="cv-block">
        <h3>Education</h3>
{render_education()}
      </div>

      <div class="cv-block">
        <h3>Research experience</h3>
{render_projects()}
      </div>

      <div class="cv-block">
        <h3>Research visits &amp; industry</h3>
{render_entries(RESEARCH_VISITS)}
{render_entries(INDUSTRY)}
      </div>

      <div class="cv-block">
        <h3>Honours &amp; awards</h3>
        <ul class="awards">
{render_awards()}
        </ul>
      </div>

      <div class="cv-block">
        <h3>Skills</h3>
        <div class="skills">
{skills}
        </div>
      </div>
    </section>

  </main>
</div>

<footer class="foot">
  <span>&copy; 2026 {NAME_EN}. Last updated October 2026.</span>
  <span>Hosted on GitHub Pages.</span>
</footer>

</body>
</html>
"""
    out = SITE / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out}  ({len(html)} chars)")


if __name__ == "__main__":
    build()
