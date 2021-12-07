import os


def make_dir(path):
    base_path = "."
    parts = path.split("/")

    if path.startswith("./"):
        parts.pop(0)
    elif path.startswith("/"):
        parts.pop(0)
        base_path = ""

    for part in parts:
        base_path += f"/{part}"
        if not os.path.exists(base_path):
            os.mkdir(base_path)
