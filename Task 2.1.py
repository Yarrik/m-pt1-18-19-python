print ('введите 3 числа : ',  )
a = int(input())
b = int(input())
c = int(input())
if a and b and c :
    print ("Нет нулевых значений " )
else :
    print('среди чисел есть нулевое значение' )
if a or b or c : 
    print('Первое ненулевое значение =' , a or b or c)
a or b or c or print('Ненулевых значений нет')
if a > b + c :
    print(a-b-c)
elif a < b + c :
    print(b + c - a)
if a > 50 and b > a or c > a :
    print('Вася')
else :
    if  a > 5 or b == 7 and c == 7 :
        print ('Петя')
