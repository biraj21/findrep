import tkinter as tk


class FindRepGUI:
    def __init__(self, width, height, font, bg, fg):
        self.__bg = bg
        self.__fg = fg
        self.__font = font

        self.window = tk.Tk()
        self.window.configure(bg=bg)
        self.window.geometry(f"{width}x{height}")

    def new_button(self, master, text, width=None, bg=None, fg=None, command=None):
        btn = tk.Button(
            master, text=text, bd=0, font=self.__font,
            highlightthickness=0, command=command
        )

        if width != None:
            btn.configure(width=width)

        if bg != None:
            btn.configure(bg=bg)

        if fg != None:
            btn.configure(fg=fg)

        return btn

    def new_entry(self, master, width=None):
        entry = tk.Entry(master, bd=0, font=self.__font)

        if width != None:
            entry.configure(width=width)

        return entry

    def new_label(self, master, text, bg=None, fg=None, **kwargs):
        if bg == None:
            bg = self.__bg

        if fg == None:
            fg = self.__fg

        return tk.Label(master, text=text, bg=bg, fg=fg, font=self.__font, **kwargs)

    def new_text(self, master, width=None, height=None):
        text = tk.Text(master, bd=0, font=self.__font)

        if width != None:
            text.configure(width=width)

        if height != None:
            text.configure(height=height)

        return text
