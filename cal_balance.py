#calculate balance

op_bal = 1000
cl_bal = 1150
tran = [200,-100,300,-50,-200]
net = 0

for amt in tran:
	net += amt
	break

Sop_bal = net+op_bal

if Sop_bal == cl_bal:
	print("Balance Matched",Sop_bal, "is equal to", cl_bal)
	
	
else:
	print("Balance mismatched found ",Sop_bal, "is equal no to", cl_bal)
	