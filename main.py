command = ''


# fio = input('Enter your full name \'FIO\' \n')


def get_alphabet():
    return {
        '00': 'A', '01': 'B', '02': 'C', '03': 'D', '04': 'E',
        '05': 'F', '06': 'G', '07': 'H', '08': 'I', '09': 'J',
        '10': 'K', '11': 'L', '12': 'M', '13': 'N', '14': 'O',
        '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T',
        '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y',
        '25': 'Z', '26': '_'
    }


def task1():
    new_table = {}
    result = ''
    name = 'KOZHUKHOVSKY'
    alphabet = get_alphabet()
    key_list = list(alphabet.keys())
    val_list = list(alphabet.values())
    decode = {
        '00': '10', '01': '22', '02': '17', '03': '07', '04': '15',
        '05': '19', '06': '01', '07': '13', '08': '20', '09': '26',
        '10': '03', '11': '14', '12': '25', '13': '04', '14': '09',
        '15': '05', '16': '02', '17': '24', '18': '21', '19': '06',
        '20': '00', '21': '08', '22': '23', '23': '12', '24': '16',
        '25': '11', '26': '18'

    }

    for key in decode:
        new_table[key] = alphabet[decode[key]]

    for letter in name:
        result += new_table[key_list[val_list.index(letter)]]

    print(result)


def task2():
    new_table = {}
    offset = {}
    result = ''
    offset_values = []
    name = 'KOZHUKHOVSKY'
    pubic_key = 'SLOGAN_'
    alphabet = get_alphabet()
    list_values = list(alphabet.values())

    # записываем ключ в новую таблицу
    for i in range(len(list_values)):
        if i < len(pubic_key):
            new_table[list_values[i]] = pubic_key[i]
        else:
            break

    # список без публичного ключа
    for i in range(len(list_values)):
        if list_values[i] not in pubic_key:
            offset_values.append(list_values[i])

    # список с оффсетом
    for i in range(len(offset_values)):
        offset[list_values[i + len(pubic_key)]] = offset_values[i]

    # комбинируем списки
    new_table.update(offset)

    for letter in name:
        result += new_table[letter]

    print(result)


def task3():
    result = ''
    name = 'KOZHUKHOVSKY'
    public_key = 'BITCOIN'
    alphabet = get_alphabet()
    power = len(alphabet)
    list_keys = list(alphabet.keys())
    list_values = list(alphabet.values())


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
