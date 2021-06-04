a = input("Enter a proizvolnoiy number ")
b = input("Enter a border number ")
if b>a:
    print("Произвольное число меньше пограничного")
elif b * 3 < a:
    print("Произвольное число больше пограничного в 3 раза")
elif b<a:
    print("Произвольное число больше пограничного")
else:
    print("Произвольное число равно пограничному")
