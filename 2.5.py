print("ВНИМАНИЕ А > B")
A=int(input("Введите A: "))
B = int(input("Введите B: "))
if A>B:
    M = A % B
    print(f'Длина незанятой части отрезка A: {M} ')
else:
    print("А должно быть больше В")