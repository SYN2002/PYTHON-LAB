num=int(input("Enter the number: "))

if(num%3==0):
    if(num%7==0):
        print("The given number is divisable by both 3 and 7")
    else:
        print("The given number is divisable by 3 but not by 7")
elif(num%7==0):
    if(num%3==0):
        print("The given number is divisable by both 3 and 7")
    else:
        print("The given number is divisable by 7 but not by 3")
else:
    print("The given number is neither divisable by 3 nor 7")