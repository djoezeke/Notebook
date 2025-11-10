"""Notepad"""

import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askokcancel

import ttkbootstrap as tb
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip

import notebook.utils.functions as fun

ROOT = os.path.dirname(os.path.realpath(__file__))


#################################### NAVIGATION #######################################


class Navigation(tb.Frame):
    """Menu"""

    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="ew")

        self.main_menu = tb.Menu(self, type="tearoff")

        self.selection_btn = tb.Menu(self.main_menu, tearoff=0)

        self.file_btn = tb.Menu(self.main_menu, tearoff=0)
        self.preferences = tb.Menu(self.file_btn, tearoff=0)
        self.recents = tb.Menu(self.file_btn, tearoff=0)

        self.edit_btn = tb.Menu(self.main_menu, tearoff=0)
        self.copy_as = tb.Menu(self.edit_btn, tearoff=0)

        self.view_btn = tb.Menu(self.main_menu, tearoff=0)
        self.zoom = tb.Menu(self.view_btn, tearoff=0)

        self.help_btn = tb.Menu(self.main_menu, tearoff=0)

        self.create_main_menu()

        self.popup_menu = tb.Menu(self, tearoff=0)
        self.create_popup_menu()

        self.bind("<Button-3>", self.pop_up)

    def create_main_menu(self):
        """popup"""

        self.create_file_nav()
        self.create_edit_nav()
        self.create_selection_nav()
        self.create_view_nav()
        self.create_help_nav()

        self.main_menu.add_cascade(label="File", menu=self.file_btn)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_btn)
        self.main_menu.add_cascade(label="Selection", menu=self.selection_btn)
        self.main_menu.add_cascade(label="View", menu=self.view_btn)
        self.main_menu.add_cascade(label="Help", menu=self.help_btn)

    def pop_up(self, event):
        """popup"""

        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.popup_menu.grab_release()

    def create_popup_menu(self):
        """popup"""

        self.popup_menu.add_command(label="Navigation")
        self.popup_menu.add_command(label="Copy")
        self.popup_menu.add_command(label="Paste")
        self.popup_menu.add_command(label="Reload")
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Rename")

    def create_file_nav(self):
        """frame"""

        self.file_btn.add_command(label="New File", accelerator="Ctrl+N")
        self.file_btn.add_separator()
        self.file_btn.add_command(label="Open File", accelerator="Ctrl+O")
        self.file_btn.add_command(label="Open Recent", accelerator="Ctrl+S")
        self.file_btn.add_separator()
        self.file_btn.add_command(label="Save", accelerator="Ctrl+S")
        self.file_btn.add_command(label="Save As", accelerator="Ctrl+Shift+S")
        self.file_btn.add_command(label="Save All", accelerator="Ctrl+Alt+S")
        self.file_btn.add_separator()
        self.file_btn.add_command(label="Share")
        self.file_btn.add_separator()
        self.file_btn.add_checkbutton(label="Auto Save")
        self.file_btn.add_cascade(label="Preferences")
        self.file_btn.add_separator()
        self.file_btn.add_command(label="Close Tab", accelerator="Ctrl+W")
        self.file_btn.add_command(label="Close Editor", accelerator="Ctrl+F4")
        self.file_btn.add_command(label="Close Window", accelerator="Alt+F4")
        self.file_btn.add_separator()
        self.file_btn.add_command(label="Exit")

    def create_edit_nav(self):
        """frame"""

        self.copy_as.add_command(label="Copy Remote File URL")
        self.copy_as.add_command(label="Copy Remote File URL From...")

        self.edit_btn.add_command(label="Undo", accelerator="Ctrl+Z")
        self.edit_btn.add_command(label="Redo", accelerator="Ctrl+Y")
        self.edit_btn.add_separator()
        self.edit_btn.add_command(label="Cut", accelerator="Ctrl+X")
        self.edit_btn.add_command(label="Copy", accelerator="Ctrl+C")
        self.edit_btn.add_cascade(label="Copy As", menu=self.copy_as)
        self.edit_btn.add_command(label="Paste", accelerator="Ctrl+V")
        self.edit_btn.add_separator()
        self.edit_btn.add_command(label="Delete", accelerator="Del")
        self.edit_btn.add_separator()
        self.edit_btn.add_command(label="Find", accelerator="Ctrl+F")
        self.edit_btn.add_command(label="Find Next", accelerator="F3")
        self.edit_btn.add_command(label="Find Previous", accelerator="Shift+F3")
        self.edit_btn.add_command(label="Replace", accelerator="Ctrl+H")
        self.edit_btn.add_command(label="Goto", accelerator="Ctrl+G")
        self.edit_btn.add_separator()
        self.edit_btn.add_command(label="Find in Files", accelerator="Ctrl+Shift+F")
        self.edit_btn.add_command(label="Replace in Files", accelerator="Ctrl+Shift+H")
        self.edit_btn.add_separator()
        self.edit_btn.add_command(label="View", accelerator="Ctrl+Shift+/")

    def create_selection_nav(self):
        """popup"""

        self.selection_btn.add_command(label="Select All", accelerator="Ctrl+A")
        self.selection_btn.add_command(label="Expand Selection", accelerator="Shift+Alt+RightArrow")
        self.selection_btn.add_command(label="Shrink Selection", accelerator="Shift+Alt+LeftArrow")
        self.selection_btn.add_separator()
        self.selection_btn.add_command(label="Copy Line Up", accelerator="Shift+Alt+UpArrow")
        self.selection_btn.add_command(label="Copy Line Down", accelerator="Shift+Alt+DownArrow")
        self.selection_btn.add_command(label="Move Line Up", accelerator="Alt+UpArrow")
        self.selection_btn.add_command(label="Move Line Down", accelerator="Alt+DownArrow")
        self.selection_btn.add_command(label="Duplicate Selection")
        self.selection_btn.add_separator()
        self.selection_btn.add_command(label="Add Cursor Above", accelerator="Ctrl+Alt+UpArrow")
        self.selection_btn.add_command(label="Add Cursor Below", accelerator="Ctrl+Alt+DownArrow")
        self.selection_btn.add_command(label="Add Cursor To Line Ends", accelerator="Shift+Alt+I")
        self.selection_btn.add_command(label="Add Next Occurrence", accelerator="Ctrl+D")
        self.selection_btn.add_command(label="Add Previous Occurrence")
        self.selection_btn.add_command(label="Select All Occurrence", accelerator="Ctrl+Shift+L")
        self.selection_btn.add_separator()
        self.selection_btn.add_command(label="Switch to Click+Click for Multi-Cursor")
        self.selection_btn.add_command(label="Column Selection Mode")

    def create_view_nav(self):
        """frame"""

        self.zoom.add_command(label="Zoom In", accelerator="Ctrl+Plus")
        self.zoom.add_command(label="Zoom Out", accelerator="Ctrl+Minus")
        self.zoom.add_command(label="Restore Default Zoom", accelerator="Ctrl+0")

        self.view_btn.add_cascade(label="Zoom", menu=self.zoom)
        self.view_btn.add_checkbutton(label="Word Wrap", accelerator="Alt+Z")
        self.view_btn.add_separator()
        self.view_btn.add_command(label="Status Bar", accelerator="Ctrl+J")
        self.view_btn.add_command(label="Primary Bar", accelerator="Ctrl+B")

    def create_help_nav(self):
        """popup"""

        self.help_btn.add_command(label="Welcome")
        self.help_btn.add_command(label="Show All Commands")
        self.help_btn.add_command(label="Documentation")
        self.help_btn.add_separator()
        self.help_btn.add_command(label="Tips & Tricks")
        self.help_btn.add_command(label="Report Issues")
        self.help_btn.add_separator()
        self.help_btn.add_command(label="View License")
        self.help_btn.add_command(label="Privacy Statement")
        self.help_btn.add_separator()
        self.help_btn.add_command(label="Check for Update")
        self.help_btn.add_separator()
        self.help_btn.add_command(label="About")


#################################### STATUS #######################################


class Status(tb.Frame):
    """MenuBar"""

    def __init__(self, master):
        super().__init__(master, height=20)

        self.popup_menu = tb.Menu(self, tearoff=0)
        self.create_popup_menu()

        self.bind("<Button-3>", self.pop_up)

        self.icons = {
            "search": fun.get_img("add_outline.png"),
            "manage": fun.get_img("settings_filled.png"),
            "account": fun.get_img("add_outline.png"),
        }

        self.search_btn = tb.Button(
            self,
            text="Search",
            cursor="hand2",
            image=self.icons["search"],
            compound="image",
            style="light",
            # command=self.search,
        )
        self.search_btn.pack(side="left")
        Tooltip(self.search_btn, text="Search")
        self.search_btn.bind("<Enter>", lambda x: self.on_enter(x, self.search_btn))
        self.search_btn.bind("<Leave>", lambda x: self.on_leave(x, self.search_btn))

        self.manage_btn = tb.Button(
            self,
            text="Manage",
            cursor="hand2",
            image=self.icons["manage"],
            compound="image",
            style="light",
            command=self.manage,
        )
        self.manage_btn.pack(side="left")
        Tooltip(self.manage_btn, text="Manage")
        self.manage_btn.bind("<Enter>", lambda x: self.on_enter(x, self.manage_btn))
        self.manage_btn.bind("<Leave>", lambda x: self.on_leave(x, self.manage_btn))

        self.account_btn = tb.Button(
            self,
            text="Account",
            cursor="hand2",
            image=self.icons["account"],
            compound="image",
            style="light",
            command=self.account,
        )
        self.account_btn.pack(side="left")
        Tooltip(self.account_btn, text="Account")
        self.account_btn.bind("<Enter>", lambda x: self.on_enter(x, self.account_btn))
        self.account_btn.bind("<Leave>", lambda x: self.on_leave(x, self.account_btn))

    def show_menu(self, menu: tb.Menu, x=20, y=100):
        """popup"""

        try:
            menu.tk_popup(x, y)
            menu.pack()
        finally:
            menu.grab_release()

    def on_enter(self, e=None, button=None):
        """On Enter"""

        button["compound"] = "text"

    def on_leave(self, e=None, button=None):
        """On Leave"""

        button["compound"] = "image"

    def pop_up(self, event):
        """popup"""

        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.popup_menu.grab_release()

    def create_popup_menu(self):
        """popup"""

        self.popup_menu.add_checkbutton(label="Explorer")
        self.popup_menu.add_checkbutton(label="Search")
        self.popup_menu.add_checkbutton(label="Debug")
        self.popup_menu.add_checkbutton(label="Extention")
        self.popup_menu.add_checkbutton(label="Manage")
        self.popup_menu.add_separator()
        self.popup_menu.add_checkbutton(label="Account")
        self.popup_menu.add_separator()

    def account(self):
        """account"""

    def manage(self):
        """manage"""


#################################### NOTE UI #######################################


class Tooltip(ToolTip):
    """Notebook"""

    def __init__(self, master, text):
        super().__init__(
            master,
            text=text,
            delay=500,
            width=200,
            height=50,
            wraplength=100,
        )


class NutNotify(ToastNotification):
    """Notebook"""

    def __init__(self, title, message):
        super().__init__(
            title=title,
            message=message,
            # icon=None,
            # iconfont=None,
            bootstyle="dark",
            # duration=3000,
            # alert=True,
            # position=(30, 30, "sw"),
        )

    def show(self):
        """show"""
        self.show_toast()


#################################### TEXT/NOTE #######################################


class TextFrame(tb.Frame):
    """Notebook"""

    def __init__(self, master):
        super().__init__(master)

        self.file_path = ""
        self.file_name = "Untitled"
        self.file_ext = ""

        self.pack(expand=1, fill="both")

        self.popup_menu = tb.Menu(self, tearoff=0)
        self.create_popup_menu()

        self.scrollbar_x = tb.Scrollbar(self, orient="horizontal", bootstyle="light")
        self.scrollbar_x.pack(side="bottom", fill="x")

        self.scrollbar_y = tb.Scrollbar(self, orient="vertical", bootstyle="light")
        self.scrollbar_y.pack(side="right", fill="y")

        self.text_edit = tb.Text(
            self,
            font="Helvetica 10",
            yscrollcommand=self.scrollbar_y.set,
            xscrollcommand=self.scrollbar_x.set,
            wrap="none",
            undo=True,
            padx=0,
            pady=0,
        )

        self.text_edit.pack(side="left", expand=1, fill="both")
        self.text_edit.bind("<Button-3>", self.pop_up)
        self.text_edit.focus()

        # configuring a tag called start
        self.text_edit.tag_config("start", background="black", foreground="red")

        # Scroll Config
        self.scrollbar_y.config(command=self.text_edit.yview)
        self.scrollbar_x.config(command=self.text_edit.xview)

    def pop_up(self, event):
        """popup"""

        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.popup_menu.grab_release()

    def create_popup_menu(self):
        """popup"""

        self.popup_menu.add_command(label="Cut")
        self.popup_menu.add_command(label="Copy")
        self.popup_menu.add_command(label="Paste")
        self.popup_menu.add_command(label="Reload")
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Rename")

    def get_edit(self):
        """get_edit"""

        return self.text_edit

    def set_file(self, file_path: str):
        """get_edit"""

        self.file_path = file_path

        name_index = file_path.rfind("/")
        ext_index = file_path.rfind(".")

        if name_index != -1:
            self.file_name = file_path[name_index + 1 :]

        if ext_index != -1:
            self.file_ext = file_path[ext_index + 1 :]

    def get_file(self):
        """get_edit"""

        return self.file_path


#################################### APPLICATION #######################################


class Notebook(tb.Notebook):
    """Notebook"""

    def __init__(self, master):
        super().__init__(master, height=10000)

        self.count = -1
        self.text_frames: list[TextFrame] = []

        self.icons = {
            "file": fun.get_img("add_outline.png", (10, 10)),
        }

        self.no_note = tb.Frame(self, style="dark", height=10000)

        self.popup_menu = tb.Menu(self, tearoff=0)
        self.create_popup_menu()

        self.bind("<Control-h>", self.pop_up)  # Replace
        self.bind("<Control-f>", self.pop_up)  # Find

        self.bind("<Control-v>", self.pop_up)  # Paste
        self.bind("<Control-c>", self.pop_up)  # Copy
        self.bind("<Control-x>", self.pop_up)  # Cut

        self.bind("<Control-y>", self.pop_up)  # Redo
        self.bind("<Control-z>", self.pop_up)  # Undo

        self.bind("<Button-3>", self.pop_up)  # popup menu

    def create_text_frame(self):
        """frame"""

        self.count = self.count + 1
        text_frame = TextFrame(self)
        self.text_frames.append(text_frame)
        return text_frame

    def update_text_frame(self, index, filepath):
        """frame"""

        self.text_frames[index].set_file(filepath)
        self.add(
            child=self.text_frames[index],
            text=f"{self.text_frames[index].file_name}",
            image=self.icons["file"],
            compound="left",
        )

    def insert_text_frame(self, index):
        """frame"""

        self.insert(
            "end",
            self.text_frames[index],
            text=f"{self.text_frames[index].file_name}",
            image=self.icons["file"],
            compound="left",
        )

    def get_text_frame(self, index):
        """get_text_frame"""

        return self.text_frames[index]

    def pop_up(self, event):
        """popup"""

        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.popup_menu.grab_release()

    def create_popup_menu(self):
        """popup"""

        self.popup_menu.add_command(label="Note")
        self.popup_menu.add_command(label="Copy")
        self.popup_menu.add_command(label="Paste")
        self.popup_menu.add_command(label="Reload")
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Rename")


class Note(tb.Window):
    """Note"""

    open_types: list[tuple[str, str]] = [("All Files", "*")]
    saveas_types: list[tuple[str, str]] = [
        ("All Files", "*"),
        ("No Extention ", "*.*"),
    ]

    def __init__(self):
        super().__init__()

        self.title("Note Book")
        self.geometry("800x500")
        self.style.theme_use("cosmo")

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.status_var = tk.BooleanVar(value=True)

        self.note = fun.read_json("note.json")

        ############################################################

        # navigation frame
        self.navigation_frame = Navigation(self)
        self.configure(menu=self.navigation_frame.main_menu)

        # main frame
        self.note_book = Notebook(self)
        self.note_book.grid(row=1, column=0, sticky="nsew")

        # status frame
        self.status_frame = Status(self)
        self.status_frame.grid(row=2, column=0, sticky="ew")

        #############################################################

        try:
            for file in self.note["opened"]:
                self.open_file(file)
        except KeyError:
            pass

        ##########################################################

        self.bind("<Control-s>", lambda x: self.save_file())
        self.bind("<Control-o>", lambda x: self.ask_open_file())
        self.bind("<Control-Shift-S>", lambda x: self.save_file_as())

        self.bind("<Control-j>", lambda x: self.toggle_status())

        self.wm_protocol("WM_DELETE_WINDOW", self.exit_callback)

    def exit_callback(self):
        """exit_callback"""

        if askokcancel("Close Note", "Do you Really Want to Quit Note?"):
            fun.write_json("note.json", self.note)
            self.destroy()

    def toggle_status(self):
        """toggle_status"""

        if self.status_var.get():
            self.status_frame.grid_forget()
            self.status_var.set(value=False)
        else:
            self.status_frame.grid(row=2, column=0, sticky="ew")
            self.status_var.set(value=True)

    def open_file(self, filepath):
        """Open"""

        if not filepath:
            return

        self.note_book.create_text_frame()

        self.note_book.get_text_frame(self.note_book.count).get_edit().delete(1.0, tk.END)

        content = fun.read_file(filepath)
        self.note_book.get_text_frame(self.note_book.count).get_edit().insert(tk.END, content)

        try:
            if filepath not in self.note["opened"]:
                self.note["opened"].append(filepath)
        except KeyError:
            self.note["opened"] = []
            self.note["opened"].append(filepath)

        self.note_book.get_text_frame(self.note_book.count).set_file(filepath)
        self.note_book.insert_text_frame(self.note_book.count)

    def ask_open_file(self):
        """Open"""

        filepath = askopenfilename(title="Open File", filetypes=Note.open_types, initialdir=".")
        self.open_file(filepath)

    def save_file(self, file_path=None):
        """Open"""

        tab_id = self.note_book.index("current")
        filepath = self.note_book.text_frames[tab_id].get_file()

        if file_path:
            filepath = file_path

        fun.write_file(filepath, self.note_book.text_frames[tab_id].get_edit().get(1.0, tk.END))

        NutNotify("Note", f"File {filepath} saved").show()

    def save_file_as(self):
        """Open"""

        filepath = asksaveasfilename(
            title="Save File As",
            filetypes=Note.saveas_types,
            initialdir=".",
            defaultextension="txt",
        )
        self.save_file(filepath)


if __name__ == "__main__":
    note = Note()
    note.mainloop()

# MIT License

# Copyright (c) 2025 Sackey Ezekiel Etrue

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
