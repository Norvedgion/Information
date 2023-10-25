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





