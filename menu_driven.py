while True:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        print("Addition: ",num1+num2)
    elif choice==2:
        print("Subtraction: ",num1-num2)
    elif choice==3:
        print("Multiplication: ",num1*num2)
    elif choice==4:
        print("Division: ",num1/num2)
    else:
        print("Invalid Choice")    
    ans=input1=input("Do you want to continue(y/n): ")    
    ans=ans.lower()
    if ans=='n':
        break            