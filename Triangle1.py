from pickle import EXT4


n = 6
class NonNumericError(Exception):
    pass
class InconsistentDataError(Exception):
    pass
try:    
    	k1 = [int(input("Введите для 3-ёх разных треугольников значения катетов А и Б поочерёдно:")) for item in range(n)]
except ValueError:
    raise NonNumericError
if k1 == str:
    raise NonNumericError
if len(k1) != 5:
    raise InconsistentDataError
k2 = [item**2 for item in k1]
c1 = (k1[0] + k1[2])**0.5
c2 = (k1[1] + k1[3])**0.5
c3 = (k1[4] + k1[5])**0.5
S1 = ((k1[0] + k1[2])/2)
S2 = ((k1[1] + k1[3])/2)
S3 = ((k1[4] + k1[5])/2)
print(f'Треугольник 1 с катетами {k1[0]} и {k1[2]} имеет гипотенузу {c1} и площадь {S1}')
print(f'Треугольник 2 с катетами {k1[1]} и {k1[3]} имеет гипотенузу {c2} и площадь {S2}')
print(f'Треугольник 3 с катетами {k1[4]} и {k1[5]} имеет гипотенузу {c3} и площадь {S3}')