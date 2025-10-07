Task3

#Print numbers from 1 to 100.

1.)
i = 1
while i <= 100:
    print(i)
    i += 1
    

2)
for i in range (1,101):
    print(i)
    
#Print numbers from 100 to 1.
    
    
for i in range(100, 0, -1):
    print(i)
    
    
i = 100
while i >= 1:
    print(i)
    i -= 1
    
#Print the multiplication table of 6 using a while loop.    
    
    
num = 6
i = 1
while i <= 10:
    print(f"{num * i}")
    i += 1
    
    
    
#Find the sum of all even numbers from 1 to 50 using a loop.
num = 0
for i in range(1, 51):
    if i % 2 == 0:
        num += i
print("Sum of even numbers from 1 to 50 is:", num)


i = 1
num = 0

while i <= 50:
    if i % 2 == 0:
        num += i
    i += 1

print("Sum of even numbers from 1 to 50 is:", num)






#Display the reverse of a number using a while loop (e.g., 123 → 321).

num = int(input("Enter Number"))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number is:", reverse)



#Print numbers from 1 to 20, but stop the loop if the number is 13.


for i in range(1, 21):
    if i == 14:
        break
    print(i)
    
    
#Print numbers from 1 to 20, but skip multiples of 3.
    
    
for i in range(1, 21):
    if i % 3== 0:
        continue
    print(i)
    
    
    
'''Write a program that iterates through a string and uses pass for vowels (so only consonants are printed)
Problem Statement:
Suppose opening balance = 1000. 
Transactions: [200, -100, 300, -50, -200]
Closing balance = 1150. Use a loop to calculate the net effect of transactions. Check if Opening + Net Transactions = Closing. 
If mismatch, print "Balance mismatch found" and stop (break).'''


opening_balance = 1000
transactions = [200, -100, 300, -50, -200]
closing_balance = 1150

net_effect = 0

for amount in transactions:
    net_effect += amount
    expected_balance = opening_balance + net_effect
    if expected_balance != closing_balance and amount == transactions[-1]:
        print("Balance mismatch found")
        break
else:
    print("Balance verified successfully")
    