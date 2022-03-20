import io

from google.cloud import vision
from PIL import Image


def detect_text(image: Image.Image) -> str:
    """Detects text in the file."""

    client = vision.ImageAnnotatorClient()

    temp = io.BytesIO()
    image.save(temp, format="PNG")
    content = temp.getvalue()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    out = []

    for text in texts:
        # print('\n"{}"'.format(text.description))
        out.append(text.description)

        # vertices = [
        #     f"({vertex.x},{vertex.y})"
        #     for vertex in text.bounding_poly.vertices
        # ]

    if response.error.message:
        raise Exception(
            "{response.error.message}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors"
        )

    return out[0] if len(out) > 0 else ""
