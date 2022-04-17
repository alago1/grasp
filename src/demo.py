# pylint: disable=invalid-name, unused-import
from PIL import Image

from pipeline import export_txt, process_references
from reference_producer import get_references
from text_detection import detect_text

# text = detect_text(Image.open("src/tests/data/probability.1130400.jpg"))
# print(f"DEMO TEXT DETECTION:\n{text}\n\n")

# refers = get_references(text)
# print(f"DEMO REFERENCES:\n{refers}")

# outputFile = open("output.txt", "w")

# tsrefs = process_references("/home/jesse/EEL4712-01-24.mp4")
# tsrefs = process_references("/home/jesse/EEL4712-01-24.mp4")
# tsrefs = process_references("/home/jesse/testVideo.mp4")
tsrefs = process_references("/home/jesse/TCP_IP.mp4", "", "", True)
export_txt("output.txt", tsrefs)
for tsp, refs in tsrefs:
    print(f"Timestamp: {tsp}")
    print(tsrefs)
    # outputFile.write(f"Timestamp: {tsp}")
    # outputFile.write(f"{tsrefs}")

# outputFile.close()
