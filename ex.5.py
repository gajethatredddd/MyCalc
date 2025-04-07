print("Найдем объем куба и площадь его поверхности")

a = int(input("Введите длину ребра: "))
while True:
    try:
        if a <= 0 :
            print("Введите число больше нуля")
            exit()
        else:
            break
    except:
        raise ValueError
V = a^3
S = 6*a^2
print(f'Объем куба:{V}\nПлощадь его поверхности:{S}')
