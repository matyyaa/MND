import random

# довільно вибрані коефіцієнти
a0, a1, a2, a3 = 3, 4, 2, 3

# сгенеровані списки для х1, х2, х3
x1 = [random.randrange(1, 20) for i in range(8)]
x2 = [random.randrange(1, 20) for i in range(8)]
x3 = [random.randrange(1, 20) for i in range(8)]

max1, max2, max3 = 0, 0, 0

# обчислення у
def y_count(x1, x2, x3):
    return a0 + a1 * x1 + a2 * x2 + a3 * x3

y = [y_count(x1[i], x2[i], x3[i]) for i in range(8)]

# обчислення значень х0
x01 = (max(x1) + min(x1)) / 2
x02 = (max(x2) + min(x2)) / 2
x03 = (max(x3) + min(x3)) / 2

# обчислення інтервалу зміни фактора
dx1 = x01 - min(x1)
dx2 = x02 - min(x2)
dx3 = x03 - min(x3)

# обчислення нормованого значення xn для кожного фактора
xn1 = [(x1[i] - x01)/dx1 for i in range(8)]
xn2 = [(x2[i] - x02)/dx2 for i in range(8)]
xn3 = [(x3[i] - x03)/dx3 for i in range(8)]


# обчислення за критерієм вибору оптимальності
yET = y_count(x01, x02, x03)

k = 100
for i in range(len(y)):
    if y[i] > yET and y[i] < k:
        k = y[i]


# результати
print("Коефіцієнти:\na0 = %s, a1 = %s, a2 = %s, a3 = %s" % (a0, a1, a2, a3))
print("Всі значення X1 = ", x1)
print("Всі значення X2 = ", x2)
print("Всі значення X3 = ", x3)
print("Значення х0: %s %s %s"%(x01, x02, x03))
print("Відповідні значення y:\n", y)
print("Інтервали зміни факторів dx: %s %s %s"%(dx1, dx2,dx3))
print("Нормовані значення xn для кожного фактора:")
print("Xn1:", xn1)
print("Xn2:", xn2)
print("Xn3:", xn3)
print("Еталонне значення у :", yET)
print("Y <-", k)
