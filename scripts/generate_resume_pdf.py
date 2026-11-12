#!/usr/bin/env python3
"""
generate_resume_pdf.py
Compiles templates/resume.html into a high-DPI executive resume PDF
using macOS Google Chrome in headless print mode, verifies strict 2-page pagination,
exports page preview images, and audits target strings.
"""

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = BASE_DIR / "templates" / "resume.html"
OUTPUT_RESUME_PDF = BASE_DIR / "static" / "Nathan_Lester_Resume.pdf"
OUTPUT_EXEC_PDF = BASE_DIR / "static" / "Nathan_Lester_Executive_Resume.pdf"
OUTPUT_DATED_PDF = BASE_DIR / "static" / "Nathan-Lester-Resume-20261112.pdf"
BACKUP_EXEC_PDF = BASE_DIR / "static" / "Nathan_Lester_Executive_Resume.original.pdf"
PREVIEW_P1 = BASE_DIR / "static" / "img" / "resume_page1_preview.png"
PREVIEW_FULL = BASE_DIR / "static" / "img" / "resume_full_preview.png"
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def check_prerequisites():
    if not TEMPLATE_PATH.exists():
        print(f"Error: Template not found at {TEMPLATE_PATH}", file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(CHROME_PATH):
        print(f"Error: Google Chrome binary not found at {CHROME_PATH}", file=sys.stderr)
        sys.exit(1)


def audit_template_content():
    print("--> Auditing template content requirements...")
    html_content = TEMPLATE_PATH.read_text(encoding="utf-8")

    required_terms = [
        "hello@nathanscottlester.com",
        "www.nathanscottlester.com",
        "(888) 600-3783",
        "AI-103",
    ]
    for term in required_terms:
        if term not in html_content:
            print(f"ERROR: Required term '{term}' not found in template!", file=sys.stderr)
            sys.exit(1)

    print("--> PASSED: Template strictly adheres to all text inclusion rules.")


def generate_pdf():
    print(f"--> Rendering PDF from {TEMPLATE_PATH.name}...")
    OUTPUT_RESUME_PDF.parent.mkdir(parents=True, exist_ok=True)

    # Backup original executive resume if not already backed up
    if OUTPUT_EXEC_PDF.exists() and not BACKUP_EXEC_PDF.exists():
        shutil.copy2(OUTPUT_EXEC_PDF, BACKUP_EXEC_PDF)
        print(f"--> Backed up original executive resume to {BACKUP_EXEC_PDF.name}")

    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={OUTPUT_RESUME_PDF}",
        f"file://{TEMPLATE_PATH.resolve()}",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Chrome PDF generation failed: {result.stderr}", file=sys.stderr)
        sys.exit(result.returncode)

    if not OUTPUT_RESUME_PDF.exists() or OUTPUT_RESUME_PDF.stat().st_size == 0:
        print("Error: PDF was not generated or has 0 bytes.", file=sys.stderr)
        sys.exit(1)

    # Sync to Nathan_Lester_Executive_Resume.pdf and Nathan-Lester-Resume-20261112.pdf
    shutil.copy2(OUTPUT_RESUME_PDF, OUTPUT_EXEC_PDF)
    shutil.copy2(OUTPUT_RESUME_PDF, OUTPUT_DATED_PDF)

    print(f"--> PDF successfully generated at {OUTPUT_RESUME_PDF} ({OUTPUT_RESUME_PDF.stat().st_size:,} bytes).")
    print(f"--> Updated {OUTPUT_EXEC_PDF} and {OUTPUT_DATED_PDF}.")


def verify_page_count():
    print("--> Verifying strict 2-page pagination...")
    pdf_bytes = OUTPUT_RESUME_PDF.read_bytes()
    matches = re.findall(rb"/Type\s*/Page\b", pdf_bytes)
    count = len(matches)
    print(f"Detected PDF Page Count: {count}")
    if count != 2:
        print(f"ERROR: Expected strictly 2 pages, found {count} pages!", file=sys.stderr)
        sys.exit(1)
    print("--> PASSED: Strictly 2-page boundary verified.")


def generate_previews():
    print("--> Generating high-res visual previews via Chrome...")
    PREVIEW_P1.parent.mkdir(parents=True, exist_ok=True)

    cmd_p1 = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        f"--screenshot={PREVIEW_P1}",
        "--window-size=816,1056",
        f"file://{TEMPLATE_PATH.resolve()}",
    ]
    subprocess.run(cmd_p1, capture_output=True, text=True)

    cmd_full = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        f"--screenshot={PREVIEW_FULL}",
        "--window-size=816,2150",
        f"file://{TEMPLATE_PATH.resolve()}",
    ]
    subprocess.run(cmd_full, capture_output=True, text=True)

    if PREVIEW_P1.exists():
        print(f"--> Saved Page 1 preview to {PREVIEW_P1} ({PREVIEW_P1.stat().st_size:,} bytes)")
    if PREVIEW_FULL.exists():
        print(f"--> Saved Full 2-page preview to {PREVIEW_FULL} ({PREVIEW_FULL.stat().st_size:,} bytes)")


def main():
    check_prerequisites()
    audit_template_content()
    generate_pdf()
    verify_page_count()
    generate_previews()
    print("\nSUCCESS: Executive resume PDF generated, audited, and verified!")


if __name__ == "__main__":
    main()
