import os


def count_directories(dir_path, step):
    str = ""
    for x in os.scandir(dir_path):
        if os.path.isdir(x.path) and not x.name.startswith(".") and not x.name.startswith("_"):
            str += (step*"    " + x.name + "\n")
            str += count_directories(x.path, step + 1)
    if step != 0:
        return str
    else:
        print(str)


path = r"C:\Users\filip\Programering\GitLab\assignment-03"
count_directories(path, 0)
