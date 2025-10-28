print('________________________Lists_______________________________')

Txns=[100, -50, 200, -75, 300]
Txns.append(-100)
print(Txns)

print('The first negative index is', Txns.index(-50))
print('The last transaction is removed which was', Txns.pop())
print(Txns)
print('The maximum number from the list is',max(Txns))
print('The minimum number from the list is',min(Txns))


print('__________________________________________________________')

numbs=[5,2,9,1,7,2,5]
print('The count of 5 is', numbs.count(5))
numbs.remove(2)
print('Removing the first appearance of 2 -', numbs)
numbs.sort(reverse='True')
print('Sorting the list in desending order', numbs )
print('Slicing the list from 1st to 3rd', numbs[:3])
print('__________________________________________________________')

friends=['Alice', 'Bob', 'Charlotte']
friends+=('David', 'Eve')
print(friends)

friends_new=friends.copy()
print('This is new list', friends_new)
friends.clear()
print('This is old list, after the clearing', friends)

if 'Alice' in friends_new:
    print('The word is present')
else:
    print('The word is not present')

print('The total count of friends is', len(friends_new))

print('______________________________________________')

bank=[100, 200, 300, 400, 500]
custodian=[100, 200, 250, 400, 600]

#To find transactions only in bank
txns_in_bank=[]
for b in bank:
    if b not in custodian:
        txns_in_bank.append(b)
print('The transactions which are unique to bank are', txns_in_bank)

#To find transactions only in custodian
txns_in_custodian=[]
for b in custodian:
    if b not in bank:
        txns_in_custodian.append(b)
print('The transactions which are unique to custodian are', txns_in_custodian)
#Combine both lists and remove the duplicates

combined_list=custodian + bank
print(combined_list)
combined_list.sort()
for a in combined_list:
    if combined_list.count(a)>1:
        combined_list.remove(a)
print(combined_list)

print('The count of outstanding entries is',len(txns_in_bank)+len(txns_in_custodian))

print('_____________________________________________________');
print('____________________Tuples___________________________');

tup=(1,2,3,4,5)
print(tup)

tup1=(10,20,30,40,50)
print(tup1[2], 'this is 3rd element from the list')

tup2=(1,2,3,4,5,6,7)
print(tup2[2:5])

tup3=(1,2,3)
tup4=(4,5,6,7)
tup5=tup3+tup4
print(tup5)

tup6=(5,2,3,5,4,5)
print('The count of 5 is', tup6.count(5))

tup7=('Python', 'is', 'Fun')
for i in tup7:
    print(i)

tup8=(1,2)
tup9=(3,4)
tup10=(5,6)
tup11=((1,2),(3,4),(5,6))

print(tup11)
print(tup11[1][1])

tup12=('a','b','c')
str1=''.join(tup12)
print(str1)

tup14=(10,20,30,40)
sum=0
for i in tup14:
    sum+=i
print('The sum of the digits from the tuple is', sum)

tup15=(1,2,3,4,2,4,1,5)
tup16=sorted(tup15)
list1=[]
print(tup16)
for i in tup16:
    if i not in list1:
        list1.append(i)
list1=tuple(list1)
print(list1)

tup17=((1,2),(3,4)
       ,(5,6))
print('The y axis of 2nd point is', tup17[1][1])