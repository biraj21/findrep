import tkinter as tk
from gui import *
from handlers import *

GUI.new_label("Select:").pack(anchor=tk.W, padx=20, pady=(10, 6))

sframe = tk.Frame(GUI.window, width=300, height=28, bd=0, bg="#111")
sframe.pack_propagate(0)
sframe.pack()

GUI.new_button(
    "Files", master=sframe, width=11, command=lambda: get_filenames(slabel)
).pack(side=tk.LEFT)

GUI.new_button(
    "Folder", height=2, master=sframe, width=11,
    command=lambda: get_dirname(slabel)
).pack(side=tk.RIGHT)

slabel = GUI.new_label("No files or folder selected")
slabel.pack(pady=(10, 0))

GUI.new_label("Find (RegEx):").pack(anchor=tk.W, padx=20, pady=(10, 6))

find_field = GUI.new_entry(width=30)
find_field.pack(padx=20, ipady=2)

GUI.new_label("Replace with:").pack(anchor=tk.W, padx=20, pady=(10, 6))

replace_field = GUI.new_text(width=30, height=5)
replace_field.pack(padx=20)

GUI.new_button(
    "Find & Replace", bg="#7b19fa", fg="#fff",
    command=lambda: findrep(
        find_field.get(), replace_field.get("1.0", "end-1c"), info_label
    )
).pack(side=tk.BOTTOM, pady=(10, 20), ipadx=5)

info_label = GUI.new_label(
    "Note: non-text files will be skipped", wraplength=300
)
info_label.pack(side=tk.BOTTOM, ipadx=5)

GUI.window.mainloop()
