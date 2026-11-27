#!/usr/bin/env python3
"""Render each page of a PDF as a PNG image."""

import argparse
from pathlib import Path


def positive_int(value: str) -> int:
    """Parse a positive integer argument."""
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be an integer") from exc
    if number <= 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return number


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="PDF file to convert")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        help="directory for PNGs (default: <pdf-name>_images next to the PDF)",
    )
    parser.add_argument(
        "--dpi",
        type=positive_int,
        default=150,
        help="render resolution in DPI (default: 150)",
    )
    args = parser.parse_args()

    if not args.pdf.is_file():
        parser.error(f"PDF file does not exist: {args.pdf}")

    output_dir = args.output_dir or args.pdf.with_name(f"{args.pdf.stem}_images")

    try:
        import pymupdf
    except ImportError:
        parser.error("PyMuPDF is required; install it with: python -m pip install pymupdf")

    output_dir.mkdir(parents=True, exist_ok=True)
    scale = args.dpi / 72

    with pymupdf.open(args.pdf) as document:
        for page_number, page in enumerate(document, start=1):
            image = page.get_pixmap(
                matrix=pymupdf.Matrix(scale, scale),
                alpha=False,
            )
            image.save(output_dir / f"page-{page_number:03}.png")

    print(f"Converted {len(document)} pages to PNGs in {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
