import tkinter.filedialog as filedialog
import logic

filenames = ()
dirname = ""


def get_filenames(label):
    global filenames
    global dirname

    filenames = filedialog.askopenfilenames(title="Choose Files")
    nfiles = len(filenames)
    if nfiles != 0:
        dirname = ""
        label.configure(
            text=f"{nfiles} file{'s' if nfiles > 1 else ''} selected"
        )


def get_dirname(label):
    global filenames
    global dirname

    dirname = filedialog.askdirectory(mustexist=1)
    if dirname != "":
        filenames = ()
        label.configure(text="1 folder selected")


def findrep(regex, replacement, label):
    try:
        if len(filenames) > 0:
            logic.findrep_files(filenames, regex, replacement)
        elif dirname != "":
            logic.findrep_directory(dirname, regex, replacement)
        else:
            raise Exception("no files or folder selected")

        label.configure(text="findREp successful",  bg="#4f4", fg="#000")
    except Exception as err_msg:
        label.configure(text=f"Error: {str(err_msg)}", bg="#f44", fg="#fff")
