List_1 = ['1.missis Marfa Vasilievna ','age', 120,{'Hobby':['needlepoint','fairy tales','Ivan Vasilievich']}]
List_2 = ['2. mister Ivan the Terrible ','age', 59, {'Hobby':['oprichniki','son ','Kemska volost']}] 
List_of_persons = List_1 + List_2
i ='_'
j ='-'
k ='*'
l ='+'
m ='^'
a = str(input('Please , enter your Name - ' ))
b = int(input('Please , enter your age, (years) = ' ))
c = str(input('Please , Who are you ? Enter "mister" , "miss" or "missis"  - ' ))
d = float(input('Please , enter your height, (m) = ' ))
e = float(input('Please , enter your Weight, (kg) = ' ))
x = (e/d**2)
print("===============================================")
if c == 'mister' :
    print('Hello , mister', a, '!')
elif c == 'miss':
        print('Hello , miss ', a, '!')
elif c == 'missis':
        print('Hello , missis ', a, '!')  
print('- your Age - ',b , 'years')     
print('- your height =',d , 'm')
print('- your weight =',e ,'kg')
print('- your Body Mass Index =' , round(x, 4) , 'kg/m2')
if  x < 19  :
    print('Recomendation : you must eat more , because you are underweight ')
    print('graphic BMI')
    print(0, i*int(float(x)) + "x" + i*int(float(19-x)), 19,j*5,25,k*4,30,l*4,35,m*9,45)
elif 19 <= x < 25 :
    print('Recomendation : you look very good , your BMI is normal !!!')
    print('graphic BMI')
    print(0,i*18,19,j*int(float(x-19)) +'x'+ j*int(float(25-x)),25,k*4,30,l*4,35,m*9,45)
elif 25 <= x < 30 :
    print('Recomendation : Not so bad , but You should monitor for your meal. Your BMI is owerweight')
    print('graphic BMI')
    print(0,i*18,19,j*5,25,k*int(float(x-25)) + 'x' + k*int(float(30-x)),30,l*4,35,m*9,45)
elif 30 <= x < 35 :
    print('Recomendation : Danger!!! You must go to Gym  and practice every day . You are obese  !!!')
    print('graphic BMI')
    print(0,i*18,19,j*5,25,k*4,30,l*int(float(x-30)) + 'x' + l*int(float(35-x)),35,m*9,45)
elif 35 <= x < 50 :
    print('Recomendation : I am sorry , i have no idea , what to do ((( You are extremely obese )))) ' )
    print('graphic BMI')
    print(0,i*18,19,j*5,25,k*4,30,l*4,35,m*int(float(x-35)) + 'x' + m*int(float(45-x)),45)
print('Ok! Now we continues. Do you want to know about other persons? Yes or No?')
input()
if 'yes' :
    print(List_of_persons)
elif 'no' :
    print('Ok. enough')
print('May be you want to add new person? Yes or No?' )
input()
if 'yes' :
    print('Ok , lets do it! ')
    a1 = str(input('Please , enter Name of person - ' ))
    b1 = int(input('Please , enter  age of person, (years) = ' ))
    c1 = str(input('Please , Who is this person ? Enter "mister" , "miss" or "missis"  - ' ))
    d1 = float(input('Please , enter  height, (m) = ' ))
    e1 = float(input('Please , enter  Weight, (kg) = ' ))
    x1 = (e1/d1**2)
    print('-  Name is ',a1 ) 
    print('-  Age - ',b1 , 'years')     
    print('-  height =',d1 , 'm')
    print('-  weight =',e1 ,'kg')
    print('-  Body Mass Index =' , round(x1, 4) , 'kg/m2')
elif 'no' :
    print('Ok. enough')
Next_person = [{3:c1,'Name': a1},{'Age ':b1,'height ':d1,
     'weight ': e1,'Body Mass Index ':x1,}]
print('Do you want to add this person in List_of_persons ? Yes or No?')
input()
if 'yes' :
    List_of_persons.append(Next_person) 
    print('This is new list ' , List_of_persons)
elif 'no' :
    print('Ok. enough')
print('Do you want to delete any person in List_of_persons ? Yes or No? ')
input()
if 'yes' :
    print('What person do you want to delete? Marfa Vasilievna or Ivan the Terrible or ' , a1 ,'?')
    z= input()
    if 'Marfa Vasilievna'==z :
        del List_of_persons[0:4]
        print('Ok, look at new list :', List_of_persons)
    elif 'Ivan the Terrible'== z:
        del  List_of_persons[4:8]
        print('Ok, look at new list :', List_of_persons)
    elif a1 ==z :
        del  List_of_persons[8:]
        print('Ok, look at new list :', List_of_persons)
elif 'no' :
    print('Ok. enough')
print('if you want to see information about one of our persons please \
push 1:Marfa Vasilievna or 2:Ivan the Terrible  or 3:', a1 )
P = input()
if P == 1 :
    print (List_1)
elif P == 2 :
    print (List_2)
elif P == 3 :
    print (Next_person)




    
    
