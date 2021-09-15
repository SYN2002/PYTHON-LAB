score=int(input("Enter thr percentage: "))
if(score>90):
    print("Grade is 'O'")
elif(score>80 and score<=90):
    print("Grade is 'A'")
elif(score>70 and score<=80):
    print("Grade is 'B'")
elif(score>60 and score<=70):
    print("Grade is 'C'")
elif(score>50 and score<=60):
    print("Grade is 'D'")
else:
    print("FAIL!")