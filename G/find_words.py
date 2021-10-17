def read_file(file_path):
    file = open(file_path, encoding='utf-8')
    lines = file.readlines()
    file.close()
    return lines


# Find every word in a row
def get_words(row):
    words = []
    for word in row.lower().split():
        newword = ""
        for c in word:
            newword += c.strip("1234567890!?#&.,_|\n:;()%¤$—–-•’”“")
        if newword != "":
            if len(newword) == 1:
                if newword == "a" or newword == "i":
                    words.append(newword)
            else:
                words.append(newword)
    return words

def save_words(file_path, words):
    file = open(file_path, "w", encoding="utf-8")
    for word in words:
        file.write(word + " ")
    file.close()


# Read text files
path = r"C:\Users\filip\Programering\Gitlab\assignment-03\G\Textfiles\large_texts.txt" + r"\eng_news_100K-sentences.txt"
rows = read_file(path)
print(f"\nRead {len(rows)} lines from file {path}")

# Collect words
words = []
for row in rows:
    w = get_words(row)  # Returns a list of words
    words += w
# Save words in file
outpath = r"C:\Users\filip\Programering\Gitlab\assignment-03\G\output\\" + f"output_{len(words)}_words.txt"
save_words(outpath, words)
print(f"Saved {len(words)} words in file {outpath}")  # About 1.8 million words
