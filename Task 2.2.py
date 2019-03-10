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