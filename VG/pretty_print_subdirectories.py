import os


# Prints the directories with indent
def print_subdirectories(dir_path, step):
    str = ""
    for x in os.scandir(dir_path):
        if (os.path.isdir(x.path) and not x.name.startswith(".")
           and not x.name.startswith("_")):
            str += (step*"    " + x.name + "\n")
            str += print_subdirectories(x.path, step + 1)
    if step != 0:
        return str
    else:
        print(str)


path = r"C:\Users\filip\Programering\GitLab\assignment-03"
print_subdirectories(path, 0)
