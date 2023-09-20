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
