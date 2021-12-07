import tkinter as tk
from gui import *
from handlers import *

gui = FindRepGUI(340, 420, ("Arial", 12), bg="#111", fg="#eee")
root = gui.window
root.resizable(0, 0)
root.title("findREp")

# args to be passed to pack() method of title labels
title_pack_args = {
    "anchor": tk.W,
    "padx": 20,
    "pady": (10, 6)
}

gui.new_label(root, "Select:").pack(**title_pack_args)

sframe = tk.Frame(root, width=300, height=27, bd=0, bg="#111")
sframe.pack_propagate(0)
sframe.pack()

slabel = gui.new_label(root, "No files or folder selected")
slabel.pack(pady=(10, 0))

gui.new_button(
    sframe, "Files", width=13,
    command=lambda: get_filenames(slabel)
).pack(side=tk.LEFT)

gui.new_button(
    sframe, "Folder", width=13,
    command=lambda: get_dirname(slabel)
).pack(side=tk.RIGHT)

gui.new_label(root, "Find (RegEx):").pack(**title_pack_args)

find_field = gui.new_entry(root, 33)
find_field.pack(ipady=2)

gui.new_label(root, "Replace With (text):").pack(**title_pack_args)

replace_field = gui.new_text(root, 33, 5)
replace_field.pack()

gui.new_button(
    root, "Find & Replace", bg="#7b19fa", fg="#fff",
    command=lambda: findrep(
        find_field.get(), replace_field.get("1.0", "end-1c"), info_label
    )
).pack(side=tk.BOTTOM, pady=(10, 20), ipadx=5)

info_label = gui.new_label(
    root, text="Note: non-text files will be skipped", wraplength=300
)
info_label.pack(side=tk.BOTTOM, ipadx=5)

root.mainloop()
