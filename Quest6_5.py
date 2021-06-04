def makeslovar():
    firstspisok = input('Введите строку 1:').split(",")

    print("Слов в строке:", len(firstspisok))
    secondspisok = input('Введите столько же слов:'.format(len(firstspisok))).split(",")

    if len(secondspisok) != len(firstspisok):

        print("Количество слов не совпадает, словарь будет сделан в соответствии с размером меньшей строки")
    return dict(zip(firstspisok, secondspisok))

print(makeslovar())
