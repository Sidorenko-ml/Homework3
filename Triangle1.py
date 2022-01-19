n = 4
class NonNumericError(Exception):
    pass
class InconsistentdataError(Exception):
    pass
try:
    a = [int(input("Введите значения катетов А:")) for item in range(n)]
    b = [int(input("Введите значения катетов Б:")) for item in range(n)]
except ValueError:
    raise NonNumericError
if a and b == str:
    raise NonNumericError
if len(a) or len(b) != 4:
        raise InconsistentdataError
katA = [item**2 for item in a]
katB = [item**2 for item in b]
c = [(katA[0]+katB[0])**0.5, (katA[1]+katB[1])**0.5, (katA[2]+katB[2])**0.5, (katA[3]+katB[3])**0.5]
S1 = (a[0] * b[0])/2
S2 = (a[1] * b[1])/2
S3 = (a[2] * b[2])/2
S4 = (a[3] * b[3])/2
print(f'Треугольник 1 с катетами {a[0]} и {b[0]} имеет гипотенузу {c[0]} и площадь {S1}')
print(f'Треугольник 2 с катетами {a[1]} и {b[1]} имеет гипотенузу {c[1]} и площадь {S2}')
print(f'Треугольник 3 с катетами {a[2]} и {b[2]} имеет гипотенузу {c[2]} и площадь {S3}')
print(f'Треугольник 4 с катетами {a[3]} и {b[3]} имеет гипотенузу {c[3]} и площадь {S4}')