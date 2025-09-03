tuple1=("apple","banana","cherry","apple","orange","banana")
print("The length of this thing is:",len(tuple1),"elements")
x=0
y=0

for word in tuple1:
    if word=="apple":
        x+=1
print("The word apple appears",x,"times")

for index in tuple1:
    if index=="cherry":
        print("The word cherry was found at index",y)
        break
    y+=1