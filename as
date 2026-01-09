w=int(input("enter your weight:" ))
s=input("Kg or Lbs:" )
if s=="Kg":
conversion = w * 2.25
print("weight in Lbs: " + str(conversion))
else:
conversion = w / 2.25
print("weight in kg: " + str(conversion))
