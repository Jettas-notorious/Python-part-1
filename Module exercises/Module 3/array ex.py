hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

number=int(input("Replace the middle number:"))
hat_list[2]=number

del hat_list[4]

print("The length of the list is:",len(hat_list))

print(hat_list)
