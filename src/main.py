import threading
import tkinter as tk
from tkinter import NE, Canvas, Label, OptionMenu, StringVar
from tkinter import filedialog as fd
from tkinter import ttk

from PIL import Image, ImageTk

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

    print(filepath, len(filepath))

    if len(filepath) < 1:
        return None

    result = PREVIEW_PLAYER.load_new_preview(filepath)

    if result == 0:
        root.after(100, update_preview_frame, root)
    return None


def main(root: tk.Tk) -> None:
    root.title("Grasp")
    root.minsize(width=500, height=500)

    PREVIEW_PLAYER.root = root

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

    output_folder_button = ttk.Button(
        root, text="Select output folder", command=lambda: "DO NOTHING"
    )
    output_folder_button.pack(expand=True)

    output_folder_label = Label(root, text=f"Selected folder: {None}")
    output_folder_label.pack(expand=True)

    output_type = StringVar(root)
    output_type.set("TXT")

    output_type_dropdown = OptionMenu(root, output_type, "TXT", "PDF")
    output_type_dropdown.pack(expand=True)

    process_button = ttk.Button(
        root, text="Find references", command=lambda: "DO NOTHING"
    )
    process_button.pack(expand=True)


if __name__ == "__main__":
    window = tk.Tk()
    main(window)
    window.mainloop()
