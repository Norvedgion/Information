def prostoe(a):
    if a <= 1:
        return False
    for i in range(2, int (a**0.5)+1):
        if a % i == 0:
            return False
    return True

def nadva(b):
    if b % 2 == 0:
        return True
    else:
        return False

def task1():
    while True:
        print("Введите число")
        x=float(input())
        if prostoe(x):
            print("Число простое")
        else:
            print("Число НЕ простое")
        if nadva(x):
            print("Число делится на два")
        else:
            print("Число НЕ делится на два")
task1()

from math import *
def prostoe(number1):
    if number1 % number1 % 1:
        number1 = 0
    else:
        number = 1
        return number1

def divide(number1):
    if number1 % 2:
        number1 = 0
    else:
        number1 = 1
        return number1

def task1():
    b=int(input("Введите число "))
    if prostoe(b) == 0:
        print('простое')
    if divide (b) == 0:
        print('Делится на 2')

task1()

def number_in_new_numeral_system(number, base):
    result = ""
    while number > 0:
        remainder = int(number % base)
        result = str(remainder) + result
        number //= base
    return result if result else "0"
desimal_number = float(input("Введите целое десятичное число:"))
new_base = float(input("Введите основание новой системы счисления:"))
result_in_new_base = number_in_new_numeral_system(desimal_number, new_base)
print(f"Число{desimal_number} в {new_base}- иной системе: {result_in_new_base}")


