from dataclasses import dataclass
from math import floor
from os import path
from tkinter import Canvas, Label, Tk
from typing import List, Optional, Tuple

import av
from PIL import Image, ImageTk


def produce_video_preview(filepath: str) -> Optional[List[Image.Image]]:
    """
    Given a path string, returns a list of PIL Images with
    up to first 50 frames of the video as a preview.

    If the file is not accessible, is a directory, or the file
    data is not encoded properly, returns None.
    """

    try:
        with av.open(filepath) as container:
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


@dataclass
class PreviewInstance:
    """
    Dataclass for abstracting GUI Preview data
    """

    root: Optional[Tk] = None
    title: Optional[Label] = None
    canvas: Optional[Canvas] = None
    preview: Optional[Tuple[ImageTk.PhotoImage, ...]] = None
    curr_frame: int = -1
    container_id: int = -1

    def next_frame(self) -> int:
        """
        Sets preview frame to following frame if the video has been loaded.
        If no video has been loaded or the canvas is None, returns -1.
        Otherwise, returns index of new frame.
        """

        if self.preview is None or self.canvas is None:
            return -1

        self.curr_frame = (self.curr_frame + 1) % len(self.preview)
        self.canvas.itemconfig(self.container_id, image=self.preview[self.curr_frame])

        return self.curr_frame

    def load_new_preview(self, filepath: str) -> int:
        """
        Given a filepath to a video file, produces video preview and displays on GUI.
        If the filepath is not valid or no canvas has been created, returns -1.
        """

        if self.canvas is None or self.title is None:
            return -1

        prev = produce_video_preview(filepath)

        if prev is None:
            return -1

        filename = path.split(filepath)[-1]
        self.title.config(text=f"Previewing: {filename}")

        width, height = self.canvas.winfo_width(), self.canvas.winfo_height()

        scale = 15
        self.preview = tuple(
            ImageTk.PhotoImage(p.resize((16 * scale, 9 * scale))) for p in prev
        )
        self.curr_frame = 0

        self.container_id = self.canvas.create_image(
            width // 2,
            height // 2,
            image=self.preview[self.curr_frame],
            anchor="center",
        )

        return 0
