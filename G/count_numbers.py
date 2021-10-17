def count_different(lst):
    return len(set(lst)) 


def count_occurrences(lst):
    print({item: lst.count(item) for item in lst})
    return {item: lst.count(item) for item in lst}

def filesplit(file, string):
    numbers = []
    for line in file:
        numbers += {int(num) for num in line.split(string)}
    return numbers

file2 = open(r"C:\Users\filip\Programering\GitLab\assignment-03\G\10000_integers\file_10000integers_B.txt")

file = open(r"C:\Users\filip\Programering\GitLab\assignment-03\G\10000_integers\file_10000integers_A.txt")
numbers = filesplit(file, ", ")
numbers2 = filesplit(file2, ":")
print(count_different(numbers))
print(count_different(numbers2))
dictnumbers = count_occurrences(numbers)

listsorted = sorted(dictnumbers.values())
dictsorted = {}
listkeys = []
for i in reversed(listsorted):
    for k in dictnumbers.keys():
        if dictnumbers[k] == i:
            dictsorted[k] = dictnumbers[k]
            listkeys.append(k)
            break
print(dictsorted)
print("most common numbers")
for i in range(0, 5):
    print(listkeys[i])
