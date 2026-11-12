#!/usr/bin/env python3
"""
generate_strategy_pdf.py
Compiles templates/connecting_business_strategy_applied_ai.html into a pixel-perfect,
single-page PDF using macOS Google Chrome in headless print mode, and verifies
that the page count is strictly 1 via macOS PDFKit.
"""

import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = BASE_DIR / "templates" / "connecting_business_strategy_applied_ai.html"
OUTPUT_PDF = BASE_DIR / "static" / "Nathan_Lester_Connecting_Business_Strategy_Applied_AI.pdf"
OUTPUT_PREVIEW = BASE_DIR / "static" / "img" / "strategy_brief_preview.png"
ARTIFACT_DIR = Path("/Users/natha/.gemini/antigravity-ide/brain/0adaefca-52eb-4f29-9a7c-510ceaed4dcb")
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def check_prerequisites():
    if not TEMPLATE_PATH.exists():
        print(f"Error: Template not found at {TEMPLATE_PATH}", file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(CHROME_PATH):
        print(f"Error: Google Chrome binary not found at {CHROME_PATH}", file=sys.stderr)
        sys.exit(1)


def generate_pdf():
    print(f"--> Rendering PDF from {TEMPLATE_PATH.name}...")
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={OUTPUT_PDF}",
        f"file://{TEMPLATE_PATH.resolve()}",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Chrome PDF generation failed: {result.stderr}", file=sys.stderr)
        sys.exit(result.returncode)

    if not OUTPUT_PDF.exists() or OUTPUT_PDF.stat().st_size == 0:
        print("Error: PDF was not generated or has 0 bytes.", file=sys.stderr)
        sys.exit(1)

    print(f"--> PDF successfully generated at {OUTPUT_PDF} ({OUTPUT_PDF.stat().st_size:,} bytes).")


def verify_page_count_and_export_preview():
    print("--> Verifying strict 1-page boundary with macOS PDFKit...")
    swift_script = f"""
    import Foundation
    import PDFKit
    import AppKit

    let pdfPath = "{OUTPUT_PDF}"
    let previewPath = "{OUTPUT_PREVIEW}"
    let url = URL(fileURLWithPath: pdfPath)

    guard let doc = PDFDocument(url: url) else {{
        print("FAIL: Could not open generated PDF document.")
        exit(1)
    }}

    let count = doc.pageCount
    print("PDF Page Count: \\(count)")

    if count != 1 {{
        print("ERROR: PDF has \\(count) pages, but must be STRICTLY 1 PAGE.")
        exit(2)
    }}

    guard let page = doc.page(at: 0) else {{
        print("FAIL: Page 0 not found.")
        exit(3)
    }}

    let bounds = page.bounds(for: .mediaBox)
    print("Page MediaBox: \\(bounds.width) x \\(bounds.height) pt (US Letter: 612 x 792 pt)")

    // Export high-res preview image (2x scale for crisp rendering)
    let scale: CGFloat = 2.0
    let targetSize = CGSize(width: bounds.width * scale, height: bounds.height * scale)
    let image = NSImage(size: targetSize)
    image.lockFocus()
    if let ctx = NSGraphicsContext.current?.cgContext {{
        ctx.setFillColor(NSColor.white.cgColor)
        ctx.fill(CGRect(origin: .zero, size: targetSize))
        ctx.scaleBy(x: scale, y: scale)
        page.draw(with: .mediaBox, to: ctx)
    }}
    image.unlockFocus()

    guard let tiffData = image.tiffRepresentation,
          let rep = NSBitmapImageRep(data: tiffData),
          let pngData = rep.representation(using: .png, properties: [:]) else {{
        print("FAIL: Could not render preview image.")
        exit(4)
    }}

    do {{
        try pngData.write(to: URL(fileURLWithPath: previewPath))
        print("--> Preview image successfully saved to \\(previewPath) (\\(pngData.count) bytes)")
    }} catch {{
        print("FAIL: Could not write preview image: \\(error)")
        exit(5)
    }}
    """

    res = subprocess.run(["swift", "-e", swift_script], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Swift verification failed:\n{res.stdout}\n{res.stderr}", file=sys.stderr)
        sys.exit(res.returncode)

    print(res.stdout.strip())
    print("PASSED: PDF has exactly 1 page!")

    # Copy to artifact directory if available
    if ARTIFACT_DIR.exists():
        subprocess.run(["cp", str(OUTPUT_PDF), str(ARTIFACT_DIR / OUTPUT_PDF.name)])
        subprocess.run(["cp", str(OUTPUT_PREVIEW), str(ARTIFACT_DIR / OUTPUT_PREVIEW.name)])
        print(f"--> Copied PDF and preview to {ARTIFACT_DIR}")


def main():
    check_prerequisites()
    generate_pdf()
    verify_page_count_and_export_preview()
    print("SUCCESS: 1-Page executive brief generated and verified!")


if __name__ == "__main__":
    main()
