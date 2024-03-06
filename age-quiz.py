#input age and store in int variable
age = int(input("Please input your age."))

# if age == 21, print congrats on 21st
if age == 21:
    print("Congrats on your 21st!")
#if age < 13, print qualify for kiddie discount
elif age < 13:
    print("You qualify for the kiddie discount.")
# if age => 40, print you're old
elif age >= 40 and age <= 64:
    print("You're over the hill.")    
#if age => 65 print enjoy retirement
elif age >= 65 and age <= 100:
    print("Enjoy your retirement.")
 # if age > 100, print sorry you're dead
elif age > 100:
    print("Sorry, you're dead.")
#any other age (13-20, 22-39) print age is but a number
else:
    print("Age is but a number.")