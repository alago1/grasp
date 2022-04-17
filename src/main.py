# pylint: disable=missing-function-docstring, global-statement, import-error

import threading
import tkinter as tk
from os import path
from tkinter import NE, Canvas, Label, OptionMenu, StringVar
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
from typing import Optional

from PIL import Image, ImageTk

from pipeline import process_references
from util import PreviewInstance

PREVIEW_PLAYER = PreviewInstance()
OUTPUT_FOLDER_PATH: Optional[str] = None
OUTPUT_FOLDER_LABEL: Optional[StringVar] = None
OUTPUT_FILETYPE: Optional[StringVar] = None
PROCESSING_OUTPUT_LABEL: Optional[StringVar] = None


def update_preview_frame(root: tk.Tk, frame_id: Optional[int] = None) -> None:
    if frame_id is not None and PREVIEW_PLAYER.container_id != frame_id:
        return None

    next_frame = PREVIEW_PLAYER.next_frame()

    if next_frame >= 0:
        root.after(100, update_preview_frame, root, PREVIEW_PLAYER.container_id)


def select_output_folder() -> None:
    global OUTPUT_FOLDER_PATH

    if OUTPUT_FOLDER_LABEL is None:
        return None

    folderpath = fd.askdirectory(title="Select Directory")

    if len(folderpath) < 1:
        return None

    OUTPUT_FOLDER_PATH = folderpath
    folder_name = path.split(folderpath)[-1]
    OUTPUT_FOLDER_LABEL.set(f"Selected folder: {folder_name}")


def select_file(root: tk.Tk) -> None:
    filetypes = (("MP4 files", "*.mp4"), ("All files", "*.*"))

    filepath = fd.askopenfilename(
        title="Open file",
        initialdir="~/Documents/uf/cen3032/imgBuffer/data",
        filetypes=filetypes,
    )

    if len(filepath) < 1:
        return None

    result = PREVIEW_PLAYER.load_new_preview(filepath)

    if result == 0:
        root.after(100, update_preview_frame, root)
    return None


def find_references() -> None:
    if PROCESSING_OUTPUT_LABEL is None or OUTPUT_FILETYPE is None:
        return

    if PREVIEW_PLAYER.video_path is None:
        mb.showerror("No video selected", message="Please select a video.")
        return

    if OUTPUT_FOLDER_PATH is None:
        mb.showerror(
            "No output folder selected", message="Please select an output folder."
        )
        return

    PROCESSING_OUTPUT_LABEL.set("Parsing References...")

    process_references(
        PREVIEW_PLAYER.video_path, OUTPUT_FOLDER_PATH, OUTPUT_FILETYPE.get()
    )

    PROCESSING_OUTPUT_LABEL.set("Successfully exported references")
    mb.showinfo(
        "Export complete", message=f"References exported to {OUTPUT_FOLDER_PATH}"
    )


def main(root: tk.Tk) -> None:
    global OUTPUT_FOLDER_LABEL, OUTPUT_FILETYPE, PROCESSING_OUTPUT_LABEL

    root.title("Grasp")
    root.minsize(width=500, height=500)

    img = ImageTk.PhotoImage(
        Image.open("grasp_logo.png")
        .crop((166, 533, 1833, 1466))
        .resize((100, int(100 / 1.78671)))
    )
    logo = Label(root, image=img, anchor=NE)
    logo.image = img  # type: ignore
    logo.pack(expand=True)

    open_button = ttk.Button(
        root,
        text="Select video file",
        command=lambda: threading.Thread(target=lambda: select_file(root)).start(),
    )
    open_button.pack()

    PREVIEW_PLAYER.title = Label(root)
    PREVIEW_PLAYER.title.pack(expand=True)

    PREVIEW_PLAYER.canvas = Canvas(root, width=320, height=180)
    PREVIEW_PLAYER.canvas.pack(expand=True)

    OUTPUT_FOLDER_LABEL = StringVar(root)
    OUTPUT_FOLDER_LABEL.set("No folder selected")

    output_folder_button = ttk.Button(
        root,
        text="Select output folder",
        command=lambda: threading.Thread(target=select_output_folder).start(),
    )
    output_folder_button.pack(expand=True)

    output_folder_label2 = Label(root, textvariable=OUTPUT_FOLDER_LABEL)
    output_folder_label2.pack(expand=True)

    OUTPUT_FILETYPE = StringVar(root)
    OUTPUT_FILETYPE.set("TXT")

    output_type_dropdown = OptionMenu(root, OUTPUT_FILETYPE, "TXT", "PPTX")
    output_type_dropdown.pack(expand=True)

    process_button = ttk.Button(
        root,
        text="Find references",
        command=lambda: threading.Thread(target=find_references).start(),
    )
    process_button.pack(expand=True)

    PROCESSING_OUTPUT_LABEL = StringVar(root)
    PROCESSING_OUTPUT_LABEL.set("")

    loading_indicator = Label(root, textvariable=PROCESSING_OUTPUT_LABEL)
    loading_indicator.pack(expand=True)


if __name__ == "__main__":
    window = tk.Tk()
    main(window)
    window.mainloop()
