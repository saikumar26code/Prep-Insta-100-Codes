n=int(input())
num=n
sum=0
while n!=0:
    rem=n%10
    sum+=rem
    n=n//10
if num%sum==0:84
    print("yes")
else:
    print("no")