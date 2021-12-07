import mimetypes
import os
import re

import utils

OUTPUT_DIR = "findreped"

__regex = None
__replacement = None


def __findrep(ifilename, ofilename):
    filetype = mimetypes.guess_type(ifilename)[0]
    if filetype == None or "text" not in filetype:
        return

    with open(ifilename, "r") as file, open(ofilename, "w") as new_file:
        content = file.read()
        new_file.write(re.sub(__regex, __replacement, content))


def findrep_files(filenames, regex, replacement):
    if regex == "":
        raise Exception("regex is required")

    global __regex
    global __replacement

    __regex = regex
    __replacement = replacement

    for filename in filenames:
        __findrep(filename, f"{OUTPUT_DIR}/{os.path.basename(filename)}")


def __process_recursive(input_path, output_path):
    with os.scandir(input_path) as entries:
        for entry in entries:
            if entry.is_dir():
                __process_recursive(
                    f"{input_path}/{entry.name}",
                    f"{output_path}/{entry.name}",
                )
            else:
                utils.make_dir(output_path)

                __findrep(
                    f"{input_path}/{entry.name}",
                    f"{output_path}/{entry.name}",
                )


def findrep_directory(directory, regex, replacement):
    if regex == "":
        raise Exception("regex is required")

    global __regex
    global __replacement

    __regex = regex
    __replacement = replacement

    __process_recursive(
        directory, f"{OUTPUT_DIR}/{os.path.basename(directory)}"
    )
