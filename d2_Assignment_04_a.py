n=int(input("Enter the number: "))
n1=n2=n
i,rem,sum=0,0,0
while n1>0:
    i=i+1
    n1=n1//10
while n2>0:
    rem=n2%10
    sum=sum+rem**i
    n2=n2//10
if(sum==n):
    print("The given number is an armstrong number!")
else:
    print("The given number is not an armstrong number!")