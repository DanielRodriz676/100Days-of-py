from art import logo

print(logo)

def soma(n1, n2):
    return n1 + n2

def subt(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

f_numb = 0
result = 0

while True:
    if f_numb == 0:
        f_numb = int(input("What's the first number?: "))
    print('+\n-\n*\n/')
    operator = input('Pick an operation: ')
    s_numb = int(input("What's the next number?: "))
    if operator == '+':
        result = soma(f_numb, s_numb)
    elif operator == '-':
        result = subt(f_numb, s_numb)
    elif operator == '*':
        result = mult(f_numb, s_numb)
    elif operator == '/':
        result = div(f_numb, s_numb)

    print(f"{f_numb} {operator} {s_numb} = {result}")

    cont_numb = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if cont_numb == 'y':
        f_numb = result
    else:
        f_numb = 0