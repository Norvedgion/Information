from math import *

def task1():
  pass


x = float(input("введи значение x: "))
y = float(input())
z = float(input())

a1=log1p(sqrt(abs(x-1)+1))+sqrt(abs(y))
a2=sqrt(x**2+x)+sin(y)*cos(x)
a=a1/a2
b=sqrt(x)-(abs(z))**(1/4)+4*x-log2(z)

print('a=',a)
print('b=',b)

from math import *
def task1():
    print('введите значение x')
    x=float(input())
    a = -3
    b = 2
    c = 1
    t1=(b*x**2+a)**2
    t2=c+x**3
    t=t1/t2-x**4
    print(t)


def task2():
    print('введите значение x')
    x=float(input())
    a=(tan(x))**3*(abs(log1p(x**3)))
    print(a)
