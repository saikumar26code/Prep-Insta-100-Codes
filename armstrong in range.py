low=200
high=1000
res=[]
for num in range(low,high+1):
    l=len(str(num))
    number=num
    sum=0
    while num!=0:
        rem=num%10
        sum+=(rem**l)
        num=num//10
    if sum==number:
        res.append(sum)
print(res)