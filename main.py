command = ''
fio = input('Enter your full name \'FIO\' \n')


def task1():
    print('task1')


def task2():
    print('task2')


def task3():
    print('task3')


def task4():
    print('task4')


def task5():
    print('task5')


def info():
    print('\n########################')
    print('#     Command list       #')
    print('#       [task1]          #')
    print('#       [task2]          #')
    print('#       [task3]          #')
    print('#       [task4]          #')
    print('#       [task5]          #')
    print('#       [info]           #')
    print('#      [q] - exit        #')
    print('########################\n')


info()


def get_command():
    global command
    command = (input('Select option \n')).lower().strip()


if __name__ == '__main__':
    while command != 'q':
        if command == 'info':
            info()
        elif command == 'task1':
            task1()
        elif command == 'task2':
            task2()
        elif command == 'task3':
            task3()
        elif command == 'task4':
            task4()
        elif command == 'task5':
            task5()
        get_command()
