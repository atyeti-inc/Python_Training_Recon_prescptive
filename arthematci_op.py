#arthematic_op

def arthematic_op(a,b): 
    cal = {
        'sum': a + b,
        'difference': a - b,
        'product': a * b,
        'quotient': a / b if b != 0 else 'undefined (division by zero)'}
    return cal

in_num = input("Input two numbers giving space : ")
#list_num = list(in_num)	
op_num = [int(num) for num in in_num.split()]
print(op_num)
#result = arthematic_op(op_num)
result = arthematic_op(op_num[0],op_num[1])
print(result)
	
	