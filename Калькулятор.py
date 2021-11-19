from colorama import Fore
print(Fore.CYAN)
c = input('Выберите нужное действие ( +, -, *, :, ** ): ')
if c == '+':
    print('Вы выбрали действие сложение')
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    d = a + b
    print(Fore.BLUE)
    print('Ответ: ' + str(d))
elif c == '-':
    print('Вы выбрали действие вычитание')
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    d = a - b
    print(Fore.BLUE)
    print('Ответ: ' + str(d))
elif c == '*':
    print('Вы выбрали действие умножение')
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    d = a * b
    print(Fore.BLUE)
    print('Ответ: ' + str(d))
elif c == ':':
    print('Вы выбрали действие деление')
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    d = a / b
    print(Fore.BLUE)
    print('Ответ: ' + str(d))
elif c == '**':
    print('Вы выбрали возведение в степень')
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    d = a ** b
    print(Fore.BLUE)
    print('Ответ: ' + str(d))
else:
    print(Fore.RED)
    print('Вы выбрали не верное действие!')

input()
