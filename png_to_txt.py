from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image
import pytesseract


def convert_png_to_text(png_path: Path, output_path: Path | None = None) -> Path:
    """Convert a PNG image containing text into a plain-text file.

    Args:
        png_path: Path to the PNG image.
        output_path: Optional path for the resulting text file. Defaults to the
            PNG path with a ``.txt`` suffix.

    Returns:
        Path to the generated text file.
    """

    if not png_path.exists():
        raise FileNotFoundError(f"PNG file not found: {png_path}")

    if output_path is None:
        output_path = png_path.with_suffix(".txt")

    image = Image.open(png_path)
    text = pytesseract.image_to_string(image)

    # Ensure the output ends with a newline for readability.
    if text and not text.endswith("\n"):
        text += "\n"

    output_path.write_text(text, encoding="utf-8")
    return output_path


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert text from a PNG image into a plain-text file using OCR.",
    )
    parser.add_argument("png", type=Path, help="Path to the PNG image to convert")
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        help="Optional output path for the generated .txt file",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    output_path = convert_png_to_text(args.png, args.output)
    print(f"Text saved to {output_path}")


if __name__ == "__main__":
    main()
