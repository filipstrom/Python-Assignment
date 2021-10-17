def count_different(lst):
    return len(set(lst)) 


def count_occurrences(lst):
    return {item: lst.count(item) for item in lst}


def filesplit(file, string):
    numbers = []
    for line in file:
        numbers += [int(num) for num in line.split(string)]
    return numbers


def getValue(tpl):
    return tpl[1]


def mostCommon5(dct):
    items = list(dct.items())
    valueSorted = (sorted(items, key=getValue))[::-1]
    for k, v in valueSorted[:5]:
        print(k, "\t", v)


file = open(r"C:\Users\filip\Programering\GitLab\assignment-03\G" +
            r"\10000_integers\file_10000integers_A.txt").readlines()
file2 = open(r"C:\Users\filip\Programering\GitLab\assignment-03\G" +
             r"\10000_integers\file_10000integers_B.txt").readlines()
numbers = filesplit(file, ", ")
numbers2 = filesplit(file2, ":")
dictnumbers = count_occurrences(numbers)
dictnumbers2 = count_occurrences(numbers2)

print("For File A:")
print("Different integers", count_different(numbers))
print("most common numbers")
mostCommon5(dictnumbers)
print()
print("For File B:")
print("Different integers ", count_different(numbers2))
print("most common numbers")
mostCommon5(dictnumbers2)
