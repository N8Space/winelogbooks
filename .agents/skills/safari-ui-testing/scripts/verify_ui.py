#!/usr/bin/env python3
"""
macOS Native Browser UI/UX Verification Script
Uses native safaridriver (or system Chrome fallback) via Selenium.
Captures responsive screenshots across Desktop, Tablet, and Mobile viewports.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

VIEWPORTS = {
    "desktop": (1440, 900),
    "tablet": (768, 1024),
    "mobile": (375, 812)
}


def get_driver(browser_choice="auto"):
    """
    Initializes a WebDriver.
    Attempts Safari first if 'auto' or 'safari' is requested.
    Falls back to headless system Chrome if Safari remote automation is disabled.
    """
    if browser_choice in ("safari", "auto"):
        try:
            print("🚀 Attempting to launch macOS native Safari (safaridriver)...")
            driver = webdriver.Safari()
            print("✓ Safari WebDriver session established.")
            return driver, "safari"
        except Exception as e:
            err_msg = str(e)
            if "Allow remote automation" in err_msg or "SessionNotCreatedException" in type(e).__name__:
                print("⚠️ Safari remote automation is not enabled.")
                print("   To enable Safari: Open Safari > Settings > Advanced > check 'Show features for web developers'")
                print("   Then click Develop > Allow Remote Automation (or run: sudo safaridriver --enable).")
            else:
                print(f"⚠️ Safari launch error: {e}")

            if browser_choice == "safari":
                print("❌ Exiting: Safari was explicitly requested but could not start.")
                sys.exit(1)

            print("🔄 Falling back to system Chrome (headless)...")

    # Chrome fallback
    from selenium.webdriver.chrome.options import Options
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=opts)
    print("✓ System Chrome WebDriver session established (headless).")
    return driver, "chrome"


def verify_page(url, browser="auto", output_dir="screenshots", viewports=None):
    if viewports is None:
        viewports = ["desktop", "tablet", "mobile"]

    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    driver, active_browser = get_driver(browser)
    results = {
        "url": url,
        "browser": active_browser,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "screenshots": {},
        "elements_found": {},
        "interactions": []
    }

    try:
        print(f"\n🌐 Navigating to: {url}")
        driver.get(url)
        time.sleep(1.5)

        results["title"] = driver.title
        print(f"📄 Page Title: {driver.title}")

        # Check key components
        for sel, name in [
            ("header.site-header", "header"),
            ("table.matrix-table", "matrix_tables"),
            (".simulator-panel", "decision_simulator"),
            (".code-window", "code_window"),
            (".best-practices-grid", "best_practices"),
            ("footer.footer", "footer")
        ]:
            elems = driver.find_elements(By.CSS_SELECTOR, sel)
            results["elements_found"][name] = len(elems)
            print(f"   • {name}: {len(elems)} found")

        # Test interactive components if on the blueprint page
        sim_buttons = driver.find_elements(By.CSS_SELECTOR, ".sim-btn")
        if sim_buttons:
            print(f"⚡ Testing {len(sim_buttons)} simulator preset buttons...")
            for btn in sim_buttons[:2]:
                btn_text = btn.text
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                time.sleep(0.3)
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(0.4)
                results["interactions"].append(f"Clicked simulator button: {btn_text}")

        # Test copy prompt button if present
        copy_btns = driver.find_elements(By.ID, "copyPromptBtn")
        if copy_btns:
            print("📋 Testing Copy Prompt button...")
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", copy_btns[0])
            time.sleep(0.3)
            driver.execute_script("arguments[0].click();", copy_btns[0])
            time.sleep(0.5)
            btn_text_after = copy_btns[0].text
            results["interactions"].append(f"Clicked copyPromptBtn (text: {btn_text_after})")

        # Capture responsive viewports
        for vp_name in viewports:
            if vp_name not in VIEWPORTS:
                continue
            width, height = VIEWPORTS[vp_name]
            print(f"📸 Capturing {vp_name.upper()} viewport ({width}x{height})...")
            driver.set_window_size(width, height)
            time.sleep(0.8)

            file_name = f"{vp_name}_{int(time.time())}.png"
            file_path = out_path / file_name
            driver.save_screenshot(str(file_path))
            results["screenshots"][vp_name] = str(file_path)
            print(f"   Saved to: {file_path}")

        print("\n✅ Verification and screenshot capture complete!")

    finally:
        driver.quit()
        print("🛑 WebDriver session closed.")

    return results


def main():
    parser = argparse.ArgumentParser(description="Verify UI/UX and capture responsive screenshots using Safari/Selenium.")
    parser.add_argument("--url", default="http://127.0.0.1:8000/projects/ai-engineer-blueprint", help="Target URL to test")
    parser.add_argument("--browser", choices=["auto", "safari", "chrome"], default="auto", help="Browser engine")
    parser.add_argument("--output-dir", default="static/img/screenshots", help="Directory to save screenshots")
    parser.add_argument("--viewport", choices=["desktop", "tablet", "mobile", "all"], default="all", help="Viewport to capture")

    args = parser.parse_args()
    vps = ["desktop", "tablet", "mobile"] if args.viewport == "all" else [args.viewport]

    results = verify_page(args.url, browser=args.browser, output_dir=args.output_dir, viewports=vps)
    print("\n--- Summary Report ---")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
