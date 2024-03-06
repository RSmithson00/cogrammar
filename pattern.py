#This piece of code outputs an increasing-decreasing star pattern with a max. of 5
#requirements: 1 for loop, 1 if-else statement
#I feel the pattern[1:index] is somewhat cheating / seems inelegant - is this a correct assumption?
stars = 1
pattern = "*****"


for i in range(0,9):
    index = 10 - i
    if stars <= 5:
        print(stars * "*")
        stars += 1
    else:
        print(pattern[1:index])