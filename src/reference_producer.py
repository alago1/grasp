from typing import List, Tuple

import spacy
import wikipedia
from wikipedia import DisambiguationError

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
    noun_chunks = set()
    for chunk in doc.noun_chunks:
        if len(chunk.text) <= 3 or chunk.text in noun_chunks:
            continue

        noun_chunks.add(chunk.text)

        try:
            query = wikipedia.page(chunk.text)
            references.append((chunk.text, query.url))
        except DisambiguationError:
            print(f'Ignoring "{chunk}" (Ambiguous)')
        except KeyError:
            pass

    return references
