'''Q1. Pallidrome check
Write a one-liner to check if "madam" is a pallindrome'''

print("Pallidrome check for the word madam: ")
print("madam" == "madam"[::-1])
print("------------------End of program 1---------------------")

#In Python, a one-liner function is a function that is defined in a single line, often using the lambda keyword or by writing the whole logic in one return statement.

'''Q2. Extract letters and digits from below
from "Python@123", extract:
only letters -> "Python"
ony digits -> "123" '''

print("Extract letters and digits from Python@123:")
s = "Python@123"

digit= ''.join(filter(str.isdigit,s))
letters = ''.join(filter(str.isalpha,s))

print("Letters:", letters)  # Python
print("Digits:", digit)    # 123
print("------------------End of program 2---------------------")
#In Python, the filter() function is a built-in function that is used to filter elements from a sequence (like list, string, tuple) based on a condition (True/False)

'''Q3. Clean the string(remove space)
input: " python is fun"
output: "python is fun"'''
print("remove the spaces from python is fun word: ")
input_1= " Python is fun"
print("input : ",input_1)
print("output :",input_1.strip())
print("------------------End of program 3---------------------")

#The strip() method in Python is used to remove characters from the beginning and end of a string

'''Check Methods
For each string, identify which of these return True: isalnum(),isdigit(),isnumeric()
a.) "12345"
b.) "123 1/3
c.) "Python3
d.) "Python 3'''

a="12345"
print("12345")
print("isdigit: ",a.isdigit())
print("isnumeric: ",a.isnumeric())
print("isalnum: ",a.isalnum())
print("-----")

b="123½"
print("123½")
print("isdigit: ",b.isdigit())
print("isnumeric: ",b.isnumeric())
print("isalnum: ",b.isalnum())
print("-----")

c="Python3"
print("Python3")
print("isdigit: ",c.isdigit())
print("isnumeric: ",c.isnumeric())
print("isalnum: ",c.isalnum())
print("-----")

d="Python 3"
print("Python 3")
print("isdigit: ",d.isdigit())
print("isnumeric: ",d.isnumeric())
print("isalnum: ",d.isalnum())

print("------------------End of program 4---------------------")

'''Write a program that takes a number as input and:
prints "Positive" if the number > 0
prints "negative" if the number < 0
print "Zero" otherwise'''

num1=int(input("Enter a number to find positive or negative or zero: "))

if num1 > 0:
    print("Positive")
elif num1 < 0:
    print("Negative")
else:
    print("Zero")
print("------------------End of program 5---------------------")

'''Write a program to assign a grade.
A grading system is defined as:
90+ -> "A"
80-89 -> "B"
70-79 -> "C"
below 70 -> "Fail'''

grade =float(input("Enter the mark: "))
if grade >=90:
    print("Grade A")
elif grade >=80:
    print("Grade B")
elif grade >=70:
    print("Grade C")
else:
    print("Fail")
print("------------------End of program 6---------------------")

'''Write a program to find the greatest of 3 numbers entered by the user'''

number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
number3 = int(input("Enter number3: "))



if number1 > number2 and number1 > number3:
    print("Greatest number: ",number1)
elif number2 > number1 and number2 > number3:
    print("Greatest number: ",number2)
else:
    print("Greatest number: ", number3)

print("------------------End of program 7---------------------") 

'''Write a program to check if a number is s multiple  of 7 or not'''

mul=int(input("Enter a number to check if a number is s multiple  of 7 or not: "))

if mul%7==0:
    print(mul, "is multiple of 7")
else:
    print(mul, "is not multiple of 7")

print("------------------End of program 8---------------------") 
