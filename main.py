import random

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


def decode_alphabet():
    decoded_alphabet = {}
    alphabet = get_alphabet()
    decode = {
        '00': '10', '01': '22', '02': '17', '03': '07', '04': '15',
        '05': '19', '06': '01', '07': '13', '08': '20', '09': '26',
        '10': '03', '11': '14', '12': '25', '13': '04', '14': '09',
        '15': '05', '16': '02', '17': '24', '18': '21', '19': '06',
        '20': '00', '21': '08', '22': '23', '23': '12', '24': '16',
        '25': '11', '26': '18'

    }
    for key in decode:
        decoded_alphabet[key] = alphabet[decode[key]]

    return decoded_alphabet


def pretty_print(array):
    print('#' * (len(array[0])+4))

    for i in array:
        print('#', end=' ')

        for j in i:
            print(j, end='')

        print(' #', end=' \n')

    print('#' * (len(array[0])+4), end="\n\n")


def find_index(array, needle):
    row = -1
    col = -1
    for i in range(len(array)):
        for j in range(len(array[i])):
            if needle == array[i][j]:
                row = i
                col = j

    return [row, col]


def add_diff_to_list(list1, list2):
    diff = len(list1) - len(list2)
    elements = ['-', '.', '~']

    for i in range(diff):
        list2.append(random.choice(elements))


def get_element_by_index(column, array_list):
    res = ''
    for i in array_list:
        if i == array_list[0] or i == array_list[1]:
            continue
        res += i[column]
    res += ' '

    return res


def task1():
    result = ''
    name = 'KOZHUKHOVSKY'
    new_table = decode_alphabet()
    alphabet = get_alphabet()
    key_list = list(alphabet.keys())
    val_list = list(alphabet.values())

    for letter in name:
        result += new_table[key_list[val_list.index(letter)]]

    print('Input: {}'.format(name))
    print('Result: {}'.format(result))


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

    print('Input: {}'.format(name))
    print('Result: {}'.format(result))


def task3():
    result = ''
    name = 'KOZHUKHOVSKY'
    public_key = 'BITCOIN'
    alphabet = get_alphabet()
    power = len(alphabet)
    list_keys = list(alphabet.keys())
    list_values = list(alphabet.values())

    if int(len(name) / len(public_key)) <= 2:
        public_key = public_key * 2
    else:
        public_key = public_key * int(len(name) / len(public_key))

    for i in range(len(name)):
        num1 = list_keys[list_values.index(name[i])]
        num2 = list_keys[list_values.index(public_key[i])]

        new_key = int(num1) + int(num2)

        if new_key > power:
            new_key = new_key - power
            new_key = new_key if new_key > 9 else '0{}'.format(new_key)
        elif new_key < power:
            new_key = new_key if new_key > 9 else '0{}'.format(new_key)

        result += list_values[list_keys.index(str(new_key))]

    print('Input: {}'.format(name))
    print('Result: {}'.format(result))


def task4():
    result = ''
    matrix = []
    tmp = []
    index = 0
    name = 'KOZHUKHOVSKY' if len('KOZHUKHOVSKY') % 2 == 0 else 'KOZHUKHOVSKY' + '.'
    decoded_alphabet = decode_alphabet()
    values = list(decoded_alphabet.values())
    values = values[:4] + ['.'] + values[4:14] + [','] + values[14:19] + ['-'] + values[19:]

    # заполняем матрицу
    for i in range(len(values)):
        if i + 1 == len(values):
            tmp.append(values[i])
            matrix.append(tmp)
            tmp = []
            break
        if i != 0 and i % 5 == 0:
            matrix.append(tmp)
            tmp = []
        tmp.append(values[i])

    while index < len(name):
        a = find_index(matrix, name[index])
        b = find_index(matrix, name[index + 1])

        # если вдруго задали символ, которого нет в матрице
        if a[0] == -1 or b[0] == -1 or a[1] == -1 or b[1] == -1:
            result = 'Symbol do not exist in the search alphabet'
            break

        # если в одной колонке
        if a[0] == b[0]:
            if a[0] == len(matrix[0]):
                result += matrix[a[0]][0]
            else:
                result += matrix[a[0]][a[1] + 1]

            if b[0] == len(matrix[0]):
                result += matrix[b[0]][0]
            else:
                result += matrix[b[0]][b[1] + 1]

        # если в одном ряду
        elif a[1] == b[1]:
            if a[0] == len(matrix):
                result += matrix[0][a[1]]
            else:
                result += matrix[a[0] + 1][a[1]]

            if b[0] == len(matrix):
                result += matrix[0][b[1]]
            else:
                result += matrix[b[0] + 1][b[1]]

        # если в разных рядах и колонках
        else:
            result += matrix[a[0]][b[1]]
            result += matrix[b[0]][a[1]]

        index += 2

    pretty_print(matrix)
    print('Input: {}'.format(name))
    print('Result: {}'.format(result))


def task5():
    public_key = 'FOREVER'
    clone_key = ''.join(sorted(public_key))
    shifr = 'KOZHUKHOVSKY YAROSLAV АLEKSANDROVICH'
    number_shifr = ''
    result = ''
    key_dictionary = {}
    matrix = []

    # создаем ключь значение для публичного ключа
    for i in range(len(clone_key)):
        key_dictionary[i+1] = clone_key[i]

    keys = list(key_dictionary.keys())
    values = list(key_dictionary.values())

    # создаем нумерованный ключь
    for i in public_key:
        number_shifr += str(keys[values.index(i)])
        keys.remove(keys[values.index(i)])
        values.remove(values[values.index(i)])

    matrix.append(list(public_key))
    matrix.append(list(number_shifr))

    # создаем матрицу
    tmp = []
    shifr = shifr.replace(' ', '')

    for i in range(len(shifr)):
        if i + 1 == len(shifr):
            tmp.append(shifr[i])

            # если не хватает символов в последнем кортеже
            if len(shifr) > len(tmp):
                add_diff_to_list(public_key, tmp)
            matrix.append(tmp)
            tmp = []
            break
        if i != 0 and i % len(public_key) == 0:
            matrix.append(tmp)
            tmp = []
        tmp.append(shifr[i])

    for i in list(key_dictionary.keys()):
        index = find_index(matrix, str(i))
        result += get_element_by_index(index[1], matrix)

    pretty_print(matrix)
    print('Input: {}'.format(shifr))
    print('Result: {}'.format(result))


def info():
    print('\n##########################')
    print('#      Command list        #')
    print('#       [task1 - 1]        #')
    print('#       [task2 - 2]        #')
    print('#       [task3 - 3]        #')
    print('#       [task4 - 4]        #')
    print('#       [task5 - 5]        #')
    print('#       [info - i]         #')
    print('#       [q - exit]         #')
    print('##########################\n')


info()


def get_command():
    global command
    command = (input('Select option \n')).lower().strip()


if __name__ == '__main__':
    while command != 'q':
        if command == 'i':
            info()
        elif command == '1':
            task1()
        elif command == '2':
            task2()
        elif command == '3':
            task3()
        elif command == '4':
            task4()
        elif command == '5':
            task5()
        get_command()
