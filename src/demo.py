# pylint: disable=invalid-name, unused-import
from PIL import Image

from pipeline import process_references
from reference_producer import get_references
from text_detection import detect_text

# text = detect_text(Image.open("src/tests/data/probability.1130400.jpg"))
# print(f"DEMO TEXT DETECTION:\n{text}\n\n")

# refers = get_references(text)
# print(f"DEMO REFERENCES:\n{refers}")

tsrefs = process_references(
    "/home/allanlago/Documents/uf/cen3032/imgBuffer/data/probability.mp4"
)
for tsp, refs in tsrefs:
    print(f"Timestamp: {tsp}")
    print(tsrefs)
