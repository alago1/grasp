from functools import lru_cache
from typing import List, Optional, Tuple, cast

import spacy
import wikipedia
from wikipedia import DisambiguationError, PageError

NLP_MODEL = spacy.load("en_core_web_sm")


@lru_cache(maxsize=1024)
def get_single_reference(key: str) -> Optional[str]:
    """
    Given a key to search for, returns reference url and caches result.
    """

    if len(key) <= 3 or not all(x.isalnum() or x == "" for x in key.split()):
        return None

    try:
        query = wikipedia.page(key)
        print(f'Added "{key}": {query.url}')
        return cast(str, query.url)
    except DisambiguationError:
        print(f'Ignoring "{key}" (Ambiguous)')
    except PageError:
        print(f'Ignoring "{key}" (No match)')
    except KeyError:
        pass

    return None


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
    urls = set()
    for chunk in doc.noun_chunks:
        if chunk.text in noun_chunks:
            continue

        noun_chunks.add(chunk.text)
        url = get_single_reference(chunk.text)

        if url is None or url in urls:
            continue

        urls.add(url)
        references.append((chunk.text, url))

    return references
