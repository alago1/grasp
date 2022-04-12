import io
from typing import List

from google.cloud import vision
from PIL import Image


# ADD: Consider including a layer to processes out Watermarks and Logos
def detect_text(image: Image.Image) -> str:
    """Detects text in the file."""

    client = vision.ImageAnnotatorClient()

    temp = io.BytesIO()
    image.save(temp, format="PNG")
    content = temp.getvalue()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    out: List[str] = []

    for text in texts:
        out.append(text.description)

    if response.error.message:
        raise Exception(
            "{response.error.message}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors"
        )

    return out[0] if len(out) > 0 else ""
