from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    html = response.text

    # 1. Explanation of who Nathan is with language from the "Executive Story" page
    assert "McDonald's" in html or "McDonald&#39;s" in html
    assert "Voice-Activated Drive-Thru Order Taker" in html
    assert "Scooter's Coffee" in html or "Scooter&#39;s Coffee" in html
    assert "regulated insurance carrier" in html
    assert "eliminate routine drudgery" in html
    assert "What should you build, and how do you design it so teams adopt it safely and reliably?" in html
    assert "Chicago, IL, Milwaukee, WI, and Indianapolis, IN" in html

    # 2. YouTube video kept as-is + updated language below + 3 required links
    assert "https://www.youtube-nocookie.com/embed/V-cfCoKe1TQ" in html
    assert "Specializing in practical AI enablement, solution architecture, and operational readiness." in html
    assert "operational readiness, and cloud governance across enterprise environments" not in html
    assert 'href="/static/Nathan-Lester-Resume-20261112.pdf"' in html
    assert 'href="tel:+18886003783"' in html
    assert 'href="mailto:hello@nathanscottlester.com"' in html

    # 3. Other main content removed; replaced with 3 case study placeholders
    assert "Why Hands-On AI Enablement Matters" not in html
    assert "Semi-Autonomous Agent Factory" not in html
    assert "Knowledge Hub Chatbot" in html
    assert "News Chatbot with Tools" in html
    assert "AI Voice Assistant" in html
    assert "The Problem" in html
    assert "The Solution" in html
    assert "https://github.com/N8Space/intelligent-knowledge-hub" in html
    assert "https://github.com/N8Space/NewsGenie" in html

    # 4. AI Voice Assistant card on main page: no "Try AI Voice Assistant", no private GitHub link,
    # and "View Full Case Study" placed in footer actions
    assert "Try AI Voice Assistant" not in html
    assert "https://github.com/N8Space/call-agent" not in html
    assert '<a class="btn btn-primary" href="/projects/call-agent">View Full Case Study →</a>' in html
    assert '<span class="btn-phone-number">+1 (888) 600-3783</span>' in html

    # Case study card upper-right icons
    assert "case-study-icon--kb" in html
    assert "case-study-icon--newsgenie" in html
    assert "case-study-icon--voice" in html

    # Updated Knowledge Hub Chatbot copy on main page
    assert "I saw support teams spending too much time digging through online reference pages" in html
    assert "I built an example for demonstration that is a hybrid search chatbot hosted on Azure App Service" in html
    assert "[Placeholder:" not in html

    # Updated News Chatbot with Tools copy on main page
    assert "I built this because standard AI models are frozen in time at their training cutoff." in html
    assert "I designed this assistant to figure out what a user is actually asking and pick the right tool for the job." in html

    # Updated AI Voice Assistant copy on main page
    assert "I built this because I stay busy and didn't want to miss an important call" in html
    assert "I designed this as a dependable voice assistant that works right out of the box." in html
    assert "stop losing prospects and end the game of phone tag." in html

    # 5. Bottom "Rooted in the Midwest..." section removed
    assert "Rooted in the Midwest" not in html

    # 6. Footer kept
    assert '<footer class="footer">' in html
    assert "Targeting roles in Chicago • Milwaukee • Indianapolis • Remote" in html

    # 7 & 8. Nav links to Case Studies (/projects) and Executive Story (/about) removed
    assert 'href="/projects"' not in html
    assert 'href="/about"' not in html
    assert "Executive Story" not in html


def test_removed_pages_return_404():
    assert client.get("/projects").status_code == 404
    assert client.get("/about").status_code == 404


def test_ai_voice_assistant_case_page():
    for path in ["/projects/call-agent", "/projects/ai-voice-assistant"]:
        response = client.get(path)
        assert response.status_code == 200
        html = response.text
        # a. Heading updated to "My AI Voice Assistant"
        assert "<h1>My AI Voice Assistant</h1>" in html
        assert 'AI Voice Assistant ("Nova") &amp; Missed-Call Recovery' not in html
        # b. Nova avatar image included
        assert '/static/img/nova-avatar.png' in html
        # c. Updated subtitle copy under heading
        assert (
            "Nova is built to answer inbound phone calls, book live appointments during the call, "
            "text back callers if they hang up before scheduling, and answer questions about me on my behalf."
        ) in html
        # d. System Specs in dedicated card in main body
        assert 'class="system-specs-card"' in html
        assert "System Specs" in html
        # e. Sidebar Quick Links removed
        assert "Quick Links" not in html
        # f. Architectural Stack and Modular Calendar Provider Architecture removed
        assert "Architectural Stack" not in html
        assert "Modular Calendar Provider Architecture" not in html
        # h. All references to GitHub repo ("N8Space/call-agent") removed
        assert "N8Space/call-agent" not in html
        assert "https://github.com/N8Space/call-agent" not in html
        # i. Download link for architecture-diagram.png included
        assert 'href="/static/img/call-agent-architecture.png" download="architecture-diagram.png"' in html
        # j. Repository Structure horizontal scroll controls/affordance included
        assert 'id="repo-structure-pre"' in html
        assert "Scroll horizontally" in html
        assert '/static/img/toll-free-opt-in-workflow.jpg' in html
        assert "Try AI Voice Assistant in Browser" not in html
        assert '<footer class="footer">' in html


def test_call_agent_assets_served():
    arch_resp = client.get("/static/img/call-agent-architecture.png")
    assert arch_resp.status_code == 200
    assert arch_resp.headers["content-type"] == "image/png"

    optin_resp = client.get("/static/img/toll-free-opt-in-workflow.jpg")
    assert optin_resp.status_code == 200
    assert optin_resp.headers["content-type"] == "image/jpeg"

    nova_png_resp = client.get("/static/img/nova-avatar.png")
    assert nova_png_resp.status_code == 200
    assert nova_png_resp.headers["content-type"] == "image/png"

    nova_avif_resp = client.get("/static/img/nova-avatar.avif")
    assert nova_avif_resp.status_code == 200


def test_resume_download_served():
    for path in [
        "/static/Nathan-Lester-Resume-20261112.pdf",
        "/static/Nathan_Lester_Resume.pdf",
        "/static/Nathan_Lester_Executive_Resume.pdf",
    ]:
        response = client.get(path)
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/pdf"
        assert len(response.content) > 1000


def test_voice_agent_modal_and_script():
    for path in ["/", "/projects/call-agent"]:
        html = client.get(path).text
        assert '<dialog id="voice-agent-modal"' in html
        assert "Call Nova" in html
        assert "<span>Nathan Lester's AI Assistant</span>" in html
        assert '<span class="voice-subtitle-line">Connected to Live Calendar</span>' in html
        assert "Dial from your phone to speak with Nova" in html
        assert "Start Voice Call" not in html
        assert "browser microphone" not in html
        assert 'src="/static/voice-agent.js"' in html

    js_resp = client.get("/static/voice-agent.js")
    assert js_resp.status_code == 200
    for fn in ["copyPhone", "openVoiceAgentModal", "closeVoiceAgentModal"]:
        assert f"window.{fn} = {fn}" in js_resp.text


def test_health_robots_and_sitemap():
    health = client.get("/health")
    assert health.status_code == 200
    assert health.json()["status"] == "healthy"

    robots = client.get("/robots.txt")
    assert robots.status_code == 200
    assert "Sitemap: https://www.nathanscottlester.com/sitemap.xml" in robots.text

    sitemap = client.get("/sitemap.xml")
    assert sitemap.status_code == 200
    assert "https://www.nathanscottlester.com/projects/call-agent" in sitemap.text
    assert "https://www.nathanscottlester.com/projects</loc>" not in sitemap.text
    assert "https://www.nathanscottlester.com/about" not in sitemap.text
