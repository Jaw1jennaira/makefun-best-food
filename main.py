"""Golden Hour Salmon entry runner.

Copies the entry image (pan-seared salmon, golden hour light) to the
output directory make.fun grades.

The copy is byte-for-byte: no re-encoding, no resize.
"""
import os
import shutil

ENTRY_FILENAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(out, exist_ok=True)
    shutil.copyfile(os.path.join(here, ENTRY_FILENAME), os.path.join(out, ENTRY_FILENAME))


if __name__ == "__main__":
    main()
