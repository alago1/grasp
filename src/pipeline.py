import io
from os import path
from typing import List, Optional, Tuple

from pptx import Presentation
from pptx.util import Inches

from buffer import get_frame_data
from reference_producer import get_references
from text_detection import detect_text


def process_references(
    filepath: str, slides_path: Optional[str] = None
) -> List[Tuple[int, List[Tuple[str, str]]]]:
    """
    Given filepath to video file, process entire
    pipeline and returns list of timestamped pairs
    of noun-chunks, references.
    """

    prs = Presentation()
    blank_slide = prs.slide_layouts[6]
    references: List[Tuple[int, List[Tuple[str, str]]]] = []

    img_buffer = get_frame_data(filepath)
    for timestamp, img in img_buffer:
        print(f"CURRENT TIMESTAMP: {timestamp}")

        text = detect_text(img)
        refs = get_references(text)
        references.append((timestamp, refs))

        slide = prs.slides.add_slide(blank_slide)
        with io.BytesIO() as output:
            img.save(output, format="GIF")
            slide.shapes.add_picture(
                output, Inches(0), Inches(0), width=prs.slide_width
            )
            slide.notes_slide.notes_text_frame.text = "\n".join(
                [f'"{kw}": {ref}' for kw, ref in refs]
            )

    split_path = path.split(filepath)
    filename = split_path[-1].split(".")[0]
    if slides_path is None:
        slides_path = path.join(*split_path[:-1], f"slides_{filename}.pptx")
    else:
        slides_path = path.join(slides_path, f"slides_{filename}.pptx")

    prs.save(slides_path)

    return references
