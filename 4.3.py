spisok = ["a", "s", 1, "a", 32, 23]
numbers = []
letters = []

for item in spisok:
    if isinstance(item,int):
        numbers.append(item)
    elif isinstance(item,str):
        letters.append(item)
print("Цифры: ", numbers)
print("Буквы: ", letters)