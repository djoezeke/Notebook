"""Functions"""

import json
import os
from pathlib import Path

from PIL import Image
from PIL import ImageTk

ROOT = Path(__file__).resolve().parent.parent.parent / "resources"

#################################### UTILS #######################################


def get_img(file, size=(24, 24)):
    """get_img image"""

    icons = os.path.join(ROOT, "icons")
    image_ = Image.open(os.path.join(icons, file)).resize(size)
    image_ = ImageTk.PhotoImage(image_)
    return image_


def read_json(file: str):
    """JSON"""

    result = {}
    try:
        with open(file, encoding="utf-8") as f:
            try:
                result = json.load(f)
            except json.JSONDecodeError:
                pass
    except FileNotFoundError:
        pass

    return result


def write_json(file: str, data: dict):
    """JSON"""

    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f)


def read_file(file: str):
    """JSON"""

    result = ""
    try:
        with open(file, encoding="utf-8") as f:
            result = f.read()
    except FileNotFoundError:
        pass

    return result


def write_file(file: str, data: str):
    """JSON"""

    with open(file, "w", encoding="utf-8") as f:
        f.write(data)


#################################### FILE #######################################


def new_file():
    """..."""


def open_file():
    """..."""


def save_file():
    """..."""


def save_file_as():
    """..."""


def open_recent():
    """..."""


def save_all_file():
    """..."""


def share_file():
    """..."""


def auto_save():
    """..."""


def preferences():
    """..."""


def close_tab():
    """..."""


def close_editor():
    """..."""


def close_window():
    """..."""


def exit():
    """..."""


#################################### VIEW #######################################


def zoom_in():
    """..."""


def zoom_out():
    """..."""


def zoom_reset():
    """..."""


def word_wrap():
    """..."""


def toggle_status():
    """..."""


def toggle_primary():
    """..."""
