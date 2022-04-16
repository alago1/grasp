import pytest
from PIL import Image

# pylint: disable=too-few-public-methods, import-error
from src.text_detection import detect_text


class TextDetectionProxy:
    """Proxy class for testing Text Detection with little fuss"""

    @staticmethod
    def clean_text(
        filename: str, case_sensitive: bool = False, strip: bool = True
    ) -> str:
        """
        Given filename, creates PIL Image from src/tests/data/filename
        and parses text and clears case sensitivity and newlines.
        """

        img = Image.open(f"src/tests/data/{filename}")
        text = detect_text(img)

        if not case_sensitive:
            text = text.lower()

        if strip:
            text = text.strip()

        return text  # type: ignore


def test_handwritten_text() -> None:
    """test handwritting detection"""
    assert TextDetectionProxy.clean_text("helloworld.jpg") == "hello world!"


def test_handwritten_math_jargon() -> None:
    """test that complex mathematical jargon gets detected in handwritten text"""
    text = TextDetectionProxy.clean_text("handwritten1.png")
    assert "extreme value theorem" in text
    assert "intermediate value" in text


def test_typed_math_jargon() -> None:
    """test that complex mathematical jargon gets detected in typed text"""
    text = TextDetectionProxy.clean_text("probability.1130400.jpg")
    assert "expectation of discrete random variables" in text
    assert "expected value" in text
    assert "common probability space" in text


def test_lower_resolution() -> None:
    """test lower resolution images"""
    assert "example of use case diagram" in TextDetectionProxy.clean_text(
        "lowres_diagram.png"
    )


def test_slight_blur() -> None:
    """test text detection of images with slight blur"""
    assert TextDetectionProxy.clean_text("aerodynamics.png") == "aerodynamics of a cow"


def test_high_blur() -> None:
    """test very blurry images are detected"""
    text = TextDetectionProxy.clean_text("blurry.jpg")
    assert "this is blurry text h1" in text
    assert "this is blurry text h2" in text
    assert "this is blurry text h3" in text


@pytest.mark.xfail(reason="input needs to be cleaned")
def test_stylized_logo() -> None:  # type: ignore
    """test text detection recognizes styling"""
    assert TextDetectionProxy.clean_text("f12022.png") == "2022"


def test_stylized_logo2() -> None:
    """test text detection within a logo"""
    assert TextDetectionProxy.clean_text("uf_uav_logo.png") == "uf\nuav"


def test_rotated_text() -> None:
    """test slightly rotated text is recognized"""
    assert TextDetectionProxy.clean_text("value_menu.png") == "value menu"


def test_inner_text() -> None:
    """test off-focus inner text is detected"""
    text = TextDetectionProxy.clean_text("starship.png")
    assert "tanker" in text
    assert "lunar" in text
    assert "texas" in text
