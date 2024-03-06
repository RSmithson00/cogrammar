#get name, assign variable
name = input("What's your name?")
#get age, assign variable
age = input("And what's your age?")
#get house no., ibid
house_number = input("Please provide your house number.")
#get st name, ibid
street_name = input ("Please tell us the name of the street you live on.")

#print all user details in one sentence
print("Hello {}. You are {} years old and you live at house number {} on {}.".format(name, age, house_number, street_name))