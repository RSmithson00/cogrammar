string = input("Give me some words.")

#letters
def letters_function(string):
    string = list(string)
    for i in range(len(string)):
        if i % 2 == 0:
            string[i] = string[i].upper()
        else:
            string[i] = string[i].lower()
    string = "".join(string)
    return string

#words
def words_function(string):
    words = string.split()
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].upper()
        else:
            words[i] = words[i].lower()
    words = " ".join(words)
    return words

a = letters_function(string)
b = words_function(string)

print(a)
print(b)
