
def fact(n):
    sum=1
    for i in range(1,n+1):
        sum=sum*i
    return sum
def strongnum(num):
    res=0
    number=num
    while num!=0:
        rem=num%10
        res=res+fact(rem)
        num=num//10
    if res==number:
        return "yes"
    return "no"
n=int(input())
print(strongnum(n))