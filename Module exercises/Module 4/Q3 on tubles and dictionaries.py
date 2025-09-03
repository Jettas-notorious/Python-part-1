tuple1=("Alice","Bob","Charlie")
name_score={
        tuple1[0]:85,
        tuple1[1]:90,
        tuple1[2]:78,
}
for elem in name_score.items():
    print("Here follows the names and scores of each student:\n",elem)


high_score=name_score[tuple1[0]]
print(high_score)
