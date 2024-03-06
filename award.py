swimming = int(input("How long did the athlete take in the swimming section?"))
cycling = int(input("How long did the athlete take in the cycling section?"))
running = int(input("And how long did the athelete take in the race section?"))

time_range = swimming + cycling + running

if time_range <= 100:
    print("The athelete wins Provincial Colours.")
elif time_range >= 101 and time_range <= 105:
    print("The athlete wins Provincial Half Colours.")
elif time_range >= 106 and time_range <= 110:
    print("The athelte wins the Provincial Scroll.")
else:
    print("Your time was greater than 110 minutes. No award won.")