a= {'jack','rose','mike','lucy'}
b = {'adam','brian','nikki','sam','jack','lucy'}
print(a | b)  #total name in both sets a and b
print(a & b)  #common name
print(a-b)  #unique data of a in the combined set of a and b
print(b-a)  #unique data of b in the combined set of a and b


price= [100,120,80,70]
earning_per_share = [9,15,0,6]
#here in the code below, we are returning the actual ration only if the value of e is not 0 otherwise we are returning the value of ratio as -1
pe_ratio = [round(p/e,2) if e!=0 else -1 for p,e in zip(price,earning_per_share)] #here we are rounding off the ratio into .2 decimals
print(pe_ratio)