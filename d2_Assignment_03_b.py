n=int(input("Enter the number: "))
c=0 
i=1
if n>1:
    while(i<=n):
        if(n%i==0):
            c=c+1
        i=i+1
    if(c==2):
        print("The given number is a prime number!")
    else:
        print("The given number is not a prime number!")
else:
    print("Wrong Input!")
