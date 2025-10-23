#transaction_list

bank = [100,200,300,400,500]
custodian = [100,200,250,400,600]

Diff = list(set(bank)-set(custodian))
print(Diff, "is not available in custodian")

unique = set(bank+custodian)
print("unique transaction from ban and custodian are", unique)

set1 = set(bank)
set2 = set(custodian)

unrecon = set1.symmetric_difference(set2)
print(list(unrecon), "are unreconciled items from bank and custodian")