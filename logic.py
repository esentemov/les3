role = input("Введите вашу роль в проекте: ")
age = input("Введите ваш возраст ")
age = int(age)


if role == "admin" and age > 18:
    print("Добро пожаловать с полными правами")
elif role == "user" and age > 14:
    print("У вас есть некоторые права в этом проекте")
elif role != "admin" or role != "user" or age < 15:
    print("Чат закрыт на карантин")
