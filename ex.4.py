print("Найдем длину окружности")
d = float(input("Введите диаметр: "))
while True:
    try:
        if d <= 0 :
            print("Введите число больше нуля")
            exit()
        else:
            break
    except:
        raise ValueError

p: float = 3.14
L = p*d
BB = "%.2f" % L
print(f'Длинна окружности:{BB}')