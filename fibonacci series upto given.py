n=10
if n==1:
    res=[0]
elif n==2:
    res=[0,1]
else:
    n1,n2=0,1
    res=[0,1]
    while (n-2)!=0:
        n3=n1+n2
        res.append(n3)
        n1=n2
        n2=n3
        n=n-1
print(res)
