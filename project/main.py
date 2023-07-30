# нам нужно хранить координаты кусочков кубика рубика (x,y,z) и Цвет кусочка со всех сторон(x(color),y(color),z(color))
# хранение и реализация поворотов ребер по одной из 2 направлений (вверх право) (противоположные значения поворотов будут записываться со знаком '-')
# надо выбрать как хранить координаты для каждого уровня кубика 
# (0, 1, 2)
# (3, 4, 5) те хранение
# (6, 7, 8)  


# пример ввода данных
# пользователь вводит 6 сторон по очереди
print('Пример:')
print('Развертка:')
print('        B B R       2')
print('  1---> Y W W     ↙  ')
print('        Y R O   ↙    ')
print('              ↙      ')
print('O O R   G G G   W R W')
print('B G B   Y R B   W B W')
print('Y Y Y   R G W   O W B')
print('↑                   ↑')
print('|       B O B       |')
print('4   5-> G Y O       3')
print('        O R W        ')
print('                     ')
print('        G Y R        ')
print('    6-> O O G        ')
print('        Y R G        ')


trash = input('Как поймете нажмите ENTER: ')

print('Для стороны используйте запись цвета через пробел')
print('B B R <--> 1 2 3    ')
print('Y W W <--> 4 5 6 --> B B R Y W W Y R O')
print('Y R O <--> 7 8 9    ')


def from_string_to_array(count): # Функция делает из
    side = input(f'Введите цвета для {count} стороны через пробел -> ').upper().split()
    arr_1 = side[:3]
    arr_2 = side[3:6]
    arr_3 = side[6:]
    return arr_1, arr_2, arr_3



side_1 = from_string_to_array(1) # хранение данных - кортеж из 3 массивов с цветами
side_2 = from_string_to_array(2)
side_3 = from_string_to_array(3)
side_4 = from_string_to_array(4)
side_5 = from_string_to_array(5)
side_6 = from_string_to_array(6)
print(side_1, side_2, side_3, side_4, side_5, side_6)

# кубик рубика имеет 8 подвижных углов (с 3 цветами), 12 подвимжных ребер(с 2 цветами) и 6 центров (с 1 цветом)
# В кубике рубика центры не двигаются 

#angle = (x,y,z и 3 цвета) цвета беруться из сторон
# верхний слой
angle_1 = ('x,y,z', side_1[0][0], side_4[0][0], side_6[2][0]) # ┍ вид сверху
edge_1 = ('x,y,z', side_1[0][1], None, side_6[2][1]) # ┍┑ вид сверху
angle_2 = ('x,y,z', side_1[0][2], side_3[0][2], side_6[2][2]) # ┑ вид сверху ((верх/низ)(лево/право)(перед/зад))

edge_2 = ('x,y,z', side_1[1][0], side_4[0][1], None)
center_1 = ('x,y,z', side_1[1][1], None, None)
edge_3 = ('x,y,z', side_1[1][2], side_3[0][1], None)

angle_3 = ('x,y,z', side_1[2][0], side_4[0][2], side_2[0][0]) # ┕ вид сверху
edge_4 = ('x,y,z', side_1[2][1], None, side_2[0][1])
angle_4 = ('x,y,z', side_1[2][2], side_3[0][0], side_2[0][2]) # ┚ вид сверху


# Средний слой
edge_5 = ('x,y,z', None, side_4[1][0], side_6[1][0])
center_6 = ('x,y,z', None, None,side_6[1][1])
edge_6 = ('x,y,z', None, side_3[1][2], side_6[1][2])

center_4 = ('x,y,z', None, side_4[1][1], None)
# пустота
center_3 = ('x,y,z', None, side_3[1][1], None)

edge_7 = ('x,y,z', None, side_4[1][2], side_2[1][0])
center_2 = ('x,y,z', None, None,side_2[1][1])
edge_8 = ('x,y,z', None, side_3[1][0], side_2[1][2]) 


# Нижний слой
angle_5 = ('x,y,z', side_5[2][0], side_4[2][0], side_6[0][0]) # ((верх/низ)(лево/право)(перед/зад))
edge_9 = ('x,y,z', side_5[2][1], None, side_6[0][1])
angle_6 = ('x,y,z', side_5[2][2], side_3[2][2], side_6[0][2])

edge_10 = ('x,y,z', side_5[1][0], side_4[2][1], None)
center_5 = ('x,y,z', side_5[1][1], None, None)
edge_11 = ('x,y,z', side_5[1][2], side_3[2][1], None)

angle_7 = ('x,y,z', side_5[0][0], side_4[2][2], side_2[2][0])
edge_12 = ('x,y,z', side_5[0][1], None, side_2[2][1])
angle_8 = ('x,y,z', side_5[0][2], side_3[2][0], side_2[2][2])

print('Верхний слой:')
print(angle_1, edge_1, angle_2, edge_2, center_1, edge_3, angle_3, edge_4, angle_4)
print('Средний слой:')
print(edge_5, center_6, edge_6, center_4, center_3, edge_7, center_2, edge_8)
print('Нижний слой:')
print(angle_5, edge_9, angle_6, edge_10, center_5, edge_11, angle_7, edge_12, angle_8)

# edge = ('x,y,z',side_1[0][0], None , side_6[2][0] )
# так может принимать данные ребро тк 2 цвета и центр будет принимать 1 значение

# import numpy as np  # Идем снизу вверх
# def create_cube():

    