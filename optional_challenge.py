# This programme contains two compilation errors, a runtime error and a logical error. 

print("It's your birthday. You walk into the room, and see a cake box and a group of presents. You get two choices:") #Syntax error: no parentheses when required for the print function!

present_type = input("Would you like the small present or the big present?")
while present_type == "small" or present_type == "big":
    continue
print("You've picked the {present_type} present.")                                  #Syntax error: no formatting 'f' at the beginning of the argument means that the variable will not be contained in {}.

cake_type = input("Do you want chocolate cake or vanilla cake?")
print(f"Cool - you've picked the {cake} cake.")                                     #Runtime error: the variable cake has not been defined!

if present_type == "medium":                        # Here is the logical error: present type is presumably not medium, if the user selects one of the two present_type choices indicated above. 
    print("Happy Birthday!")                        # This means the programme will simply terminate once the statement in line 9 is printed (if it was working, that is!)