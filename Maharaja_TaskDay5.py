#Create Dictionary with 5 fruit names

Fruits={'Apple':100,'Orange':80,'Kiwi':90}
print(Fruits)
print (Fruits.items())

#Print Highest mark student among 3 people

Marks={'Amit':85,'Sneha':92,'Ravi':98}
highest_marks=0
highest_mark_student=""
for i in Marks:
    if (Marks[i]>highest_marks):
        highest_marks=Marks[i]
        highest_mark_student=i
print(highest_mark_student,Marks[i])