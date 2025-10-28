# To print numbers from 1 to 100
for n in range (1, 101):
    print(n)

# To print numbers from 100 to 1
i=100
while i!=0:
    print(i)
    i-=1

# Table of 6
i=6
while i<=60:
    print(i)
    i+=6


# Sum of all even numbers upto 50
i=0
for n in range(0,51):
    if n%2==0:
        i+=n
print('Sum of all even numbers upto 50 is', i)

# Reverse a given number
number=int(input('Enter a number for reversal : '))
reversed_number=0
while number>0:
    last_digit=number%10
    reversed_number=reversed_number*10+last_digit
    number=number//10
print(reversed_number)

# To print the numbers from 1 to 20, stop at 13
for i in range (1, 21):
    print(i)
    if i==13:
        break

# To print numbers from 1 to 20,skipping 3
for i in range(1, 21):
    if i%3==0:
        continue
    else:
        print(i)
# To skip the vowels 
string='abcdefghijklmnopqrstuvwxyz'
string_split=string.split()
print(string_split)
to_skip=['a', 'e', 'i', 'o', 'u']
to_print=[]
for n in string:
    if n in to_skip:
        continue
    else:
        print(n, end='')  ;

# Balance Validation
Opening_balance=1000
Transactions=[100, 10, -10, -100, -100]
Closing_balance=900
Net_of_transactions=0

for i in Transactions:
    Net_of_transactions+=i

if Opening_balance+Net_of_transactions==Closing_balance:
    print('\nBalances match..')
else:
    print('Balances are mismatched')