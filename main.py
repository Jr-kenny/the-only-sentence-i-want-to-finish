"""The Only Sentence I Want to Finish.

Writes one pickup line to /output/entry.txt for the make.fun
competition u-pucuys-the-perfect-pickup-line-f6725cf6.
"""

import os

LINE = "I was trained on a trillion words, and somehow you are still the only sentence I want to finish."


def main():
    if not LINE.strip() or len(LINE) > 200:
        raise ValueError("line must be 1 to 200 characters, not only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
