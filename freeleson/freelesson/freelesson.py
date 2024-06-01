num1=float(input("enter your number: "))
num2=float(input("enter your number: "))

operation=input("select operation : +,-,*,/ ")

if operation == "+":
    print(num1, "+", num2, "=", num1 + num2)
elif operation == "-":
    print(num1,"-", num2, "=", num1-num2)
elif operation == "*":
    print(num1,"*", num2, "=", num1*num2)    
elif operation == "/":
    if num2 == 0:
        print("you cant divide by 0")
    else:
        print(num1,"/", num2, "=", num1/num2)   
else:
    print("invalid operation")        

