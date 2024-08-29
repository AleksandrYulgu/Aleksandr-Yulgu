

def create_short_list(a, n, m): #формирую короткие списки обхода, где а это начальное значение (первая цифра)
    # n это максимально возвожная цифра, m количество цифр в списке
    short_list = list(range(1, m+1))
    for i in range(m):
        if (a > n):
            a = 1
        short_list[i] = a
        a += 1
    return short_list

'''print(create_short_list(3, 15, 8))'''

def long_list(n, m): #создаю список обхода
    string = ''
    way = [1, ]
    a = m
    while True: #работает пока первая цифра списка не станет равной первой цифре начального списка
        short_list = create_short_list(a, n, m) #сформировал короткий списк
        way.append(short_list[0]) #Добавил первую цифру в путь из свормированного короткого списка
        a = short_list[m-1] #меняю значение а на последнюю цифру в коротком списке
        if short_list[0] == 1:
            break
    for el in way: #преобразовываю список в строку
        string += str(el)
    return string



"""print(long_list(5, 4))"""





