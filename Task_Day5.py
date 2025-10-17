## Day 6
# 1. Create a dictionary of 5 fruits with their prices
dict={"Mango":40, "Orange":50, "Apple":60, "Orange":65, "Banana":35}
print(dict)

# 2. 
marks={"Amit":85, "Sneha":92, "Ravi":78}
highest_score=0
highest_score_student=""
for i in marks:
    if marks[i]>highest_score:
        highest_score=marks[i]
        highest_score_student=i
print(highest_score_student)

# 3. Count word frequency in a sentence using dictionary 
from collections import Counter
sentence="Hello this is Sumithaa. This is Python practice questions"
words=sentence.split()
count=Counter(words)
print(count)

# 4.Create a set
words=['Python','Java','Python','C++','Java']
print(set(words))

# 5. common intersection
set1=({'Sumi', 'Sai', 'Kavya', 'Harini', 'Nithesh'})
set2=({'Sumi', 'Raj', 'Nithesh', 'Priya', 'Sai'})
common_set=set1.intersection(set2)
print(common_set)

# 6. 
def greet(name,msg):
    print(f"Hello {name}, {msg}")

greet("Sumithaa", "Welcome")

# 7. 
def sum_all(*numbers):
    return sum(numbers)
print(sum_all(1,2,3,4))
print(sum_all(5,10))

# 8.
def arithmetic_ops(a,b):
    addition=a+b
    print(f"Addition of two numbers is: {addition}")
    difference=a-b
    print(f"Difference of two numbers is: {difference}")
    product=a*b
    print(f"Product of two numbers is: {product}")
    quotient=a/b
    print(f"Quotient of two numbes is: {quotient}")

arithmetic_ops(31,12)

