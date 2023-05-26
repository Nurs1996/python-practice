def add(a, b):
    return a + b 

def subtracts(a, b):
    return a - b

def multiplies(a, b):
    return a * b

def divides(a, b):
    return a / b 

val1 = float(input("Please enter first number: "))
val2 = float(input("Please enter second number: "))

oper = input("""Please pick what you want to do: 
               + - addition
               - - subtruction
               * - multiplication
               / - division 
               your choice """)

if oper == "+":
    total = add(val1, val2)
    print(total)

elif oper == "-":
    total = subtracts(val1, val2)
    print(total)

elif oper == "*":
    total = multiplies(val1, val2)
    print(total)

elif oper == "/":
   total = divides(val1, val2)
   print(total)

else:
    print("Pick the right choice: ")




