from art import logo
import os

print(logo)


def add(a, b):
    """take two number and perform addition"""
    return a + b


def subtract(a, b):
    """take two number and perform subtract"""
    return a - b


def multiply(a, b):
    """take two number and perform multiply"""
    return a * b


def divide(a, b):
    """take two number and perform divide"""
    return a / b


def main():
    flag = True
    num1 = int(input("What is the First Number?"))
    re = num1
    print("+ \n- \n* \n/")
    while flag:
        symbol = input("Pick an operation?")
        num2 = int(input("What is the Next Number?"))
        result = 0
        if symbol == "+":
            result = add(re, num2)
            print(f"{re} + {num2} = {result}")
        elif symbol == "-":
            result = subtract(re, num2)
            print(f"{re} - {num2} = {result}")
        elif symbol == "*":
            result = multiply(re, num2)
            print(f"{re} * {num2} = {result}")
        elif symbol == "/":
            result = divide(re, num2)
            print(f"{re} / {num2} = {result}")
        else:
            print("invalid Symbol")
        re = result
        option = input(f"Type 'y' to continue calculating with {result} or, Type 'n' to perform new calculation \n")
        if option == "n":
            os.system('cls||clear')
            main()
        else:
            flag = True


main()



