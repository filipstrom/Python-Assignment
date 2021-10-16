import os


def count_directories(dir_path, step):
    str = ""
    for x in os.listdir(dir_path):
        str += (step*"    " + x + "\n")
        if not ("." in x):
            str += count_directories(dir_path + "\\" + x, step + 1)
    if step != 0:
        return str
    else:
        print(str)


path = r"C:\Users\filip\Programering\python_courses\1DV501\fs223gv_assignment3"
count_directories(path, 0)

os.getcwd()
os.listdir(r"C:\Users\filip\Programering\python_courses\1DV501\fs223gv_assignment3\G")
os.chdir()
os.scandir(r"C:\Users\filip\Programering\python_courses\1DV501\fs223gv_assignment3\G")
