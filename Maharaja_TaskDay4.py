#Write a loop to flag all negative transactions in this list: txns = [100, -50, 200, -75] 
txns=[100,-50,200,-75]
for i in txns:
    if i<0:
        print(i)


#txns = [100, -50, 200, -75, 300]
# Append a new transaction -100.
txns = [100, -50, 200, -75, 300]
txns.append(-100)
print(txns)

#Print 1st occurance of negative value
txns = [100, -50, 200, -75, 300]
for i in txns:
    if i<0:
        print(txns.index(i))
        break
		
## Remove the last transaction using pop().
txns = [100, -50, 200, -75, 300]
txns.pop(-1)
print(txns)


#To print max & min values from the list
txns = [100, -50, 200, -75, 300]
print("The maxvalue of txns is:", max(txns))
print("The minvalue of txns is:", min(txns))

#To print no of 5 present in the listnums = [5, 2, 9, 1, 7, 2, 5]
i=nums.count(5)
print(i)

#To remove first occurance of value 2
nums = [5, 2, 9, 1, 7, 2, 5]
nums.remove(2)
print(nums)

#To sort the values in desc order
nums = [5, 2, 9, 1, 7, 2, 5]
nums.sort(reverse=True)
print(nums)

#Slice the first 3 elements from the list
nums = [5, 2, 9, 1, 7, 2, 5]
sli=nums[0:3]
print(sli)

#Extend the list with ["David", "Eve"]
friends = ["Alice", "Bob", "Charlie"]
friends.append("David")
friends.append("Eve")
print(friends)

#Check if "Alice" is present in the list
friends = ["Alice", "Bob", "Charlie"]
friends1=friends
print(friends1)
for i in friends1:
    if i=="Alice":
     print("Alice present")

# Find the total number of friends in the copied list.
friends = ["Alice", "Bob", "Charlie"]
friends1=friends
print(len(friends1))

