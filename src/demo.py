from PIL import Image

from reference_producer import get_references
from text_detection import detect_text

# pylint: disable=invalid-name

text = detect_text(Image.open("src/tests/data/probability.1130400.jpg"))
print(f"DEMO TEXT DETECTION:\n{text}\n\n")

refers = get_references(text)
print(f"DEMO REFERENCES:\n{refers}")
