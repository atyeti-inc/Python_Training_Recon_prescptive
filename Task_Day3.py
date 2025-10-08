## Day 4
## Print numbers from 1 to 100
for i in range(1,101):
    print(i)

## Print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)

## Print the multiplication of table 6 using while loop
i=1
while i <= 10:
    print(f"6 x {i}: {6 * i}")
    i+=1

## Find the sum of all even numbers from 1 to 50 using a loop
total=0
for i in range(1,51):
    if i%2==0:
        total +=i
print("Sum of even numbers from 1 to 50 is:", total)

## Display the reverse of a number using while loop
num=input("Enter the number:")
reverse_str=""

i = len(num)-1
while i >= 0:
    reverse_str += num[i]
    i -=1

print("Reverse of", num, "is", reverse_str)

## Print numbers 1 to 20 but skip if number is 13
for i in range(1,21):
    if i==13:
        break
    print(i)

## Print numbers 1 to 20 but skip multiples of 3
for i in range(1,21):
    if i%3==0:
        continue
    print(i)

## Write a program to iterate through the string and uses pass for vowels(so only consonants are printed)
string=input("Enter a string:")

for char in string:
    if char.lower() in 'aeiou':
        pass
    else:
        print(char, end='')


## Problem Statement:
Opening_balance=1000
Transactons=[200, -100, 300, -50, -200,]
Closing_balance=1150
for i in Transactons:
    i += Opening_balance
    if i != Closing_balance:
        print("Balance mismatch found")
        break
    else:
        print("Balance matched")




