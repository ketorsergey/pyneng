username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')



while True:
    if len(password) < 8:
        print('Пароль слишком короткий')
    elif username in password:
        print('Пароль содержит имя пользователя ')
    else:
        print('Пароль для пользователя {} установлен '.format(username))
        break
        password = input('Введите пароль еще раз: ')

