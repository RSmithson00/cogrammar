str_manip = input("Please give me a sentence, lovely user.")

#display length
print(f"The length of your sentence is: {len(str_manip)}.")

#last letter -> all instances are @
replace_char = str_manip[-1]
print(str_manip.replace(replace_char, "@"))


# last 3 letters backwards
print(str_manip[-1:-4:-1])

# 5 letter word
print(str_manip[0:3] + str_manip[-2:])