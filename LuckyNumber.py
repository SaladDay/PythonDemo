sName=input("Please enter your English name.")
sName=sName.strip().lower()
luckyNumber=0
for x in sName:
    v=ord(x)-ord('a')+1
    luckyNumber+= v
    print("value of",x,"=",v)
print("Your luckyNumber is ",luckyNumber)