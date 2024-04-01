low=int(input())
high=int(input())
res=[]
for num in range(low,high+1):
    if num<2:
        pass
    elif num==2 or num==3:
        res.append(num)
    elif num%2==0 or num%3==0:
        continue
    else:
        for i in range(3,(int(num**0.5)+1),2):
            if num%i==0:
                break
        else:
            res.append(num)
print(res)