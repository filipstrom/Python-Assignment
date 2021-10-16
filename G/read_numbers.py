import math


def mean(lst):
    return sum(lst)/len(lst)


def std(lst):
    m = mean(lst)
    newlst = []
    for i in lst:
        newlst.append(math.pow(i - m, 2))
    return math.sqrt(mean(newlst))


path = r"C:\Users\filip\Programering\python_courses\1DV501\fs223gv_assignment3\G\10000_integers\file_10000integers_A.txt"
path2 = r"C:\Users\filip\Programering\python_courses\1DV501\fs223gv_assignment3\G\10000_integers\file_10000integers_B.txt"

path = r"C:\Users\filip\Programering\python_courses\1DV501\fs223gv_assignment3\G\test.txt"

file = open(path, "r")

line_count = 0
numbers = []
for line in file:
    for i in line.split():
        num = ""
        for c in i:
            if c.isdigit():
                num += c
        numbers.append(int(num))
print(mean(numbers))
print(std(numbers))
file.close()


file = open(path, "r")

line_count = 0
numbers2 = []
for line in file:
    for c in line.split(":"):
        numbers2.append(int(num))
print(mean(numbers2))
print(std(numbers2))
file.close()
