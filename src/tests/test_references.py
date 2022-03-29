from typing import Set

# pylint: disable=too-few-public-methods, import-error
from src.reference_producer import NLP_MODEL


class ReferenceProducerProxy:
    """
    Proxy class to help with testing
    """

    @staticmethod
    def get_keywords(text: str) -> Set[str]:
        """
        Given text string, uses NLP_MODEL to identify
        key noun_chunks. Returns list of keywords.
        """
        text = text.strip().lower()
        return set(str(x) for x in NLP_MODEL(text).noun_chunks)


def test_scientific_keywords() -> None:
    """test NLP_MODEL highlights scientific jargon"""

    # https://en.wikipedia.org/wiki/Maxwell%27s_equations?oldformat=true
    keywords = ReferenceProducerProxy.get_keywords(
        "Maxwell's equations are a set of coupled "
        "partial differential equations that, together with the "
        "Lorentz force law, form the foundation of classical "
        "electromagnetism, classical optics, and electric circuits"
    )

    assert "maxwell's equations" in keywords
    assert "coupled partial differential equations" in keywords
    assert "the lorentz force law" in keywords
    assert "classical electromagnetism" in keywords
    assert "classical optics" in keywords
    assert "electric circuits" in keywords


def test_computer_science_keywords() -> None:
    """test NLP_MODEL highlights computer science jargon"""

    # https://en.wikipedia.org/wiki/Rust_(programming_language)?oldformat=true
    keywords = ReferenceProducerProxy.get_keywords(
        "Rust is a multi paradigm, general-purpose programming language "
        "designed for performance and safety, especially safe concurrency. "
        "Rust is syntactically similar to C++,[14] but can guarantee "
        "memory safety by using a borrow checker to validate references."
    )

    assert "a multi paradigm" in keywords
    assert "general-purpose programming language" in keywords
    assert "especially safe concurrency" in keywords
    assert "memory safety" in keywords
    assert "a borrow checker" in keywords


def test_mathematics_keywords() -> None:
    """test NLP_MODEL highlights mathematics jargon"""

    # https://en.wikipedia.org/wiki/Measure_(mathematics)?oldformat=true
    keywords = ReferenceProducerProxy.get_keywords(
        "In mathematics, the concept of a measure is a generalization "
        "and formalization of geometrical measures (distance/length, area, "
        "volume) and other common notions, such as mass and probability "
        "of events."
    )

    assert "a measure" in keywords
    assert "probability" in keywords
    assert "formalization" in keywords
    assert "distance/length" in keywords
    assert "volume" in keywords
    assert "geometrical measures" in keywords
    assert "mass" in keywords
