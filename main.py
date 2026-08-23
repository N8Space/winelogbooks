from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(
    title="AI Enablement Portfolio",
    description="Recruiter-focused portfolio for AI project showcases and Azure enablement work.",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

CERTIFICATIONS = [
    {
        "name": "AI-103",
        "description": "Designing and implementing Microsoft AI solutions",
        "status": "Target: Oct 2026",
    },
    {
        "name": "AZ-104",
        "description": "Microsoft Azure Administrator certification path",
        "status": "Target: Dec 2026",
    },
    {
        "name": "Azure AI Foundry",
        "description": "Responsible AI, prompt engineering, and enterprise deployment",
        "status": "Applied learning",
    },
]

PROJECTS = [
    {
        "slug": "copilot-support-automation",
        "title": "AI Copilot for Support Operations",
        "category": "Azure AI + Operations",
        "summary": "A knowledge assistant built for frontline teams to answer policy, troubleshooting, and escalation questions using enterprise data and Azure AI services.",
        "outcome": "Reduced time-to-answer for recurring support tasks and created a repeatable AI adoption pattern for teams with limited ML experience.",
        "stack": ["Azure OpenAI", "AI Search", "Azure App Service", "Key Vault", "Monitor"],
        "story": "This project demonstrates how to combine governance, secure deployment, and user-centered design to create a production-ready internal AI assistant.",
    },
    {
        "slug": "azure-governance-dashboard",
        "title": "AI Governance & Security Dashboard",
        "category": "Cloud Governance",
        "summary": "A governance dashboard that connects model usage, cost controls, security posture, and operational guardrails for AI-driven teams.",
        "outcome": "Creates a clear operating model for scale-up AI adoption with policy oversight and business-friendly reporting.",
        "stack": ["Azure Monitor", "Cost Management", "Entra ID", "Policy", "Dashboards"],
        "story": "This work frames AI enablement as a platform capability, showing how to align technical delivery with compliance, cost visibility, and adoption metrics.",
    },
    {
        "slug": "intelligent-knowledge-hub",
        "title": "Intelligent Knowledge Hub",
        "category": "Knowledge Management",
        "summary": "A retrieval-first knowledge assistant that helps teams discover approved guidance, process documents, and training content quickly.",
        "outcome": "Improves knowledge accessibility and reduces manual lookup time across departments while establishing a reusable architecture for future AI copilots.",
        "stack": ["RAG", "Azure AI Search", "Python", "FastAPI", "Vector Search"],
        "story": "This project highlights how AI enablement teams can capture institutional knowledge and turn it into an enterprise service with measurable productivity gains.",
    },
]

STATS = [
    ("3+", "AI projects in progress"),
    ("AI-103", "and AZ-104 certification path"),
    ("100%", "focused on Azure enablement"),
]


def render_page(title: str, current_path: str, main_content: str) -> HTMLResponse:
    nav_items = [
        ("/", "Home"),
        ("/projects", "Projects"),
        ("/about", "About"),
        ("/docs", "API Docs"),
    ]
    links = []
    for path, label in nav_items:
        active = ' class="active"' if path == current_path else ""
        target = ' target="_blank"' if path == "/docs" else ""
        links.append(f'<a href="{path}"{active}{target}>{label}</a>')

    return HTMLResponse(
        f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="AI Enablement portfolio showcasing Azure AI projects, certification progress, and enterprise adoption work." />
  <title>{title} — Nathan Lester, AI Enablement Lead</title>
    <link rel="stylesheet" href="/static/style.css" />
  </head>
  <body>
    <header class="site-header">
      <div class="container navbar">
        <a class="brand" href="/">
        <span class="brand-mark">NL</span>
        <span>Nathan Lester</span>
        </a>
        <nav class="nav-links" aria-label="Main navigation">
          {''.join(links)}
        </nav>
      </div>
    </header>
    {main_content}
    <footer class="footer">
      <div class="container footer-inner">
      <div><strong>Nathan Lester — AI Enablement Lead</strong></div>
        <div>Available for AI Enablement Lead opportunities • hello@winelogbooks.com</div>
      </div>
    </footer>
  </body>
</html>"""
    )


def render_project_cards(project_list):
    cards = []
    for project in project_list:
        stack_items = ''.join(f'<li>{item}</li>' for item in project["stack"][:3])
        cards.append(
            f"""
            <article class="project-card">
              <div>
                <span class="tag">{project['category']}</span>
                <h3>{project['title']}</h3>
                <p>{project['summary']}</p>
              </div>
              <div>
                <ul>{stack_items}</ul>
                <div style="margin-top: 1rem;">
                  <a href="/projects/{project['slug']}">View project →</a>
                </div>
              </div>
            </article>
            """
        )
    return '\n'.join(cards)


@app.get("/", response_class=HTMLResponse)
async def home():
    project_cards = render_project_cards(PROJECTS[:3])
    stat_cards = ''.join(f'<div class="stat-card"><strong>{value}</strong><span>{label}</span></div>' for value, label in STATS)
    cert_cards = ''.join(
        f'<article class="cert-card"><span class="tag">{cert["status"]}</span><h3>{cert["name"]}</h3><p>{cert["description"]}</p></article>'
        for cert in CERTIFICATIONS
    )
    body = f"""
    <main>
      <section class="hero">
        <div class="container hero-grid">
          <div>
            <span class="kicker">AI Enablement Portfolio</span>
            <h1>Building practical <span class="gradient-text">AI solutions</span><br />for operations, governance, and growth.</h1>
            <p>I am creating a portfolio of Azure-focused AI projects and enablement work while progressing through the AI-103 and AZ-104 certification paths. My goal is to help teams turn AI ideas into secure, measurable business value.</p>
            <div class="hero-actions">
              <a class="btn btn-primary" href="/projects">Explore projects</a>
              <a class="btn btn-secondary" href="/about">Learn my story</a>
            </div>
            <div class="hero-meta">
              <span>Azure-first architecture</span>
              <span>AI adoption strategy</span>
              <span>Business-focused delivery</span>
            </div>
          </div>
          <aside class="hero-aside">
            <div class="profile-card">
                          <div class="avatar" aria-hidden="true">NL</div>
                          <h3>Nathan Lester — AI Enablement Lead</h3>
              <p>Focused on secure AI systems, operational readiness, and stakeholder enablement across Azure environments.</p>
            </div>
          </aside>
        </div>
      </section>
      <section class="section">
        <div class="container">
          <div class="section-header">
            <h2>Portfolio signal</h2>
            <p>I’m building evidence of AI capability for recruiters and hiring managers who care about lead-level thinking, not just demos.</p>
          </div>
          <div class="stats-grid">{stat_cards}</div>
        </div>
      </section>
      <section class="section">
        <div class="container">
          <div class="section-header">
            <h2>Featured project work</h2>
            <p>Each project is designed to show how I think about responsible AI, business value, and enterprise adoption patterns.</p>
          </div>
          <div class="project-grid">{project_cards}</div>
        </div>
      </section>
      <section class="section">
        <div class="container">
          <div class="section-header">
            <h2>Certification focus</h2>
            <p>My learning path is intentionally aligned to the Azure AI and administrator foundation required for AI enablement leadership.</p>
          </div>
          <div class="cert-grid">{cert_cards}</div>
        </div>
      </section>
    </main>
    """
    return render_page("AI Enablement Portfolio", "/", body)


@app.get("/projects", response_class=HTMLResponse)
async def projects():
    project_cards = render_project_cards(PROJECTS)
    body = f"""
    <main>
      <section class="page-hero">
        <div class="container">
          <span class="kicker">Project portfolio</span>
          <h1>AI projects built to show capability, value, and execution.</h1>
          <p>These projects capture the type of problem-solving I want to bring to AI Enablement Lead roles: secure architecture, practical use cases, and measurable business outcomes.</p>
        </div>
      </section>
      <section class="section">
        <div class="container project-grid">{project_cards}</div>
      </section>
    </main>
    """
    return render_page("Project Portfolio", "/projects", body)


@app.get("/projects/{slug}", response_class=HTMLResponse)
async def project_detail(slug: str):
    project = next((item for item in PROJECTS if item["slug"] == slug), None)
    if project is None:
        return render_page(
            "Project Not Found",
            "/projects",
            """
            <main>
              <section class="page-hero">
                <div class="container">
                  <span class="kicker">404</span>
                  <h1>Project not found.</h1>
                  <p>The requested project page does not exist yet. Explore the current portfolio to see the active case studies.</p>
                  <a class="btn btn-primary" href="/projects">View all projects</a>
                </div>
              </section>
            </main>
            """,
        )

    related = ''.join(
        f'<li><a href="/projects/{item["slug"]}">{item["title"]}</a></li>'
        for item in PROJECTS if item["slug"] != project["slug"]
    )
    tools = ''.join(f'<li>{tool}</li>' for tool in project["stack"])
    body = f"""
    <main>
      <section class="page-hero">
        <div class="container">
          <span class="kicker">{project['category']}</span>
          <h1>{project['title']}</h1>
          <p>{project['summary']}</p>
        </div>
      </section>
      <section class="section">
        <div class="container detail-shell">
          <article class="article-panel">
            <h2>Project story</h2>
            <p>{project['story']}</p>
            <h2>Business outcome</h2>
            <p>{project['outcome']}</p>
            <h2>Technology stack</h2>
            <ul>{tools}</ul>
          </article>
          <aside class="sidebar-panel">
            <h3>Why it matters</h3>
            <p>This project is designed to demonstrate the kind of situational awareness recruiters look for in AI enablement leaders: practical use-case selection, governance thinking, and operational readiness.</p>
            <h3>Related projects</h3>
            <ul class="sidebar-list">{related}</ul>
          </aside>
        </div>
      </section>
    </main>
    """
    return render_page(project["title"], "/projects", body)


@app.get("/about", response_class=HTMLResponse)
async def about():
    cert_list = ''.join(
        f'<li><strong>{cert["name"]}</strong> — {cert["status"]}</li>' for cert in CERTIFICATIONS
    )
    body = f"""
    <main>
      <section class="page-hero">
        <div class="container">
          <span class="kicker">About this portfolio</span>
          <h1>Designed for AI Enablement leadership roles.</h1>
          <p>This portfolio is intentionally shaped for recruiters and hiring managers evaluating AI transformation, governance, and adoption work. It highlights strategic thinking and technical hands-on execution, while showing a clear path toward AI-103 and AZ-104 certification readiness.</p>
        </div>
      </section>
      <section class="section">
        <div class="container detail-shell">
          <article class="article-panel">
            <h2>My focus</h2>
            <p>I am building a portfolio around practical Azure AI use cases, secure architecture patterns, and reusable enablement strategies. My work is centered on helping organizations move from AI experimentation to operational maturity.</p>
            <p>The approach combines solution design, governance awareness, and communication skills to connect technical work to business outcomes. That is the lens I want recruiters to see when they review my projects and certification progress.</p>
            <h2>Why this site is structured this way</h2>
            <p>I chose a single-domain portfolio with /projects/ pages because it keeps the site easy to navigate, review, and maintain while still allowing future expansion to project-specific subdomains or microsites later. This gives flexibility without sacrificing clarity for recruiters.</p>
          </article>
          <aside class="sidebar-panel">
            <h3>Current certification path</h3>
            <ul class="sidebar-list">{cert_list}</ul>
          </aside>
        </div>
      </section>
    </main>
    """
    return render_page("About the Portfolio", "/about", body)


@app.get("/health")
async def health_check():
    return {"status": "healthy", "runtime": "Python 3.13"}