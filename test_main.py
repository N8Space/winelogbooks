import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    html = response.text
    # Section 1: Hero & Positioning
    assert "Turning Enterprise Strategy into" in html
    assert "Practical AI Solutions" in html
    assert "AI Enablement &amp; Innovation Leader Applying AI" in html or "AI Enablement & Innovation Leader Applying AI" in html
    assert "McDonald&#39;s" in html or "McDonald's" in html
    assert "Scooter&#39;s Coffee" in html or "Scooter's Coffee" in html
    assert "regulated insurance carrier" in html
    assert "Physicians Mutual" not in html
    assert "linkedin.com" not in html
    assert "—" not in html
    assert "Chicago • Milwaukee • Indianapolis • Remote" in html
    assert "Download Resume (PDF)" in html
    assert "/static/Nathan_Lester_Executive_Resume.pdf" in html

    # Section 2: Differentiator Grid
    assert "Why Hands-On AI Enablement Matters" in html
    assert "Everyone can build with AI today" in html
    assert "Human-Centered Enablement &amp; Business Value" in html or "Human-Centered Enablement & Business Value" in html
    assert "Production Reality &amp; The Edge-Case Test" in html or "Production Reality & The Edge-Case Test" in html
    assert "Responsible Governance &amp; Cloud Discipline" in html or "Responsible Governance & Cloud Discipline" in html

    # Section 3: Case Studies (Business Focus)
    assert "Enterprise Knowledge Hub: Intelligent Search &amp; Retrieval" in html or "Enterprise Knowledge Hub: Intelligent Search & Retrieval" in html
    assert "Semi-Autonomous Agent Factory &amp; Harness" in html or "Semi-Autonomous Agent Factory & Harness" in html
    assert "Resume Refine: AI-Powered Career Assistant (Mobile iOS)" in html
    assert "featured-project" in html

    # Section 4 / Removed Sections Check
    assert "Technical Competency &amp; Ecosystem Matrix" not in html
    assert "Technical Competency & Ecosystem Matrix" not in html
    assert "Production AI Systems Architected" not in html
    assert "Executive AI Strategy" not in html

    # Section 5: Midwest Banner & Contact
    assert "Rooted in the Midwest" in html
    assert "hello@nathanscottlester.com" in html
    assert "Copy Direct Email" in html
    assert "Targeting roles in Chicago • Milwaukee • Indianapolis • Remote" in html


def test_resume_download_route():
    response = client.get("/static/Nathan_Lester_Executive_Resume.pdf")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert len(response.content) > 100


def test_projects_page():
    response = client.get("/projects")
    assert response.status_code == 200
    html = response.text
    assert "featured-project" in html
    assert "/projects/ai-sdlc-studio" in html
    assert "/projects/ai-engineer-blueprint" in html
    assert "Semi-Autonomous Agent Factory &amp; Harness" in html or "Semi-Autonomous Agent Factory & Harness" in html
    assert "resume-refine" in html
    assert "newsgenie" in html
    assert "azure-governance-dashboard" in html
    assert "intelligent-knowledge-hub" in html
    assert "—" not in html


def test_ai_sdlc_studio_case_study_route():
    response = client.get("/projects/ai-sdlc-studio")
    assert response.status_code == 200
    html = response.text
    assert "Semi-Autonomous Agent Factory &amp; Harness" in html or "Semi-Autonomous Agent Factory & Harness" in html
    assert "Autonomous AI SDLC Studio" not in html
    assert "automation.lesterlabs.cloud" not in html
    assert "ompression, and a complete multi-channel GTM launch kit." not in html
    assert "Architecture &amp; The AI Factory Loop" in html or "Architecture & The AI Factory Loop" in html
    assert "RegPulse" in html
    assert "Instant Change Detection &amp; Cost Control ($0 Fast-Paths)" in html or "Instant Change Detection & Cost Control ($0 Fast-Paths)" in html
    assert "Persistent Institutional Memory Bank" in html
    assert "Technology Stack &amp; Tooling" not in html
    assert "Technology Stack & Tooling" not in html
    assert "hello@nathanscottlester.com" in html
    assert "—" not in html


def test_ai_engineer_blueprint_route():
    response = client.get("/projects/ai-engineer-blueprint")
    assert response.status_code == 200
    html = response.text
    assert "The AI Engineer Blueprint: Architecture &amp; Deployment Decision Engine" in html or "The AI Engineer Blueprint: Architecture & Deployment Decision Engine" in html
    assert "What AI Architecture Do I Need?" in html
    assert "Where Should I Run It?" in html
    assert "Traditional ML / Rules" in html
    assert "Direct Prompting" in html
    assert "RAG (Retrieval-Augmented)" in html
    assert "Single Agent (with Tools)" in html
    assert "Multi-Agent / Swarm" in html
    assert "Local Machine / Edge" in html
    assert "Self-Hosted VPS (Hostinger)" in html or "Self-Hosted VPS" in html
    assert "Cloud Hyperscaler (Azure/AWS/GCP)" in html or "Cloud Hyperscaler" in html
    assert "The AI Engineer: System Instructions" in html
    assert "ai_engineer_system_prompt.md" in html
    assert "Start with Single Agents" in html
    assert "Modular Decoupled Design" in html
    assert "Acknowledge the ACI" in html
    assert "hello@nathanscottlester.com" in html
    assert "—" not in html


def test_existing_projects():
    for slug in ["newsgenie", "azure-governance-dashboard", "intelligent-knowledge-hub", "resume-refine"]:
        response = client.get(f"/projects/{slug}")
        assert response.status_code == 200
        assert "—" not in response.text


def test_about_page():
    response = client.get("/about")
    assert response.status_code == 200
    assert "hello@nathanscottlester.com" in response.text
    assert "McDonald" in response.text
    assert "Scooter" in response.text
    assert "regulated insurance carrier" in response.text
    assert "Physicians Mutual" not in response.text
    assert "—" not in response.text
    assert "Chicago" in response.text
    assert "Milwaukee" in response.text
    assert "Indianapolis" in response.text


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_not_found_project():
    response = client.get("/projects/unknown-slug")
    assert response.status_code == 200
    assert "Project not found" in response.text


def test_canonical_urls_and_metadata():
    home_resp = client.get("/")
    assert home_resp.status_code == 200
    assert '<link rel="canonical" href="https://www.nathanscottlester.com" />' in home_resp.text
    assert 'property="og:url" content="https://www.nathanscottlester.com"' in home_resp.text

    blueprint_resp = client.get("/projects/ai-engineer-blueprint")
    assert blueprint_resp.status_code == 200
    assert '<link rel="canonical" href="https://www.nathanscottlester.com/projects/ai-engineer-blueprint" />' in blueprint_resp.text

    studio_resp = client.get("/projects/ai-sdlc-studio")
    assert studio_resp.status_code == 200
    assert '<link rel="canonical" href="https://www.nathanscottlester.com/projects/ai-sdlc-studio" />' in studio_resp.text


def test_robots_txt():
    response = client.get("/robots.txt")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/plain")
    assert "Sitemap: https://www.nathanscottlester.com/sitemap.xml" in response.text


def test_sitemap_xml():
    response = client.get("/sitemap.xml")
    assert response.status_code == 200
    assert "application/xml" in response.headers["content-type"]
    assert "https://www.nathanscottlester.com" in response.text
    assert "https://www.nathanscottlester.com/projects/ai-sdlc-studio" in response.text
    assert "https://www.nathanscottlester.com/projects/ai-engineer-blueprint" in response.text

