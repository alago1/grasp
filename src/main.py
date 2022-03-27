from PIL import Image

from pipeline import get_full_process
from references import get_references
from text_detection import detect_text

RESULT = get_references(
    detect_text(Image.open("src/tests/data/probability.1130400.jpg"))
)
print(RESULT)

# NOTE: Add more test data to ensure the full pipeline works
get_full_process("sample_video_file_path.mp4")
