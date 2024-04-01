n=int(input())
sq=n**2
mod=10**len(str(n))
if sq%mod==n:
    print("yes")
else:
    print("no")