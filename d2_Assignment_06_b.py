n=int(input("Enter the number: "))
i,sum=1,0
while i<n:
    if(n%i==0):
        sum=sum+i
    i=i+1
if(sum==n):
    print(n,"is a perfect number!")
else:
    print(n,"is not Perfect number!")