# The user inputs integers using the number variable. 
# A running sum is stored in the sum_of_guesses variable, and then divided by the guess counter when the user inputs -1.
# -1 is not included in the mean calculation.

number = 0
sum_of_guesses = 0
guess_counter = 0
print("This piece of code will allow you to input a series of integers. 
\n When you input -1, the code will calculate the mean of your inputted integers (not including the -1). Let's begin!")

while number != -1:
    number = int(input("Please enter a number:"))
    if number == -1 and guess_counter == 0:
        confirmation = input("Are you sure you want to terminate the programme? Please type 'Y' to confirm.")
        if confirmation == "Y":
            print("Understood! Programme terminated.")
            break
        else:
            number = int(input("Please enter a number:"))
    if number != -1:
        guess_counter = guess_counter + 1
        print(f"Your number of guesses is: {guess_counter}.")
        sum_of_guesses = sum_of_guesses + number
        print(f"Your running total is: {sum_of_guesses}.")
    if number == -1 and guess_counter != 0:
        print(f"The average of your guesses is {str((sum_of_guesses/guess_counter))}.")
