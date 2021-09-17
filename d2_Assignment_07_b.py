n1=int(input("Enter the lower limit: "))
n2=int(input("Enter the uper limit: "))
i=n1
print("The numbers are: ")
while i<=n2:
    j=1
    c=0
    while j<=i:
        if (i%j==0):
            c=c+1
        j=j+1
    if (c==2):
        print(i,end=" ")
    i=i+1