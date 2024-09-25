import art
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def divide(n1,n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2

operations={
    "+":add,
    "-":subtract,
    "/":divide,
    "*":multiply
}
print(art.logo)
new_calc=True
while new_calc:
    num_1=float(input("What is the first number?: "))
    current_calc=True
    output=0
    while current_calc:
        for each in operations:
            print(each)
        operation=input("Pick an operation: ")
        num_2=float(input("What is the next number?: "))
        output=operations[operation](num_1,num_2)
        print(f"{num_1} {operation} {num_2} = {output}")
        continue_calc=input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ").lower()
        if continue_calc=='n':
            current_calc=False
        if continue_calc=='y':
            num_1=output

