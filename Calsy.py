import sys
operator= 0
Userproblem=str(sys.argv[1])
if'+'in Userproblem:
    operator= '+'
    numbers=Userproblem.split("+")
elif'-' in Userproblem:
    operator='-'
    numbers=Userproblem.split("-")
elif '*' in Userproblem:
    operator='*'
    numbers=Userproblem.split("*")
elif'/'in Userproblem:
    operator='/'  
    numbers=Userproblem.split("/")
elif'%'in Userproblem:
    operator='%'  
    numbers=Userproblem.split("%")
else:
    print("please give correct operator")  

if 'operator' in locals():
    number1 = int(numbers[0])
    number2 = int(numbers[1])
if operator== '+':
      print("result=",number1 + number2)
elif operator=='-':
      print("result=",number1 - number2)
elif operator == '*':
      print("result=",number1 * number2)
elif operator == '/':
      print("result=",number1 / number2)
elif operator == '%':
      print("result=",number1 % number2)
 







