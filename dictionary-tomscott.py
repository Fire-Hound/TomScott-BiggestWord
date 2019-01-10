import re
with open("words.txt") as f:
    words = f.readlines()
    bad_words = re.compile("[gkmqvwxzio]")
    biggest_word = ""
    print(len(words))

    for word in words:
        word = word.lower()
        if re.search(bad_words, word):
            continue
        if len(biggest_word)<=len(word):
            biggest_word = word
            print(biggest_word + str(len(biggest_word)))
    print(biggest_word + str(len(biggest_word)))
