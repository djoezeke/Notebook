"""Functions"""

import os
import json
from PIL import Image, ImageTk
from tksvg import SvgImage

ROOT = os.path.dirname(os.path.realpath(__file__))

#################################### UTILS #######################################


def get_img(file, size=(24, 24)):
    """get_img image"""

    icons = os.path.join(ROOT, "icons")
    image_ = Image.open(os.path.join(icons, file)).resize(size)
    image_ = ImageTk.PhotoImage(image_)
    return image_


def get_svg(file, height=20, width=25):
    """get_svg image"""

    svg = os.path.join(ROOT, "svgs")
    image_ = SvgImage(
        format="svg", file=f"{os.path.join(svg, file)}", height=height, width=width
    )
    return image_


def read_json(file: str):
    """JSON"""

    result = {}
    try:
        with open(file, "r", encoding="utf-8") as f:
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
        with open(file, "r", encoding="utf-8") as f:
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
