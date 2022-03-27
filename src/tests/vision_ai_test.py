from PIL import Image

from text_detection import detect_text

# will fail
assert detect_text(Image.open("src/tests/data/probability.1130400.jpg")) == ""


# ADD: Test case for typed presentation image

# ADD: Test case for handwritten presentation image

# ADD: Test case for image with no text

# ADD: Test case for diagrams

# ADD: Test case for png

# ADD: Test case for jpg

# ADD: Test case for svg

# ADD: Test case for logos and watermarks
