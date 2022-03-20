import operator
from functools import reduce
from typing import Iterator, cast

import av
import numpy as np
from PIL import Image


def get_frame_data(path: str) -> Iterator[Image.Image]:
    """
    Returns iterator of relevant frames (Pillow Image)
    given a path to a mp4
    """





    # FIXME: Assert that path is valid

    with av.open(path) as container:
        stream = container.streams.video[0]
        stream.codec_context.skip_frame = "NONKEY"

        last_keyframe = None
        last_pts = 0

        for frame in container.decode(stream):
            array = frame.to_ndarray(format="rgb24")

            if last_keyframe is None:
                last_keyframe = array

            # skip if less than 10 seconds elapsed
            if frame.pts - last_pts // 30000 < 10:
                continue

            diff = abs(last_keyframe - array)
            diff_rate = np.count_nonzero(diff) / reduce(operator.mul, diff.shape)

            # skip if less than 10% of frame changed since last key
            if diff_rate <= 0.1:
                continue

            last_keyframe = array
            last_pts = frame.pts

            yield cast(Image.Image, last_keyframe.to_image())
