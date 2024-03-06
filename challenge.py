# Add 'un' prefix to a word - DONE
def add_prefix_un(word):
    new_word = "un" + word
    return new_word

print(add_prefix_un(word = input("Give me a word: ")))

# Add prefixes to word groups - en, pre, inter, auto - DONE
def make_word_groups(vocab_words):
    vocab_words = vocab_words.split(", ")
    print(vocab_words)
    prefix = vocab_words[0]
    print(prefix)
    semi_string = vocab_words[1:]
    final_string = []
    for i in semi_string:
        final_string.append(prefix + i)
    final_string.insert(0, prefix)
    return final_string

print(make_word_groups(vocab_words = input("Give me your prefix and list of words: ")))

# Remove 'ness' suffix from a word
def remove_suffix_ness(word):
    new_word = list(word)
    for i in range(5):
        new_word.pop()
    new_word = "".join(new_word)
    new_word = new_word + "y"
   
    return new_word

print(remove_suffix_ness(word = input("Give me your -ness word: ")))

# Extract and transform a word - verbify - DONE
def adjective_to_verb(sentence, index):
    sentence_list = sentence.split()
    index = int(index)
    new_word = sentence_list[index] + "en"
    return new_word

print(adjective_to_verb(sentence = input("Give me a sentence: "), index = input("Give me the index of the verb: ")))