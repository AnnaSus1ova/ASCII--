import pyfiglet
from termcolor import colored
while True:
    msg = input('What do you want to print?:')
    color = input('What color do you want?:')
    valid_color = ['red', 'green', 'yellow', 'blue', 'cyan', 'white']
    if color not in valid_color:
        color = 'white'
    result1 = pyfiglet.figlet_format(msg)
    result2 = colored(result1, color)
    print(result2)

'''
Если выдает ошибку, попробуй в терминале прописать "pip install pyfiglet" и потом "pip install termcolor".
Русский текст программа игнорирует.
Цвет записывать только маленькими буквами.
Чтобы прикратить выполнение: Ctrl + C в консоли.
'''
