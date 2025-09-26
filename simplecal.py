#simple calculator
num1=int(input("enter the first numbe"))
operator=input("enter the operator")
num2=int(input("enter your second digit:"))
if operator=='-':
    results=(num1-num2)

elif operator=='+':
    results=num1+num2
elif operator=='*':
    results=num1*num2
elif operator=='/':
    if num2 !=0:
      results=num1/num2
    else:
        print("syntax error!")
elif operator=='%':
    results=num1%num2
else:
    print("void operation")
print("results:",results)