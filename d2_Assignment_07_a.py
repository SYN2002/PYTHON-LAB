n1=int(input("Enter the lower limit: "))
n2=int(input("Enter the uper limit: "))
i,j,c=1,0,0
print("The numbers are: ")
for i in range(n1,n2+1):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
    if(c==2):
        print(i,end=" ")