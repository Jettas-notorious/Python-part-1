temp=float(input("Give me a temperature:"))
scale=input("What do you want your scale to be?(C)\n")
print(temp,"C",sep="")

con1=(temp*9/5)+32 #converts temps
con2=temp+273.15
print(con1,"F",sep="") #rpnits the converted temps
print(con2,"K",sep="")

