
slovar = {
    "имя": "Иван",
    "возраст": 30,
    "пол": "мужской",
    "рост": 175,
    "вес": 70,

}

for key, value in slovar.items():
    print(f"{key.capitalize()}: {value}")
print()
print()
slovar["размер ноги"] = 42

for key, value in slovar.items():
    print(f"{key.capitalize()}: {value}")

del slovar["возраст"]
print()
print()
for key, value in slovar.items():
    print(f"{key.capitalize()}: {value}")
