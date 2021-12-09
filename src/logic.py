import os
import re

__regex = None
__replacement = None


def __findrep(filename, backup_path):
    try:
        with open(filename, "r") as file:
            content = file.read()
    except:
        return

    new_content, nchanges = re.subn(__regex, __replacement, content)
    if nchanges == 0:
        return

    os.makedirs(backup_path, exist_ok=True)
    os.rename(filename, os.path.join(backup_path, os.path.basename(filename)))
    with open(filename, "w") as file:
        file.write(new_content)


def findrep_files(filenames, regex, replacement):
    if regex == "":
        raise Exception("regex (find) is required")

    global __regex
    global __replacement

    __regex = regex
    __replacement = replacement

    for filename in filenames:
        backup_path = os.path.join(
            os.path.dirname(filename), "original_files"
        )

        __findrep(filename, backup_path)


def __process__directory(input_path, backup_path):
    with os.scandir(input_path) as entries:
        for entry in entries:
            if entry.is_dir():
                __process__directory(
                    f"{input_path}/{entry.name}",
                    f"{backup_path}/{entry.name}"
                )
            else:
                __findrep(f"{input_path}/{entry.name}", backup_path)


def findrep_directory(directory, regex, replacement):
    if regex == "":
        raise Exception("regex (find) is required")

    global __regex
    global __replacement

    __regex = regex
    __replacement = replacement

    backup_path = os.path.join(
        os.path.dirname(directory),
        f"{os.path.basename(directory)}_original"
    )

    __process__directory(directory, backup_path)
