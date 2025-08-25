import sys  #import used to stop program if negative values are inserted as provide in line 5 and 10
hours=int(input("Give me a total number of hours:"))
if hours<0:
    print("You cannot have negative hours!")
    sys.exit()

minutes=int(input("Give me a total number of minutes:"))
if minutes<0:
    print("You cannot have negative hours!")
    sys.exit()

seconds=(hours*60*60)+(minutes*60)   #converts hours and minutes to seconds and adds them together
print("You have ",hours,"hours and",minutes,"minutes") #prints user entered hours and minutes values
print("If you were to convert that in seconds it would be",seconds,"seconds.") #prints the converted seconds
