#Create a dictionary of 5 Fruits with their prices
dict={"apple":50,"Mango":40,"Guava":30,"Orange":1,"Pineapple":2}
print(dict)

#Find student with highest marks from marks={"amit":85,"sneha":92,"ravi":78}
student={"Amit":85,"sneha":92,"Ravi":78}
highest_marks=0
high_mark_student=""
for i in student:
    if (student[i]>highest_marks):
        highest_marks=student[i]
        highest_mark_student=i
print(highest_mark_student)

#Count word frequency in a sentence using dictionary
sentence=input("Enter the sentence:")
words=sentence.split( )
dict={}

for i in words:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)

#create a set of unique subjects from:['python','java','python','c++','java']
set_1={'python','java','python','c++','java'}
print(set_1)
#Findcommon student in two batches using set intersection
set_1={"Ram","Raghav","sneha","Kajal"}
set_2={"Ram","Kajal","shyam","Raja"}
print(set_1.intersection(set_2))

#Write a function greet username(name,msg="Welcome!") that prints:"Hello<name>,<msg>"
def greet(name,msg="Welcome!"):
    print(name,msg)
greet("hello Chandra")

#Write a function sum_All(*numbers) that returns the sum of all numbers passed to it e.g:sum_all(1,2,3,4)-->10
def sum_(*numbers):
    print(sum(numbers))
sum_(10,2)

#Write a function Arithmetic_ops(A,B) that returns sum,difference,product and quotient of A and B.e.g:Arithmetic_ops(10,2)-->(12,8,20,5.0)
def Arithmetic_Ops(A,B):
    print("Sum:",A+B)
    print("Difference:",A-B)
    print("Product:",A*B)
    print("Quotient:",A/B)
Arithmetic_Ops(10,2)

