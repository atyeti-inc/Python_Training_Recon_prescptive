## Day 3
## 1. Palindrome check
print("madam" == "madam"[::-1])

## 2. Extract letters and numbers
str1="Python@123"
letters=str1[:6]
numbers=str1[7:10]
print(f"The extracted letters from the string is: {letters}")
print(f"The extracted digits from the string is: {numbers}")

## 3. Clean the string
str1= " Python is fun "
output=str1.strip()
print(output)

## 4. Check methods
strings={"12345", "1231/3", "Python3", "Python 3"}
for s in strings:
    print(f"Sring: '{s}'")
    print("isalnum: ", s.isalnum())
    print("isdigit: ", s.isdigit())
    print("isnumeric:", s.isnumeric())


## 5. Program to take inputs and assign positive, negative
number1=int(input("Enter the number: "))
if number1>0:
    print("Positive")
elif number1<0:
    print("Negative")
else:
    print("Zero")

## 6. Program to assign a grade
grade=int(input("Enter the grade: "))
if grade >= 90:
    print("The Grade obtained is: A")
elif 80 <= grade <= 89:
    print("The Grade obtained is: B")  
elif 70 <= grade <= 79:
    print("The Grade obtained is: C")
else:
    print("The Grade obtained is Fail")

## 7. Program to find the greatest of 3 numbers entered by the user.
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if a>=b and a>=c:
    greatest=a
elif b>=a and b>=c:
    greatest=b
else:
    greatest=c
print("The greatest number is: ", greatest)

## 8. Program to check if a number is multiple of 7 or not
number=int(input("Enter the number: "))
check=number%7
if check==0:
    print(f"The given number-{number} is multiple of 7")
else:
    print(f"The given number-{number} is not multiple of 7")





