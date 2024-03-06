#This is a programme that contains a logical error: the if-elif statement means that only the first statement is satisfied when an int greater than 60 is entered. This makes the elif statement obsolete.

print("Let's set the scene. You're driving your beautiful car down the road, jamming to music. \nYou see blue lights behind you, and pull over. \nA police officer approaches you, and asks:")

speed = int(input("'Youngster, how fast was this car travelling?' \nTell them your speed:"))

if speed > 30:
    print("Oh dear, oh dear. My eyesight is getting worse.")
elif speed > 60:
    print("Points on your licence! Points on your licence!")