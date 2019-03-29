import math
class Point:   
    def __init__(self, name="", x=0, y=0):
        self.x=x
        self.y=y
        self.name=name   

    def __str__(self):
        return '{} координаты: ({}, {})'.format(self.name ,self.x, self.y)

class Segment:
    def __init__(self, name, point1, point2):
        self.name=name
        self.point1=Point(name="", x=0, y=0)
        self.point2=Point(name="", x=0, y=0)

    def length (self, point2):    
        result= ((self.point1.x-point2.x)**2+(self.point2.y-point2.y)**2)**0.5
        return result

    def cosinus(self,point1, point2):
        result=(point2.x-self.point1.x)/((self.point1.x-point2.x)**2+(self.point2.y-point2.y)**2)**0.5
        return result
        
    def shift(self, dx, dy, point1, point2): 
        point1.x=point1.x+dx
        point1.y=point1.y+dy
        point2.x=point2.x+dx
        point2.y=point2.y+dy
        print("координаты точки 1:{},{} ".format(point1.x, point1.y))
        print("координаты точки 2:{},{} ".format(point2.x, point2.y))
        res=((self.point1.x-point2.x)**2+(self.point2.y-point2.y)**2)**0.5
        return res

def entry_coord():
    print("введите координаты для первой точки (x,y): ") 
    x1=int(input('x: '))
    y1=int(input('y: '))
    print("введите координаты для второй точки (x,y): ") 
    x2=int(input('x: '))
    y2=int(input('y: '))
    p1=Point("точка 1 с координатами", x1, y1)
    p2=Point("точка 2 с координатами", x2, y2)
    print(p1)
    print(p2)
    sec=Segment("отрезок1", p1, p2)
    print("длина отрезка между двумя точками: ")
    print(sec.length(p2), 2)
    def display_cos():
        print("угол между отрезком и плоскостью X: ")
        print(sec.cosinus(p1,p2))
    r=input('вывести угол? <Y/N> :')
    if r=='Y':
        display_cos()
    elif r=='N':
        print("отмена")
    else:
        print('ошибка')
    def move_coord():
        print("Задание сдвига по осям (x,y): ") 
        delta_x=int(input('delta_x: ')) 
        delta_y=int(input('delta_y: '))
        print("вывод координат точек после сдвига: ")
        print("вывод длины после сдвига: ")
        print(sec.delta(delta_x, delta_y, p1, p2))
        print("угол между отрезком и плоскостью X после сдвига: ")
        print(sec.cosinus(p1,p2))
    F=input('выполнить сдвиг по осям? <Y/N> :')
    if F=='Y':
         move_coord()
    elif F=='N':
         print("отмена")
    else:
         print('ошибка ввода операции')
  
while True:
    print('Ввод операции :1 - ввод координат для точек - вывод длины отрезка '
                         '2 - вывод угла(косинус) '
                         '3- задание сдвига по координатным осям - вывод после сдвига'
                         'QUIT - для выхода')
    p=input('введите номер операции: ')
    if p=='QUIT':
        print("Выход") 
        break
    elif p=='1':
         entry_coord()
    elif p=='2':
         entry_coord().display_cos()
    elif p=='3':
         entry_coord().move_coord()
    else:
        print("Операция неверна , еще раз")