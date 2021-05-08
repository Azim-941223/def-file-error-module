
while True:
    with open('database.txt', 'a') as f:
        with open('database.txt', 'r') as fk:
            a = int(input("Выберите действие:\n"\
                          "1.Войти \n"\
                          "2.Зарегистрироваться \n"\
                          "3.Выйти \n"))
            if a == 1:
                login = input("Введите логин: ")
                password = input("Введите пароль: ")
                if login in fk.read():
                    print("Вы успешно зашли!")
                else:
                    print("Такой учетнной записи нету в базе")

            if a == 2:
                login = input("Введите логин: ")
                password = input("Введите пароль: ")
                rep_pass = input("Повтарите пароль: ")

                if login not in fk.read() and password == rep_pass:
                    f.write(f"Логин {login} Пароль {password}\n")
                else:
                    print("Такая учетка существует или неверно повторили пароль")

            if a == 3:
                break