
def get_nambers(file):#открываю файл и формирую список для работы
    numbers = []
    nums = []
    with open(file, 'r') as f:
        for line in f:
            numbers.append([int(x) for x in line.split()])
    for i in numbers:
        nums.append(i[0])
    return nums

"""print(get_nambers('data.txt'))"""


def how_step(file):
    num = sorted(get_nambers(file)) #Сортирую список по возростанию
    i = len(num)// 2 #Нахожу индекс среднего значения к нему буду приводить остальные значения
    medium = num[i]
    counter = 0
    for el in num: #перебираю все элементы массива
        if el != medium: #Если значение элемента не равно среднему, то выполняется операция
            counter += el - medium if el > medium else medium - el #плюсую к счетчику количество необходимых ходов для привдения числа к среднему

    return (f'Минимальное количество ходов {counter}')

print(how_step('data.txt'))