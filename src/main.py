import io
from text_detection import detect_text
from typing import Iterator
from PIL import Image


def pathToIter(inStr : str) -> Iterator[Image.Image]:
    im = Image.open(inStr) 
    yield im
    
out = detect_text(pathToIter("src/tests/data/probability.1130400.jpg"))
print(out[0])

#detect_text("src/tests/data/unknown.png")
