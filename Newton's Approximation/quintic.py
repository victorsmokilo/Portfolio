

from time import sleep

x5 = float(input('x^5 value: '))
x4 = float(input('x^4 value: '))
x3 = float(input('x^3 value: '))
x2 = float(input('x^2 value: '))
x1 = float(input('x^1 value: '))
x0 = float(input('x^0 vakue: '))
x = float(input('Enter guess for x: '))

for i in range(1,11):
    a5 = x5 * x**5
    a4 = x4 * x**4
    a3 = x3 * x**3
    a2 = x2 * x**2
    a1 = x1 * x
    dx5 = x5 * 5 * x**4
    dx4 = x4 * 4 * x**3
    dx3 = x3 * 3 * x**2
    dx2 = x2 * 2 * x
    dx1 = x1
    function = a5 + a4 + a3 + a2 + a1 + x0
    dfunction = dx5 + dx4 + dx3 + dx2 + dx1
    x = x - function / dfunction



print(x)

sleep(5)