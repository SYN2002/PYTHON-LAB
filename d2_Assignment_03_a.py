n=int(input("Enter the number: "))
c=0
if n>1:
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        print("The given number is a prime number!")
    else:
        print("The given number is not a prime number!")
else:
    print("Wrong Input!")
