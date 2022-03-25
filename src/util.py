from math import floor
from typing import List, Optional

import av
from PIL import Image


def produce_video_preview(path: str) -> Optional[List[Image.Image]]:
    """
    Given a path string, returns a list of PIL Images with
    up to first 50 frames of the video as a preview.

    If the file is not accessible, is a directory, or the file
    data is not encoded properly, returns None.
    """

    try:
        with av.open(path) as container:
            stream = container.streams.video[0]
            stream.codec_context.skip_frame = "NONKEY"

            frame_count = 0
            np_frames = []
            for frame in container.decode(stream):
                if frame_count > 50:
                    break

                img_frame: Image.Image = frame.to_image()
                scale = 300 / max(img_frame.size)
                new_size = (
                    floor(scale * img_frame.size[0]),
                    floor(scale * img_frame.size[1]),
                )
                np_frames.append(frame.to_image().resize(new_size))
                frame_count += 1

            return np_frames

    except (
        av.InvalidDataError,
        av.FileNotFoundError,
        av.IsADirectoryError,
        av.PermissionError,
    ):
        print("failed to read")
        return None
