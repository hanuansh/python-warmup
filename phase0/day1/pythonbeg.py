while(True):
    print("Calculator:\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Exit")
    ch=int(input("Enter your choice:"))
    if(ch==5):
        break
    a=int(input("Enter operand1:"))
    b=int(input("Enter operand2:"))
    if(ch==1):
        print("Addition is:",a+b)
    elif(ch==2):
        print("Subtraction is:",a-b)
    elif(ch==3):
        print("Multiplication is:",a*b)
    elif(ch==4):
        print("Division is:",int(a/b))
print("Programme ended")