
def add(num1,num2):
    return num1+num2
    
def sub(num1,num2):
    return num1-num2
    
def mul(num1,num2):
    return num1*num2
    
def div(num1,num2):
    return num1/num2

num1 = int(input("Enter the first number?: "))
num2 = int(input("Enter the second number?: "))
operations={"+": add,"-": sub,"*": mul,"/": div}
for symbol in operations:
    print(symbol)
operation_symbol=input("pick an operation from the line above: ")
cal_function = operations[operation_symbol]
answer=cal_function(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
 
    