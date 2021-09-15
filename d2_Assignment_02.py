num=int(input("Enter the number: "))

if(num%4==0):
    if(num%7==0):
        print("The given number is divisable by both 4 and 7")
    else:
        print("The given number is divisable by 4 but not by 7")
elif(num%7==0):
    if(num%4==0):
        print("The given number is divisable by both 4 and 7")
    else:
        print("The given number is divisable by 7 but not by 4")
else:
    print("The given number is neither divisable by 4 nor 7")