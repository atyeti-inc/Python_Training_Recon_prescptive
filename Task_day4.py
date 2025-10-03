#Write a loop to flag all negative transactions in this list:txns=[100,-50,200,-75]
txns=[100,-50,200,-75]
list1=[]
for i in range(len(txns)):
    if txns[i]<0:
        list1.append(txns[i])
print("The negative value in the txns are:",list1)


'''
Transactions:
txns=[100,-50,200,-75,300]
tasks:
a)Append a new transaction -100
b)Find the index of the first negative transaction
c)remove the last transaction using pop()
d)find the maximum and minimum transaction values
'''
#a)Append a new transaction -100
txns=[100,-50,200,-75,300]
txns.append(-100)
print(txns)
#b)Find the index of the first negative transaction
for i in range(len(txns)):
    if txns[i]<0:
        print("The index of the first negative value in txns is:",txns.index(txns[i]))
        break
#c)remove the last transaction using pop()
txns.pop()
print(txns)
#d)find the maximum and minimum transaction values
print("The maximum value in the txns is:",max(txns))
print("The minimum value in the txns is:",min(txns))


'''
nums=[5,2,9,1,7,2,5]
Tasks:
a)Count how many times 5 occurs
b)Remove the first 2
c)Sort the numbers in descending order
d)Slice the first 3 elements from the sorted list
'''
nums=[5,2,9,1,7,2,5]
#a)Count how many times 5 occurs
print("The count of 5 occurs:",nums.count(5))
#b)Remove the first 2
for i in nums:
    if(i==2):
        nums.remove(2)
        break
print(nums)
#c)Sort the numbers in descending order
nums.sort(reverse=True)
print(nums)
#d)Slice the first 3 elements from the sorted list
print(nums[0:3])


'''
Friends=["Alice","Bob","Charlie"]
Tasks:
a)Extend the list with ["David","Eve"]
b)Make a copy of the list and clear the original one
c)Check if "Alice" is still in the copied list
d)Find the total number of friends in the copied list
'''
Friends=["Alice","Bob","Charlie"]
#a)Extend the list with ["David","Eve"]
Friends.extend(["David","Eve"])
print(Friends)
#b)Make a copy of the list and clear the original one
Friends_copy=Friends.copy()
print("The list of friends present in the copied list:",Friends_copy)
Friends.clear()
print(Friends)
#c)Check if "Alice" is still in the copied list
print("Alice" in Friends_copy)
#d)Find the total number of friends in the copied list
count=0
for i in Friends_copy:
    count=count+1
print("The total number of friends in the copied list:",count)


'''
You are reconciling transactions between Bank and custodian records
bank=[100,200,300,400,500]
custodian=[100,200,250,400,600]
Tasks:
a)Find transactions that are only in Bank but not in Custodian
b)Find transactions that are only in custodian but not in Bank
c)Combine both lists and remove duplicates(use set() or list methods)
d)Count how many total unreconciled breaks exist
'''
bank=[100,200,300,400,500]
custodian=[100,200,250,400,600]
#a)Find transactions that are only in Bank but not in Custodian
print("The transaction that are only in Bank:")
for i in bank:
    if i not in custodian:
        print(i)
#b)Find transactions that are only in custodian but not in Bank
print("The transaction that are only in Custodian:")        
for i in custodian:
    if i not in bank:
        print(i)
#c)Combine both lists and remove duplicates(use set() or list methods)
bank_custodian=bank+custodian
print(bank_custodian)
remove_duplicate=[]
for i in bank_custodian:
    if i not in remove_duplicate:
        remove_duplicate.append(i)
print("The list of values after removing the duplicates:",remove_duplicate)
#d)Count how many total unreconciled breaks exist
count=0
for i in bank:
    if i not in custodian:
        count=count+1
for i in custodian:
    if i not in bank:
        count=count+1
print("The total unreconciled breaks exist:",count)


#create a tuple with numbers from 1 to 5
tuple_=(1,2,3,4,5)
print(tuple_)


#Access the 3rd element (10,20,30,40,50)
tuple1=(10,20,30,40,50)
print("The 3rd elememt in the tuple is:",tuple1[2])


#Slice (1,2,3,4,5,6,7) to get (3,4,5)
tuple2=(1,2,3,4,5,6,7)
print(tuple2[2:5])


#Concate(1,2,3) and (4,5,6)
tuple_1=(1,2,3)
tuple_2=(4,5,6)
print(tuple_1+tuple_2)


#Count how many times 5 appears in (5,2,3,5,4,5)
T1=(5,2,3,5,4,5)
print("The count of 5 is:",T1.count(5))


#Unpack("Python","is","fun") into three variables
tuple_=("Python","is","fun")
tuple1=tuple_[0]
tuple2=tuple_[1]
tuple3=tuple_[2]
print(tuple1)
print(tuple2)
print(tuple3)


#Create a nested tuple((1,2),(3,4),(5,6)) and access element 4.
tuple3=((1,2),(3,4),(5,6))
print(tuple3[1][1])


#Convert the tuple("a","b","c") into a string "abc"
tuple4=("a","b","c")
str=""
for i in range(0,len(tuple4),1):
    str=str+tuple4[i]
print("The String is:",str)


#Find the sum of all elements in (10,20,30,40)
tuple_=(10,20,30,40)
print("The sum of all elements:",sum(tuple_))


#Remove duplicates from (1,2,3,2,4,1,5)
t1=(1,2,3,2,4,1,5)
l1=[]
for i in t1:
    if i not in l1:
        l1.append(i)
unique_tuple=tuple(l1)
print("The list of values after removing the duplicates:",unique_tuple)


#Create a nested tuple((1,2),(3,4),(5,6)).Print the y-axis coordinate of the second point
tuple3=((1,2),(3,4),(5,6))
print(tuple3[1][1])


