import io
from tabnanny import verbose
from google.cloud import vision
from PIL import Image
from typing import Iterator, cast
from numpy import dtype


from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(
    'cloud_credentials.json')


# FIXME: output should be returned, not printed
def detect_text(im: Iterator[Image.Image]):
    """Detects text in the file."""

    client = vision.ImageAnnotatorClient(credentials=credentials)

    for image in im:
        temp = io.BytesIO()
        image.save(temp, format='PNG')
        content = temp.getvalue()

        image = vision.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations

        out = []
        i = 0

        for text in texts:
            #print('\n"{}"'.format(text.description))
            out.append(text.description)

            vertices = [
                "({},{})".format(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices
            ]



        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )
        
        return out
