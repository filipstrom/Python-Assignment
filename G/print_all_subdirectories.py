import os


def print_subdirectories(dir_path):
    for s in os.scandir(dir_path):
        if s.is_dir():
            print(s.name)
            print_subdirectories(s.path)


path = r"C:\Users\filip\Programering\python_courses\1DV501"
print_subdirectories(path)
