from typing import List, Tuple

from buffer import get_frame_data
from reference_producer import get_references
from text_detection import detect_text


# NOTE: To implement process of writing out to file
def process_references(filepath: str) -> List[Tuple[int, List[Tuple[str, str]]]]:
    """
    Performs the whole pipeline and returns size of the
    frame buffer given a path to a mp4
    """
    references: List[Tuple[int, List[Tuple[str, str]]]] = []

    img_buffer = get_frame_data(filepath)
    for timestamp, img in img_buffer:
        text = detect_text(img)
        refs = get_references(text)
        references.append((timestamp, refs))
    return references
