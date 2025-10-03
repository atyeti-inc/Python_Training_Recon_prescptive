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
