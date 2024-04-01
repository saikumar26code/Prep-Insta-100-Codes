n=28
flag=0
if n<2:
    flag=1
if n==2:
    flag=0
else:
    for i in range(3,(int(n**0.5)+1),2):
        if n%i==0:
            flag=1
            break
if flag==1:
    print("not prime")
else:
    print('prime')