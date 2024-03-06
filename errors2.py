# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "lion"         #Runtime error: the variable's value is a literal/string, and so requires "" to be a valid. I have also changed the "L" to an "l" for neatness, which I suppose could be a logical error?
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth." #Syntax error: the variables above cannot be inputted, as there is no formatting. This means eg. {animal_type} will be read as a string!
# Logical error: the variables number_of_teeth and animal_type are switched, meaning the printed statement is nonsense. I have swapped the variables around.

print(full_spec) #Syntax error: the (print) command requires parentheses for its argument.

