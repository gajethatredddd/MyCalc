print("Найдем площадь и периметр прямоугольника")
a = int(input("Введите значение а: "))


while True:
    try:
        if a <= 0 :
            print("Введите число больше нуля")
            exit()
        else:
            break
    except:
        raise ValueError

b = int(input("Введите значение b: "))
while True:
    try:
        if b <= 0 :
            print("Введите число больше нуля")
            exit()
        else:
            break
    except:
        raise ValueError

S = a*b
P = 2*(a + b)
print(f'Площадь:{S}\nПериметр:{P}')