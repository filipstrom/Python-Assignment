import math


def mean(lst):
    return sum(lst)/len(lst)


def std(lst):
    m = mean(lst)
    newlst = []
    for i in lst:
        newlst.append(math.pow(i - m, 2))
    return math.sqrt(mean(newlst))


path = r"C:\Users\filip\Programering\GitLab\assignment-03\G\10000_integers\file_10000integers_A.txt"
path2 = r"C:\Users\filip\Programering\GitLab\assignment-03\G\10000_integers\file_10000integers_B.txt"

file = open(path, "r").readlines()

line_count = 0
numbers = []
for line in file:
    for i in line.split(", "):
        numbers.append(int(i))

file = open(path2, "r").readlines()

line_count = 0
numbers2 = []
for line in file:
    for i in line.split(":"):
        numbers2.append(int(i))

print("mean A:", mean(numbers))
print("std A:", std(numbers))
print("Mean B:", mean(numbers2))
print("STD B:", std(numbers2))

