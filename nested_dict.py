#Nested Dictionary
#student = {1:{'Name':'Timir','Age':30,'Month':'FEB'}},
#           2:{{'Name':'Nimit','Age':3,'Month':'FEB'}}
#           
#           print(student)


student1 = frozenset({'Name':'Timir','Age':30,'Month':'FEB'}.items())
student2 = frozenset({'Name':'Nimit','Age':3,'Month':'FEB'}.items())
students = {student1, student2}
print(student1.union(student2))
