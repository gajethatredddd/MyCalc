print("Найдем длину окружности и площадь круга заданного радиуса")
R=float(input("Введите радиус: "))
while True:
    try:
        if R <= 0 :
            print("Введите число больше нуля")
            break
        else:
            break
    except:
        raise ValueError

P: float = 3.14
L= 2*P*R
S = P*R*2
L1 = "%.2f" % L
S1 = "%.2f" % S
print(f'Длина окружности: {L1}\nПлощадь круга: {S1}')