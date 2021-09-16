n=int(input("Enter the number: "))
i,sum=1,0
while i<n:
    if(n%i==0):
        sum=sum+i
    i=i+1
if(sum==n):
    print("Perfect number!")
else:
    print("Not Perfect number!")