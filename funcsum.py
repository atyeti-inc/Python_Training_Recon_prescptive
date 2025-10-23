#func sum

def sum_all(numbers):
	return sum(numbers)

#exception    
class invalid(Exception):
    pass
	
# Input
num_in = input("Input numbers seperated by , : ")

#exception block
if ',' not in num_in:
    print('Error : Please use comma seperator')

# convert input to a list
num_list = [int(num) for num in num_in.split(',')]
#num_list =  [num_in.split(',')]

#call 

result = sum_all(num_list)
print("sum of all numbers is :", result)



