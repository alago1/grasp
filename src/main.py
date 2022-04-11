import threading
import tkinter as tk
from tkinter import Canvas
from tkinter import filedialog as fd
from tkinter import ttk

from util import PreviewInstance

# pylint: disable=missing-function-docstring


PREVIEW_PLAYER = PreviewInstance()


def update_preview_frame(root: tk.Tk) -> None:

    next_frame = PREVIEW_PLAYER.next_frame()

    if next_frame >= 0:
        root.after(100, update_preview_frame, root)


def select_file(root: tk.Tk) -> None:
    filetypes = (("MP4 files", "*.mp4"), ("All files", "*.*"))

    filepath = fd.askopenfilename(
        title="Open file",
        # TODO: Change this to a better root directory
        initialdir="~/Documents/uf/cen3032/imgBuffer/data",
        filetypes=filetypes,
    )

    print(filepath)

    result = PREVIEW_PLAYER.load_new_preview(filepath)

    if result == 0:
        root.after(100, update_preview_frame, root)


def main(root: tk.Tk) -> None:
    root.title("My window")
    root.minsize(width=500, height=500)

    open_button = ttk.Button(
        root,
        text="Select video file",
        command=lambda: threading.Thread(target=lambda: select_file(root)).start(),
    )
    open_button.pack(expand=True)

    PREVIEW_PLAYER.canvas = Canvas(root, width=300, height=300)
    PREVIEW_PLAYER.canvas.pack()

    # FIXME: Label isn't reactive
    if PREVIEW_PLAYER.state != "success":
        preview_label = ttk.Label(root, text=PREVIEW_PLAYER.state)
        preview_label.pack()


if __name__ == "__main__":
    window = tk.Tk()
    main(window)
    window.mainloop()
