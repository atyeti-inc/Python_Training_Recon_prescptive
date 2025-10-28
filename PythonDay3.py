# Palindrome Check

Word='madam'
Word2=Word[::-1]
if Word==Word2:
   print('The Word is palindrome')
else:
   print('The Word is not palindrome')

# Extraction
Extraction='Python@123'
Extracted=Extraction.split(sep='@')
print(Extracted)

#Space Removing
Input=' Python is fun'
Output=Input.replace(' P', 'P')
print(Output)


# Type of string
string1='12345'
string2="1231/3"
string3='Python3'
string4='Python 3'
print(string1.isnumeric())
print(string1.isalnum())
print(string2.isascii())
print(string3.isalnum())
print(string4.isascii())

# Validation of number as positive or negative
Digit=int(input('Please enter a number for validation: '))
if Digit>=0:
   print(Digit, 'is Positive Number')
else:
   print(Digit, 'is Negative Number')

# Grade assignment
Percentage=float(input('Please enter percentage to assign grade: '))

if Percentage>=90:
   print('Your grade is \'A\'')
elif Percentage>=80 and Percentage<90:
   print('Your grade is \'B\'')
elif Percentage>=70 and Percentage<80:
   print('Your grade is \'C\'')
else:
   print('You are failed')

# Highest number identification

Number1=int(input('Please enter first number: '))
Number2=int(input('Please enter second number: '))
Number3=int(input('Please enter third number: '))

if Number1 > Number2 and Number1> Number3:
   print('The First number given -',Number1, 'is higher than others')
elif Number2>Number1 and Number2>Number3:
    print('The Second number given -',Number2, 'is higher than others')
else:
    print('The Third number given -',Number3, 'is higher than others')

# To check if the number is multiple of 7
Integer=int(input('Enter a number to check if it is multiple of 7: '))
if Integer%7==0:
   print('The number -', Integer, 'is multiple of 7')
else:
   print('The number -', Integer, 'is not divisible by 7')