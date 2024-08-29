while True:
    data = input('Введите координаты точки через пробел или s: ')
    if data != '':
        with open('dot.txt', 'a+') as f:
            f.write(data + '\n')
    else:
        break


def coordinat_point(file):
    f = open(file, 'r')
    coordinat_point = []
    c = []
    lines = 0
    for line in f:
        lines += 1
        c = list(line.split())
        coordinat_point.append(c)
    f.close()
    if lines > 100:
        return ('слишком много точек')
    else:
        return coordinat_point

'''print(coordinat_point('dot.txt'))'''

def coordinat_circle(file):
    f = open(file, 'r')
    coordinat_circle = f.readline().split()
    radius_circle = f.readline().split()
    f.close()
    return coordinat_circle, radius_circle

"""print(coordinat_circle('circle.txt'))"""


def dot_in_circle(x_c, y_c, radius, x_point, y_point):
    if (int(x_c) - int(x_point))*(int(x_c) - int(x_point)) + (int(y_c) - int(y_point))*(int(y_c) - int(y_point)) < int(radius)*int(radius):
        return 0
    elif (int(x_c) - int(x_point))*(int(x_c) - int(x_point)) + (int(y_c) - int(y_point))*(int(y_c) - int(y_point)) == int(radius)*int(radius):
        return 1
    else:
        return 2

'''print(dot_in_circle(1, 1, 5, 1, 6))'''

def main_(file_circle, file_point): #основная функция
    x_c, y_c = coordinat_circle(file_circle)[0]
    r = coordinat_circle(file_circle)[1][0]
    for x_point, y_point in coordinat_point(file_point):
        print(dot_in_circle(x_c, y_c, r, x_point, y_point))


main_('circle.txt', 'dot.txt')