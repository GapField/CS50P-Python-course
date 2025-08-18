# pip install pypdf2
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path
import math

def split_pdf_in_half(input_path, out_dir=None):
    input_path = Path(input_path)
    out_dir = Path(out_dir) if out_dir else input_path.with_suffix('')
    out_dir.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(str(input_path))
    n = len(reader.pages)
    mid = math.ceil(n / 2)  # first half gets the extra page if n is odd

    halves = [(1, mid), (mid + 1, n)] if n > 1 else [(1, 1)]

    for i, (start, end) in enumerate(halves, start=1):
        writer = PdfWriter()
        # convert to 0-based indices for PyPDF2
        for p in range(start - 1, end):
            writer.add_page(reader.pages[p])
        out_file = out_dir / f"{input_path.stem}_half{i}_{start}-{end}.pdf"
        with open(out_file, "wb") as f:
            writer.write(f)

    print(f"Done. Halves saved to: {out_dir.resolve()} (pages {halves[0]} and {halves[1]})")

# Example:
split_pdf_in_half("C:/Users/Coldf/Downloads/Formblatt03_Howard.pdf")
