import tkinter as tk


class GUI:
    bg = "#111"
    fg = "#eee"
    font = ("Cooper", 12)
    window = tk.Tk()
    window.geometry("340x420")
    window.resizable(0, 0)
    window.title("findREp")
    window.configure(bg=bg)

    @staticmethod
    def new_button(text, master=None, **config_args):
        if master == None:
            master = GUI.window

        return tk.Button(
            master, text=text, bd=0, font=GUI.font, highlightthickness=0,
            **config_args
        )

    def new_entry(master=None, **config_args):
        if master == None:
            master = GUI.window

        return tk.Entry(master, bd=0, font=GUI.font, **config_args)

    def new_label(text, master=None, **config_args):
        if master == None:
            master = GUI.window

        if "bg" not in config_args:
            config_args["bg"] = GUI.bg

        if "fg" not in config_args:
            config_args["fg"] = GUI.fg

        return tk.Label(master, text=text, font=GUI.font, **config_args)

    def new_text(master=None, **config_args):
        if master == None:
            master = GUI.window

        return tk.Text(master, bd=0, font=GUI.font, **config_args)
