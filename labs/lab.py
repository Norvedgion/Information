import math
from math import *

def task1():
x = float(input("введи значение x: "))
y = float(input())
z = float(input())
a1=log1p(sqrt(abs(x-1)+1))+sqrt(abs(y))
a2=sqrt(x**2+x)+sin(y)*cos(x)
a=a1/a2
b=sqrt(x)-(abs(z))**(1/4)+4*x-log2(z)
print('a=',a)
print('b=',b)

def task2():
    print('введите значение x')
    x=float(input())
    a = -3
    b = 2
    c = 1
    t1=(b*x**2+a)**2
    t2=c+x**3
    t=t1/t2-x**4
    print(t)

def task3():
    print('введите значение x')
    x=float(input())
    a=(tan(x))**3*(abs(log1p(x**3)))
    print(a) 
    
def task4():
    Sside = float(input("введите площадь боковой поверхности"))
    Vpyramid = float(input("введите объём пирамиды"))
    Sbase = float(input("введите площадь квадратного основания"))
    Hpyramid = (3 * Vpyramid) / Sbase
    Rcilinder = (Sside / (2 * pi * Hpyramid))
    Vsilinder = pi * Rcilinder**2 * Hpyramid
    print(f"Объём цилиндра, {Vsilinder:.4f}")


def task5():
    Money = float(input("введите сколько двое рабочих заработали вместе"))
    Week_1_Working = 2
    Week_2_Working = 4
    Earnings_1 = (Week_1_Working / (Week_1_Working + Week_2_Working )) * Money
    Earnings_2 = (Week_2_Working / (Week_1_Working + Week_2_Working)) * Money
    print(f"Первый рабочий заработал, {Earnings_1:.4f} рублей")
    print(f"Второй рабочий заработал, {Earnings_2:.4f} рублей")

def task6():
        R = float(input("введите радиус нижнего основания"))
        r = float(input("введите радиус верхнего основания"))
        a = float(input("Площадь вертикального сечения"))
        h = 2 * a / (R + r)
        v = (pi * h * (R ** 2 + R * r + r ** 2)) / 3
        print(f"Объём усеченного конуса, {v:.4f}")


def task7():
    x1 = float(input("введите координату x1"))
    x2 = float(input("введите координату x2"))
    dist = abs (x2-x1)
    print(f"расстояние между координатами, {dist:.4f}")


def task8():
    S = float(input("введите путь пройденный телом"))
    t = float(input("введите время"))
    N = float(input("введите увеличение скорости"))
    V = 2 * S / (N * t + t)
    a = (N * V - V) / t
    print(f" ускорение, {a:.4f}")
    print(f" начальная скорость, {V:.4f}")

def task9():
    KZT= float(input("введите сумму в тенге, котрую хотите перевести"))
    commission = 2 / 100
    EUR = KZT / (1977 / 1000000) - commission
    print(f" сумма с учетом комиссии, {EUR:.2f}")
