from typing import List, Tuple

from buffer import get_frame_data
from reference_producer import get_references
from text_detection import detect_text


# NOTE: To implement process of writing out to file
def process_references(filepath: str) -> List[Tuple[int, List[Tuple[str, str]]]]:
    """
    Given filepath to video file, process entire
    pipeline and returns list of timestamped pairs
    of noun-chunks, references.
    """
    references: List[Tuple[int, List[Tuple[str, str]]]] = []

    img_buffer = get_frame_data(filepath)
    for timestamp, img in img_buffer:
        print(f"CURRENT TIMESTAMP: {timestamp}")
        text = detect_text(img)
        refs = get_references(text)
        references.append((timestamp, refs))
    return references
