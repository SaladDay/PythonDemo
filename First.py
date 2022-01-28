myBytes=eval(input())
v=int.from_bytes(myBytes,'little')
ans=[]
for i in range(8):
    tmp=True if v & (0x01<<i) else False
    ans.append(tmp)
print(ans)