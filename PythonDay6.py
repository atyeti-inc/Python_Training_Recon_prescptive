print('_______________________________________________________')
Fruits={'Apple':100, 'Berry':250, 'Cherry':200}
print(Fruits)

Marks={'Amit':80, 'Shekar':90,'Ravi':98}
print('The Max Percentage from directory is', (max(Marks.values())))

Word_Count={'Python':0, 'Java':0, 'CSS':0}
Sentence='Python is Object oriented language, so is Java. Python is easy to learn'
z=0
print('Before --> word count',Word_Count)

if 'Python' in Sentence:
        z+=1
        Word_Count.update({'Python':z})
if 'Java' in Sentence:
            Word_Count.update({'Java':1})
if 'CSS' in Sentence:
            Word_Count.update({'CSS':1})

print('After --> word count', Word_Count)

lst=['Python','Java','Python','C++','Java']
print('List containing duplicates',lst)

set1=set(lst)
print('Converted into set',set1)

set2={'Student1','Student2', 'Student4','Student5'}
set3={'Student1', 'Student2', 'Student8' ,'Student9'}
print('The following are the common students from given sets,', set2.intersection(set3))


def Greet_user(name):
        print('Hello', name, 'Welcome!')

Greet_user('Hemant')

def SUM_ALL(*numbers):
        sum=0
        for i in numbers:
                sum+=i
        print(sum)

SUM_ALL(1,2,3,4,5)

def Arithmetic_operations(number1, number2):
        Sum=number1+number2
        
        print('The sum of shared numbers is',Sum)
         
        
        Substract=number1-number2
        print('The difference between shared two numbers is', Substract)


        product=number1*number2
        print('The product of the given numbers is', product)


        Quotient=number1/number2
        print('The quotient of the shared two numbers is', Quotient)
Arithmetic_operations(2,4)