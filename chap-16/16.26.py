# Given an arithmetic equation consisting of positive integers, +, -, * and / (no parentheses) compute
# the result.

def calculator(equation):
    equation = list(equation)
    integers, operators = parse_equation(equation)
    integers, operators = solve_priority(integers, operators)
    return solve_rest(integers, operators)

def solve_rest(integers, operators):
    for _ in range(len(operators)):
        i = integers.pop(0)
        j = integers.pop(0)
        operator = operators.pop(0)
        if operator == '+':
            integers.insert(0, (i + j))
        else:
            integers.insert(0, (i - j))
    return integers[0]

def solve_priority(integers, operators):
    for _ in range(len(operators)):
        i = integers.pop(0)
        operator = operators.pop(0)
        if operator == '+' or operator == '-':
            integers.append(i)
            operators.append(operator)
        else:
            j = integers.pop(0)
            if operator == '*':
                integers.insert(0, (i * j))
            else:
                integers.insert(0, (i / j))
    return integers, operators

def parse_equation(equation):
    integers = list()
    operators = list()
    number = list()
    for i in equation:
        if i == '+' or i == '-' or i == '*' or i == '/':
            operators.append(i)
            if len(number) > 0:
                integers.append(int(''.join(number)))
                number = list()
        else:
            number.append(i)
    integers.append(int(''.join(number)))
    return integers, operators

        
if __name__ == "__main__":
    equation = '2*3+5/6*3+15'
    print(calculator(equation))

