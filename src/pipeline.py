from typing import List, Tuple

from buffer import get_frame_data
from reference_producer import get_references
from text_detection import detect_text


# NOTE: To implement process of writing out to file
def get_full_process(sample_input: str) -> Tuple[int, List[Tuple[str, str]]]:
    """
    Performs the whole pipeline and returns size of the
    frame buffer given a path to a mp4
    """

    img_buffer = get_frame_data(sample_input)
    buffer_size = 0
    for img in img_buffer:
        temp_output = get_references(detect_text(img))
        buffer_size += 1
    return buffer_size, temp_output
