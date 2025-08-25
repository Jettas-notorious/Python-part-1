pro1=input("Gime me a product:")  #From line 1 till line 6 asks user for a prouct and a price
pro2=input("Give me a product:")
pro3=input("Give me a product:")
cost1=int(input("How much does the product cost?\n"))
cost2=int(input("How much does the product cost?\n"))
cost3=int(input("How much does the product cost?\n"))
print(pro1," costs R",cost1,sep="") #prints product and its price
print(pro2," costs R",cost2,sep="")
print(pro3," costs R",cost3,sep="")

subtotal=cost1+cost2+cost3 #calculates stotal subcost
Vat=(cost1+cost2+cost3)*15/100 #clculates total VAT
total=subtotal+Vat #calculates total cost VAT included

print("Your subtotal is R",subtotal,".","\nYour VAT @15% is R",Vat,".","\nYour total cost will be R",round(total,2),".",sep="") #prints everything

