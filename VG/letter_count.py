import string


def count_letters(dir_path):
    file = open(dir_path, encoding='utf-8')
    lines = file.readlines()
    dictor = {}
    for line in lines:
        for word in line:
            for c in word:
                if c in string.ascii_lowercase:
                    if (c.lower() in dictor):
                        dictor[c.lower()] += 1
                    else:
                        dictor[c.lower()] = 1
    file.close()
    return dictor

path = r"C:\Users\filip\Programering\python_courses\1DV501\fs223gv_assignment3\G\Textfiles\large_texts.txt" + r"\eng_news_100K-sentences.txt"
dictionary = count_letters(path)
XXX = 80000
for key in dictionary:
    print(key, ": ", dictionary[key]//XXX*"*")
