from PIL import Image

from text_detection import detect_text

# will fail
assert detect_text(Image.open("src/tests/data/probability.1130400.jpg")) == ""
