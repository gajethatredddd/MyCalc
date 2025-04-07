print("Найдем сумму, разность, произведение и частное их квадратов")

a = float(input("Введите значение а: "))
while True:
    try:
        if a <= 0 :
            print("Введите число больше нуля")
            exit()
        else:
            break
    except:
        raise ValueError

b = float(input("Введите значение b: "))
while True:
    try:
        if b <= 0 :
            print("Введите число больше нуля")
            exit()
        else:
            break
    except:
        raise ValueError

Summa = a + b
Minus = a - b
Proizv = a * b
Chastnoe = round(a**2 / b**2,2)

print(f'Сумма: {Summa}\nРазность: {Minus}\nПроизведение: {Proizv}\nЧастное их квадратов: {Chastnoe}')

