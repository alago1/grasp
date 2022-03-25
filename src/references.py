from typing import List, Tuple

import spacy
import wikipedia

NLP_MODEL = spacy.load("en_core_web_sm")


def get_references(text: str) -> List[Tuple[str, str]]:
    """
    Given sanitized text captured from a frame,
    returns a list of pairs of text chunks with their respective
    reference urls.
    """

    # document of processed text
    doc = NLP_MODEL(text)

    references: List[Tuple[str, str]] = []
    for chunk in set(doc.noun_chunks):
        query = wikipedia.page(chunk.text)
        references.append((chunk.text, query.url))

    return references
