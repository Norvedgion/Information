from math import *

# задание1
'''
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
'''

#задание2

def task2():
    print('Введите значение a:')
    a = float(input())
    print('Введите значение b:')
    b = float(input())
    x =[a]
    h = abs(a-b)/10
    f = []
    i = 0
    while len(x) <= 10:
        if x[i]<0:
            c =tan(x[i])-10
            f.append(c)
        else:
            d = x[i]-exp(x[i]**2)
            f.append(d)
        x.append(x[i]+h)
        i+=1
    print(x,f)


# задние3

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
'''


#задание4
'''
def task4():
    y = float(input());
    x = float(input());
    one = (y>= -3*x-30) and (y<= 5*x+42) and (y<= -1*x) and (x<=-6) and (y>= 4*x+26)
    two = (y<= -8/3*x-10) and (y>= 1/5*x-14/5) and (x>= -6) and (x<= -3)
    three = (y<= 1/5*x-8/3) and (y<= 4*x+10) and (y<= -5*x-8) and (x>= -3)

    four = (y<= 3/2*x+11/2) and (y<= -1/2*x+15/2) and (y>= 10*x-24) and (y>= -6*x-2) and (y>= -2)
    five = (y<= -4) and (y>= 1*x-9) and (y>= -1/4*x-13/2) and (y<= 2*x-2)
    six = (y>= -4) and (y<= -2) and (y<= 2*x-2)  and (y>= 10*x-24)
    figure1 = one or two or three
    figure2 = four or five or six

    if figure1:
        print("Точка находится в области первой фигуры.")
    elif figure2:
        print("Точка находится в области второй фигуры.")
    else:
        print("Точка не попадает в область ни одной из фигур.")

task4()
'''

# задание 5
'''
def найти_мин_макс_абсолютные(число1, число2, число3):
    абс1 = abs(число1)
    абс2 = abs(число2)
    абс3 = abs(число3)

    минимальное_абсолютное = min(абс1, абс2, абс3)
    максимальное_абсолютное = max(абс1, абс2, абс3)

    return минимальное_абсолютное, максимальное_абсолютное

число1 = float(input("Введите первое число: "))
число2 = float(input("Введите второе число: "))
число3 = float(input("Введите третье число: "))

мин_абс, макс_абс = найти_мин_макс_абсолютные(число1, число2, число3)
print(f"Наименьшее абсолютное значение: {мин_абс}")
print(f"Наибольшее абсолютное значение: {макс_абс}")
'''

#задание6
'''
def is_happy(number):

    if 0 <= number <= 999999:

        цифры = [int(digit) for digit in str(number)]


        сумма_первых_трех = sum(цифры[:3])
        сумма_последних_трех = sum(цифры[3:])

        return сумма_первых_трех == сумма_последних_трех
    else:
       
        return False
номер_билета = int(input("Введите номер билета (от 000000 до 999999): "))
результат = is_happy(номер_билета)

print(f"Билет счастливый: {результат}")
'''

#задание8
'''
def вычислить_сумму_последовательности(i, x, n):
    # Функция для вычисления i-го члена последовательности
    return i * (x ** (n + 2 - i))

def сумма_последовательности(x, n):
    # Инициализируем сумму
    сумма = 0

    # Вычисляем и добавляем каждый член последовательности к сумме
    for i in range(n + 2, 0, -1):
        член = вычислить_сумму_последовательности(i, x, n)
        сумма += член
        print(f"Член {i}: {член}, текущая сумма: {сумма}")

    return сумма

x = float(input("Введите значение x: "))
n = int(input("Введите значение n: "))

результат = сумма_последовательности(x, n)

#задание9

#задание9
def task9():
    current_sum = 0
    for i in range(1, 9):
        for j in range(1,i+1):
            current_sum += (j ** 2)
    print(current_sum)
task9()


def task92():
    current_sum = 0
    for i in range(1, 9):
        current_pr = 1
        for j in range(1, i+1):
            current_pr *=(j + i) * (j - i)
        current_sum+=current_pr
    print(current_sum)
task92()


def task93():
    current_sum = 0
    for i in range(1, 9):
        for j in range(1, i+1):
            for k in range(1, (i+j)+1):
                current_sum += (j**2 + i + k)
    print(current_sum)
task93()

#задание10
def koren(y: float, x: float, p: float) -> float:
    EXP = 1e-6  # точность вычислений
    while True:
        y_next = (1/p) * ((p-1) * y + (x / (y ** (p-1))))
        if abs(y_next - y) <= EXP:
            return y_next
        y = y_next

x = float(input("Введите число x: "))
p = float(input("Введите степень p: "))

y = math.exp(math.log(x * (p + 1)) / p) 
root = koren(y, x, p)

print(f"Корень {p}-й степени числа {x} равен {root}")
'''
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if x >= 0:
        return 2*(x**2 - 5) - x
    else:
        return np.tan(x) - 10

a = -3  # Начальное значение диапазона x
b = 3  # Конечное значение диапазона x

x = np.linspace(a, b, 100)  # Генерируем 100 равномерно распределенных значений x в диапазоне [a, b]
y = np.vectorize(f)(x)  # Применяем функцию f к каждому значению x

plt.plot(x, y)  # Построение графика
plt.xlabel('x')  # Название оси x
plt.ylabel('f(x)')  # Название оси y
plt.title('График функции f(x)')  # Заголовок графика
plt.grid(True)  # Включение сетки
plt.show()  # Отображение графика


