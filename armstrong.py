n=int(input())
number=n
sum=0
l=len(str(number))
while n!=0:
    rem=n%10
    n=n//10
    sum=sum+(rem**l)
if sum==number:
    print("yes")
else:
    print("no")