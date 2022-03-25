import tkinter as tk
from tkinter import SE, Canvas
from tkinter import filedialog as fd
from tkinter import ttk
from typing import Optional, Tuple

from PIL import ImageTk

from util import produce_video_preview

# pylint: disable=missing-function-docstring

# FIXME: Put this inside a class for the preview object

PREVIEW_CANVAS: Optional[Canvas] = None
VIDEO_PREVIEW: Optional[Tuple[ImageTk.PhotoImage, ...]] = None
PREVIEW_STATE: str = "success"
PREVIEW_FRAME: int = -1
PREVIEW_CONTAINER: int = -1


def update_preview_frame(root: tk.Tk) -> None:
    global PREVIEW_FRAME

    if VIDEO_PREVIEW is None or PREVIEW_CANVAS is None:
        return

    PREVIEW_FRAME = (PREVIEW_FRAME + 1) % len(VIDEO_PREVIEW)

    PREVIEW_CANVAS.itemconfig(PREVIEW_CONTAINER, image=VIDEO_PREVIEW[PREVIEW_FRAME])

    print(f"new frame: {PREVIEW_FRAME}")

    if PREVIEW_STATE == "success":
        root.after(100, update_preview_frame, root)


def select_file(root: tk.Tk) -> None:
    global VIDEO_PREVIEW, PREVIEW_STATE, PREVIEW_FRAME, PREVIEW_CONTAINER
    filetypes = (("MP4 files", "*.mp4"), ("All files", "*.*"))

    filepath = fd.askopenfilename(
        title="Open file",
        # TODO: Change this to a better root directory
        initialdir="~/Documents/uf/cen3032/imgBuffer/data",
        filetypes=filetypes,
    )

    print(filepath)

    preview = produce_video_preview(filepath)
    if preview is None:
        PREVIEW_STATE = "failed"
        return

    PREVIEW_STATE = "success"
    VIDEO_PREVIEW = tuple(ImageTk.PhotoImage(p) for p in preview)

    if PREVIEW_CANVAS is not None and PREVIEW_FRAME == -1 and VIDEO_PREVIEW is not None:
        PREVIEW_FRAME = 0

        PREVIEW_CONTAINER = PREVIEW_CANVAS.create_image(
            300, 300, anchor=SE, image=VIDEO_PREVIEW[PREVIEW_FRAME]
        )
        root.after(100, update_preview_frame, root)


def main(root: tk.Tk) -> None:
    global PREVIEW_CANVAS

    root.title("My window")
    root.minsize(width=500, height=500)

    open_button = ttk.Button(
        root, text="Select video file", command=lambda: select_file(root)
    )
    open_button.pack(expand=True)

    PREVIEW_CANVAS = Canvas(root, width=300, height=300)
    PREVIEW_CANVAS.pack()

    # FIXME: Label isn't reactive
    if PREVIEW_STATE != "idle":
        preview_label = ttk.Label(root, text=PREVIEW_STATE)
        preview_label.pack()


if __name__ == "__main__":
    window = tk.Tk()
    main(window)
    window.mainloop()
