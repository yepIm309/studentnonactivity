slova1 = set(input("Введите слова через запятую (без пробелов): ").split(','))

kolvo = len(slova1)
print("Количество слов в списке: ", kolvo)

slova2 = set(input("Введите второй список слов с таким же количеством: ").split(','))
if len(slova1)==len(slova2):
    dictionary = dict(zip(slova1, slova2))
    print(dictionary)
else:
    print("Ошибка!")