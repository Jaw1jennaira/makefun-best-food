"""Runner for the food-picture-01 entry: Golden Hour Salmon.

This script takes the finished dish photograph that ships with the
repository and places an exact copy of it in the output directory,
so the competition harness can collect the entry image.
"""

import os
import shutil
from pathlib import Path

ENTRY_IMAGE = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def main() -> None:
    """Copy the entry photograph into the output directory."""
    # Copy the image byte-for-byte without re-encoding.
    source = Path(__file__).resolve().parent / ENTRY_IMAGE
    # The destination keeps every byte of the source file intact.
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, output_dir / ENTRY_IMAGE)


if __name__ == "__main__":
    main()
