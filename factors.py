n=int(input())
if n%2==0:
    res=[n//2]
else:
    res=[]
for i in range(1,n//2):
    if n%i==0:
        res.append(i)
print(res)