#Task1: To check whether given value is palindrom or not
a=str(input("Please Enter the Value:"))
if a.lower()==a.lower()[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
	
#Task2: To fetch digit values either by numeric or string
a="Python@123"
print(a[0:6])
print(a[7:10])

#Task3: To remove whitespaces from both ends
a=" Python is fun "
b=a.strip()
print(b)

#Task4:
a='12345'
b=a.isnumeric()
print(b) #True

a="python 3"
b=a.isascii()
print(b)

a="1231/3"
b=a.isascii()
print(b)

#Task5: To find the numeric value is positive or negative
a=int(input("Please Enter the value:"))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")
    
#Task6: Assigning the Grade by marks 
a=int(input("Please Enter the value:"))
if a>=90:
    print("Grade A")
elif a>=80 and a<90:
    print("Grade B")
elif a>=70 and a<80:
    print("Grade C")
else:
    print("Fail")
    
Task7: To find highest value among 3 numbers
a=int(input("Please Enter the value1:"))
b=int(input("Please Enter the value2:"))
c=int(input("Please Enter the value3:"))
if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
else:
    print("C is greater")

#Task8: To find whether given value is multiple of 7 or not
a=int(input("Please Enter the value1:"))
if ((a%7)==0):
    print("The value is multiple of 7")
else:
    print("The value is not multiple of 7")