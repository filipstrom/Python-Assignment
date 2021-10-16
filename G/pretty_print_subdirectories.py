import os


def count_directories(dir_path, step):
    str = ""
    for x in os.scandir(dir_path):
        if x.is_dir():
            str += (step*"    " + x.name + "\n")
            str += count_directories(x.path, step + 1)
    if step != 0:
        return str
    else:
        print(str)


path = r"C:\Users\filip\Programering\python_courses\1DV501\fs223gv_assignment2"
count_directories(path, 0)
