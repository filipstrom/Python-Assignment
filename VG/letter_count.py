import string


def getKey(tpl):
    return tpl[0]


# Sort dict after key
def SortedDict(dct):
    items = list(dct.items())
    keySorted = sorted(items, key=getKey)
    return keySorted


# Counts letters in the file
def count_letters(dir_path):
    file = open(dir_path, encoding='utf-8')
    lines = file.readlines()
    total = 0
    dictor = {}
    for line in lines:
        for word in line:
            for c in word:
                cl = c.lower()
                if cl in string.ascii_lowercase:
                    if (cl in dictor):
                        dictor[cl] += 1
                    else:
                        dictor[cl] = 1
                    total += 1
    print("Total numbers of letters:", total)
    file.close()
    return dictor


# Sets the paths
path = (r"C:\Users\filip\Programering\GitLab\assignment-03\G\Textfiles" +
        r"\large_texts.txt\eng_news_100K-sentences.txt")
path2 = (r"C:\Users\filip\Programering\GitLab\assignment-03\G\Textfiles" +
         r"\large_texts.txt\holy_grail.txt")

# Print all the output
dictionary = count_letters(path)
XXX = 20000
for key in SortedDict(dictionary):
    print(key[0], ": ", key[1]//XXX*"*")

dictionary2 = count_letters(path2)
XXX = 100
for key in SortedDict(dictionary2):
    print(key[0], ": ", key[1]//XXX*"*")
