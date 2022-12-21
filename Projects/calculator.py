print('''
        + ADD
        - Substraction
        * multiply
        / division
        
''')
num1=int(input("Enter the 1st value "))
num2=int(input("Enter the 2nd value "))
opr=input("Enter the operation ...")
if opr=="+":
    print(num1,"+",num2,"=",num1+num2)
elif opr=="-":
    print(num1,"-",num2,"=",num1-num2)
elif opr=="*":
    print(num1,"*",num2,"=",num1*num2)    
elif opr=="/":
    print(num1,"/",num2,"=",num1/num2) 
else:
    print("Enter the correct operations")       