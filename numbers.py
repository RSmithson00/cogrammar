num1 = int(input("Please enter your first number."))
num2 = int(input("Please enter your second number."))
num3 = int(input("Please enter your third number."))

#Sum of all
print("The sum of your numbers is: " + str(num1 + num2 + num3))

# 1st - 2nd
print("Your first number minus your second number is: " + str(num1-num2))

# 3rd x 1st
print("Your third number multiplied by your first number is: " + str(num3*num1))
#print(num3*num1)

# (sum of all) / 3
sum = str((num1 + num2 + num3) / num3)
print(f"The sum of all your numbers over your third number is: {sum}.")