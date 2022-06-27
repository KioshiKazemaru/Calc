from colorama import init
from colorama import  Fore, Back, Style

init()


what = str()
while what != '0':
    #Цвета
    print(Fore.BLACK)
    print(Back.GREEN)
    #Чё нам надо?
    what = input("Что делаем? (+, -, *, Закрыть - 0): ")
    if what == '0' :
        break
    print(Back.CYAN)
    a = float( input("Веди первое число: "))
    b = float( input("Веди второе число: "))

    print(Back.YELLOW)
#Вычисления
    if what == '+' :
        c = a + b
        print("Результат: " + str(c))
    elif what == '-' :
        c = a - b
        print("Результат:" + str(c))
    elif what == '*' :
        c = a * b
        print("Результат: " + str(c))
    elif what != '*' or '-' or '+' :
        print ("Выбрана неверная операция")

    input()
