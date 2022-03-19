from PIL import Image

from text_detection import detect_text

OUT = detect_text(Image.open("src/tests/data/probability.1130400.jpg"))
print(OUT)
