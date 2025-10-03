#Task_day4
#Q.1)Write a loop to flag all negative transactions in this list: txns = [100,-50,200,-75]

#For loop
print("In for loop")
list1=[100,-50,200,-75]
for i in range(0,len(list1)):
    if(list1[i]<=0):
        print(list1[i], "Negative transations")

#While loop
print("In while loop")
i=0
while i<len(list1):
    if list1[i]<0:
        print(list1[i],"Negative transations")
    i+=1
print("\n------------------End of program 1---------------------\n")
      
#Q.2)Problem statement:Transactions : [100,-50,200,-75,300],
# Tasks:1. Append new transaction -100.
#2.Find the index of the first negative transaction
#3.Remove the last transaction using pop()
#4.Find the maximum and minimum transations values

list2=[100,-50,200,-75,300]
print("Original list values: ",list2)
list2.append(-100)
print("1.After appending value -100: ",list2)
for i in range(0,len(list2)):
    if list2[i]<0:
        print("2.Find the index of the first negative transaction: ",list2.index(list2[i]))
        break
print("3.Remove the last transaction using pop(): ",list2.pop())
print("Updated list after pop: ",list2)
print("Maximum: ",max(list2))
print("Minimum: ",min(list2))
print("\n------------------End of program 2---------------------\n")

#nums=[5,2,9,1,7,2,5]
#1.Count how many times 5 occurs
#2.Remove the first 2
#3.Sort the numbers in descending order
#4.Slice the first 3 elements from the sorted list

list3=[5,2,9,1,7,2,5]
print("Original list: ",list3)
print("1.Count how many times 5 occurs: ",list3.count(5))
#Remove function will remove the first element in the list which includes first duplicate also
list3.remove(2)
print("Remove the first 2: ",list3)
list3.sort(reverse=True)
print("Sort the numbers in descending order: ",list3)
print("Slice the first 3 elements from the sorted list: ",list3[:3])

print("\n------------------End of program 3---------------------\n")

#Q.3) Friends= ["Alice", "Bob", "Charlie"]
#Tasks: 1.Extend  the list with ["David","Eve"]
#2.Make a copy of the list and clear the original one
#3.Check if "Alice" is still in the copied list
#4.Find the total number of friends in the copied list

list4=["Alice", "Bob", "Charlie"]
print("Original list: ",list4)
list4.append("David")
list4.append("Eve")
print("Extend  the list with David Eve: ",list4)
list5=list(list4)
list4.clear()
print("Make a copy of the list and clear the original one: ", "Original one: ",list4,", Updated one: ",list5)
print("Check if Alice is still in the copied list: ", "Alice" in list5)
print("Find the total number of friends in the copied list: ", len(list5))

print("\n------------------End of program 4 ---------------------\n")

#Q.5) You are reconciling transactions between Bank and Custodian records
#bank = [100,200,300,400,500]
#custodian = [100,200,250,400,600]
#Tasks: 1.Find transactions that are only in Bank but not in Custodian
#2.Find transactions that are only in Custodian but not in Bank
#3.Combine both lists and remove duplicates(use set() or list methods)
#4.Count how many total unreconcilied break exist

bank=[100,200,300,400,500]
custodian=[100,200,250,400,600]
print("Bank: ",bank,"\nCustodian: ",custodian)
unique_bank = [ t for t in bank if t not in custodian]
print("1.Find transactions that are only in Bank but not in Custodian: ",unique_bank)
unique_custodian=[k for k in custodian if k not in bank]
print("2.Find transactions that are only in Custodian but not in Bank: ",unique_custodian)
print("3.Combine both lists and remove duplicates: ",list(set(bank+custodian)))
total = len(unique_bank) + len(unique_custodian)
print("4.Count how many total unreconcilied break exist: ",total)

print("\n------------------End of program 5 ---------------------\n")

print("TUPLE TASKS\n")

#create a tuple with numbers from 1 to 5.
tuple1=(1,2,3,4,5)
print("1.Create a tuple with numbers from 1 to 5: ",tuple1,"\n")

#Access the 3rd element of (10,20,30,40,50)
tuple2=(10,20,30,40,50)
print("2.Access the 3rd element of (10,20,30,40,50): ",tuple2[2],"\n")

#Slice(1,2,3,4,5,6,7) to get (3,4,5)
tuple3 =(1,2,3,4,5,6,7)
print("3.Slice(1,2,3,4,5,6,7) to get (3,4,5): ",tuple3[2:5],"\n")

#Concatenate (1,2,3) and (4,5,6)
tuple4=(1,2,3)
tuple5=(4,5,6)
print("4.Concatenate (1,2,3) and (4,5,6): ", tuple4+tuple5,"\n")

#Count how many times 5 appears in (5,2,3,5,4,5)
tuple6=(5,2,3,5,4,5)
print("5.Count how many times 5 appears in (5,2,3,5,4,5): ",tuple6.count(5),"\n")

#Unpack ("Python", "is","fun") into 3 variables
tuple7=("Python", "is","fun")
a,b,c=tuple7
print("6.Unpack(Python, is,fun) into 3 variables:","a:",a," b:",b," c:",c,"\n")

#Create a nested tuple ((1,2),(3,4),(5,6)) and access 4th element
print("7.Create a nested tuple ((1,2),(3,4),(5,6)) and access 4th element: ")
tuple8=((1,2),(3,4),(5,6))
try:
    print(tuple8[4-1])
except:
    print("tuple index out of range\n") 

#Convert a tuple ("a","b","c") into a string "abc"
tuple9=("a","b","c")
tuple10="".join(tuple9)
print("8.Convert a tuple (a,b,c) into a string abc: ",tuple10,"Type: ",type(tuple10),"\n")

#Find the sum of all elements in (10,20,30,40)
tuple11=(10,20,30,40)
print("9.Sum of all elements in (10,20,30,40): ",sum(tuple11),"\n")

#Remove duplicate from (1,2,3,2,4,1,5)
tuple12=(1,2,3,2,4,1,5)
tuple13=tuple(set(tuple12))
print("10.Remove duplicate from (1,2,3,2,4,1,5): ",tuple13,"\n")

#You have nested  cooradinates of points ((1,2),(3,4),(5,6)). Print the y-coordinate of the second point
tuple14=((1,2),(3,4),(5,6))
print("11. ((1,2),(3,4),(5,6)) print the y-coordinate of the second point: ",tuple14[1][1])

print("\n------------------End of TUPLE Tasks ---------------------\n")
