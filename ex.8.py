print("Найдем среднее арифметическое")
print("Через пробел введите 2 числа в формате a b: ")
a,b=[int(s) for s in input().split()]
Sr=(a + b)//2
print(f'Среднее арифметическое:{Sr}')