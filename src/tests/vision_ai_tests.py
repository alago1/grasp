from PIL import Image

from text_detection import detect_text

# test handwritting detection
assert (
    detect_text(Image.open("src/tests/data/helloworld.jpg")).strip().lower()
    == "hello world!"
)

# ADD: Test case for typed presentation image
# print(detect_text("src/tests/dataprobability.1130400.jpg"))
# # ADD: Test case for handwritten presentation image
# print(detect_text("src/tests/data/handwritten1.png"))
# # ADD: Test case for image with no text
# print(detect_text("src/tests/data/____"))  # ADD

# test lower resolution images
assert (
    "example of use case diagram"
    in detect_text("src/tests/data/lowres_diagram.png").lower()
)
# # ADD: Test case for svg
# print(detect_text("src/tests/data/___"))  # ADD
# # ADD: Test case for logos and watermarks
# print(detect_text("src/tests/data/____"))  # ADD
