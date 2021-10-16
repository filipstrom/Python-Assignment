import os


def count_py_lines(dir_path):
    file = open(dir_path, encoding='utf-8')
    lines = file.readlines()
    file.close()
    return len(lines)


def find_every_pythonfile(path):
    sum = 0
    for e in os.scandir(path):
        if e.is_dir():
            sum += find_every_pythonfile(e.path)
        elif e.name.endswith(".py"):
            sum += count_py_lines(e.path)
    return sum


path2 = r"C:\Users\filip\Programering\python_courses\1DV501"
print(find_every_pythonfile(path2))
