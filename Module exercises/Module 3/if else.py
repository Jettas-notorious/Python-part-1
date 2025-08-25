income = float(input("Enter the annual income: "))
if income<85528:
    tax=income*0.18-556.02
    if tax<0:
       print("The tax is:0.0", "thalers") 
elif income>85528:
    tax=14839.02+85528*0.32
   


tax = round(tax, 0)
print("The tax is:", tax, "thalers")