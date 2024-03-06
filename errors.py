# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program.")   #Syntax error: no parentheses as required by the print command.
print("\n")                             #Syntax errors: unexpected/unnecessary indent, and no parentheses as required by the print command.

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24 years old"            #Syntax error: unexpected/unnecessary indent, the == indicates equivalence not variable-value assignment (should be =). Also the capitalised 'S' in the variable name seems to be somewhat of a departure from variable-naming norms.

age_str = age_str.strip()
age_str = age_str[0:2]

# Runtime error: the input for the variable age_str is a literal/string, so it cannot be cast to an integer in the line below. 
# This could be solved in two (?)) ways: removing "years old" from the string input, leaving only the digits; or removing any alphabetical characters from the string in the program, which would be neater.
# The problem with solution two (removing other characters from the "years old" string) is if eg. the programme was based on user input, this would restrict number inputs to two digits, eg. 5 or 102 would create a logical error.

age = int(age_str)                  #Syntax error: unexpected/unnecessary indent
print(f"I'm {age} years old.")   #Syntax errors: unexpected/unnecessary indent. Runtime error: age contains an integer, cannot be concatenated, and cannot be printed without casting or formatting (I have chosen the latter in order to maintain my argument on the string -> int casting above)

# Variables declaring additional years and printing the total years of age
years_from_now = 3                #Syntax error: unexpected/unnecessary indent. Runtime error: years_from_now is a literal/string and so cannot be used in mathematical operations - I will remove the "" to make it an integer.
total_years = age + years_from_now  #Syntax errors: unexpected/unnecessary indent. Variable is an integer so cannot be used in maths operations, making these two lines erroneous.

print(f"The total number of years: {total_years}") #Syntax error: no parentheses for the print command. I also added a space to the print argument to make the output neater to read for the user. Runtime error: total_years is an integer and cannot be concatenated without casting or formatting.
#Logical error: answer_years does not exist as a variable, and does not make sense as a print statement! I will change this to total_years, which seems to make more sense here.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12                                         #Logical error: total is not a variable. 
print(f"In 3 years and 6 months, I'll be {(total_months + 6)} months old.")   #Syntax error: no parentheses for the print command. Runtime error: total_months is an integer, cannot be concatenated during print without casting or formatting.
# Logical error: without manually adding 6 months onto the total count, total_months != 330 as indicated below. Either the "and 6 months" statement is an error, or a manual calculation has been omitted (I have chosen to fix the latter for experience's sake).

#HINT, 330 months is the correct answer

