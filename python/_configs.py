import os

database = os.path.realpath("../fonts.db")


def file_get_contents(filename=""):
    file_contents = ""
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as f:
            file_contents += f.read()

    return file_contents


def file_put_contents(filename="", file_contents=""):
    with open(filename, "w+", encoding="ascii") as w:
        w.write(file_contents)
        w.close()


def confirm_directory(directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)
