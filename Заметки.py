import os
import os.path
import shutil
import datetime
import subprocess
import time

os.makedirs('Заметки', exist_ok=True)  # Создаёт папку Заметки, если ее нет, если есть, то исключание не выдаёт


def clear():  # Функция нужна только для того, чтобы запускать в консоли, она очищает экран
    subprocess.run('cls', shell=True)


def file_or_folder(x):  # Определить папка это или файл
    return 'file' if os.path.isfile(x) else 'folder'


def for_folder_forward(x):  # Смена пути 'вперед'
    os.chdir(os.path.join(os.getcwd(), x))


def for_folder_back():  # Смена пути 'назад'
    if os.path.split(os.getcwd())[1] == 'Заметки':
        clear()
        print('-' * 50)
        print('Назад больше нельзя')
        print('-' * 50)
        return
    os.chdir(os.path.split(os.getcwd())[0])


def create_file():  # Создание файла
    print('Введите название заметки')
    name = input()
    if name + '.txt' in os.listdir():
        clear()
        print('-' * 50)
        print('Заметка с таким названием уже существует')
        print('-' * 50)
        return
    print('Введите текст заметки')
    text = input()
    open(name + '.txt', 'a+', encoding='utf-8').write(text)
    clear()
    print('-' * 50)
    print(f'Заметка {name.split('.')[0]} успешно создана')
    print('-' * 50)


def create_folder():  # Создание папки
    try:
        print('Введите название папки')
        name = input()
        os.mkdir(name + ' (Папка)')
        clear()
    except:
        clear()
        print('-' * 50)
        print('Такая папка уже существует')
        print('-' * 50)


def view_content_folder():  # Просмотр содержимого папки
    print(f'Все найденные заметки и папки в каталоге {(os.path.split(os.getcwd())[1]).split()[0]}')
    slovar = {x: y for x, y in enumerate(os.listdir(), 1)}
    return slovar


def view_content_file(file_name, ans):  # Просмотр,редактирование или удаление файла
    if ans == '1':  # Просмотр
        clear()
        print('-' * 50)
        print(open(file_name, 'r', encoding='utf-8').read())
        print('-' * 50)
    if ans == '2':  # Редактирование
        print('Напишите новый текст')
        open(file_name, 'w', encoding='utf-8').write(
            input() + f'\n\nПоследнее время редактирования: {datetime.datetime.today()}')
        clear()
        print('-' * 50)
        print(f'Заметка {file_name} отредактирована')
        print('-' * 50)
    if ans == '3':  # Удаление
        os.remove(file_name)
        clear()
        print('-' * 50)
        print(f'Заметка {file_name} удалена')
        print('-' * 50)
    if ans == '4':
        return ''


def del_papka():  # Удаление папки
    if os.path.split(os.getcwd())[1] == 'Заметки':
        subprocess.run('cls', shell=True)
        print('-' * 50)
        print('Не выбрана папка')
        print('-' * 50)
        return
    papka = os.path.split(os.getcwd())[1]
    os.chdir(os.path.split(os.getcwd())[0])
    shutil.rmtree(papka)
    print('-' * 50)
    print(f'Папка {papka.split()[0]} удалена')
    print('-' * 50)


def choice_answers(option, name_file=0):  # Для сообщений, выводимых в консоль
    options = {
        1: 'Выбери номер, или нажми "x", чтобы создать что то новое, или нажми "y", чтобы вернутся назад, или нажми "d", чтобы удалить папку',
        2: 'Нажми "x", чтобы создать что то новое или нажми "y", чтобы вернутся назад, или нажми "d", чтобы удалить папку',
        3: 'Что ты хочешь создать?\n1) Заметку   2) Папку   3)Назад',
        4: f'Выбери действие с заметкой {name_file}\n1) Прочитать   2) Редактировать   3) Удалить   4) Назад'
    }
    print(options[option])


os.chdir(os.path.join(os.getcwd(), 'Заметки'))

while True:
    content_folder = view_content_folder()

    for x, y in content_folder.items():
        print(f'{x}) {y.split('.')[0]}')

    choice_answers(1) if content_folder else choice_answers(2)

    ans = input()

    try:
        if ans == 'x':
            choice_answers(3)
            ans = input()
            try:
                answer = eval(['create_file()', 'create_folder()'][int(ans) - 1])
            except:
                continue

        elif ans == 'd':
            del_papka()

        elif ans == 'y':
            for_folder_back()

        elif file_or_folder(content_folder[int(ans)]) == 'file':
            choice_answers(4, content_folder[int(ans)].split('.')[0])
            view_content_file(content_folder[int(ans)], input())

        elif file_or_folder(content_folder[int(ans)]) == 'folder':
            for_folder_forward(content_folder[int(ans)])
            time.sleep(1)
            subprocess.run('cls', shell=True)

    except:
        subprocess.run('cls', shell=True)
        print('-' * 50)
        print('Следуйте инструкциям на экране')
        print('-' * 50)
