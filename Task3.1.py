
i ='_'
j ='-'
k ='*'
l ='+'
m ='^'
List_of_persons = {
    'missis Marfa Vasilievna': {
        'age': 120,
        'height': 1.85,
        'weight': 120,
        'BMI': 35,
        'Hobby':['needlepoint','fairy tales','Ivan Vasilievich']
    },
    'mister Ivan the Terrible': {
        'age': 428,
        'height': 2.0,
        'weight': 75,
        'BMI': 18.75,
        'Hobby':['oprichniki','son ','Kemska volost']
    },
    'mister Batman': {
        'age': 35,
        'height': 1.95,
        'weight': 100,
        'BMI': 26.3,
        'Hobby':['Joker','Gotem ','Bats']
    }
}
mission_1  = input("Do you want to know about  persons? Yes or No?' ")
if mission_1 == 'yes':
    print("There are next persons in list:")
    for key in List_of_persons:
        print(key)

mission_2 = input("Do you want to know about certain person? Yes or No? ")
if mission_2 == 'yes':
    person = input("Enter full name of person: ")
    if person in List_of_persons:
        print("Name: {}\nAge: {}\nheight: {}\nweight: {}\nBMI: {}\nHobby: {}"
              .format(person, List_of_persons[person]['age'],
               List_of_persons[person]['height'],List_of_persons[person]['weight'],
                      List_of_persons[person]['BMI'],List_of_persons[person]['Hobby']))
    else:
        print("Wrong Name of person")

mission_3 = int(input("What kind of modification do you want to do?\n1 - Change data of person in the list\n"
                    "2 - Delete person from list\n3 - Enter new person in the list\n"
                    "4 - No modification\nYour answer (number): "))
if  mission_3 == 1:
    person = input("Enter full name of person, what data change: ")
    age = int(input("Enter age: "))
    height = float(input("Enter height: "))
    weight = float(input("Enter weight: "))
    bmi = weight / (height**2)
    Hobby = input("Enter Hobby of person: ") 
    if person in List_of_persons:
        List_of_persons.update({person: { 'age': age, 'height': height, 'weight': weight, 'BMI': bmi}})
        print("Now person look :\nName: {}\nAge: {}\nheight: {}\nweight: {}\nBMI: {}\nHobby: {}"
              .format(person, List_of_persons[person]['age'], List_of_persons[person]['height'],
               List_of_persons[person]['weight'],List_of_persons[person]['BMI'],List_of_persons[person]['Hobby']))
    else:
        print("Wrong name")

elif mission_3 == 2:
    del_person = input("Enter full name of person, what data delete: ")
    if del_person in  List_of_persons:
        del  List_of_persons[del_person]
        print("Person was delete. Now look at list:")
        for key in  List_of_persons:
            print(key)
    else:
        print("Wrong name")

elif mission_3 == 3:
    new_person = input("Enter full name of new person: ")
    age = int(input("Enter age: "))
    height = float(input("Enter height: "))
    weight = float(input("Enter weight: "))
    bmi = weight / (height**2)
    Hobby = input("Enter Hobby of person: ") 
    List_of_persons[new_person] = { 'age': age, 'height': height, 'weight': weight, 'BMI': bmi, 'Hobby': Hobby}
    print("Data of new person:\nName: {}\nAge: {}\nheight: {}\nweight: {}\nBMI: {}\nHobby: {}"
          .format(new_person,List_of_persons[new_person]['age'],List_of_persons[new_person]['height'],
          List_of_persons[new_person]['weight'], List_of_persons[new_person]['BMI'],List_of_persons[new_person]['Hobby']))
elif mission_3 == 4:
    print("Ok.Inough")
else:
    print("Ok")
if (mission_3 == 1 and person in List_of_persons) or mission_3 == 3:
    print("This is graphic of BMI")
n = str(input('Введите имя пользователя: '))
bmi = round(List_of_persons[n]['weight'] / List_of_persons[n]['height']**2 )
if  bmi < 19  :
    print('Recomendation : you must eat more , because you are underweight ')
    print(0, i*int(float(bmi)) + "x" + i*int(float(19-bmi)), 19,j*5,25,k*4,30,l*4,35,m*9,45)
elif 19 <= bmi < 25 :
    print('Recomendation : you look very good , your BMI is normal !!!')
    print(0,i*18,19,j*int(float(bmi-19)) +'x'+ j*int(float(25-bmi)),25,k*4,30,l*4,35,m*9,45)
elif 25 <= bmi < 30 :
    print('Recomendation : Not so bad , but You should monitor for your meal. Your BMI is owerweight')
    print(0,i*18,19,j*5,25,k*int(float(bmi-25)) + 'x' + k*int(float(30-bmi)),30,l*4,35,m*9,45)
elif 30 <= bmi < 35 :
    print('Recomendation : Danger!!! You must go to Gym  and practice every day . You are obese  !!!')
    print(0,i*18,19,j*5,25,k*4,30,l*int(float(bmi-30)) + 'x' + l*int(float(35-bmi)),35,m*9,45)
elif 35 <= bmi < 50 :
    print('Recomendation : I am sorry , i have no idea , what to do ((( You are extremely obese )))) ' )
    print(0,i*18,19,j*5,25,k*4,30,l*4,35,m*int(float(bmi-35)) + 'x' + m*int(float(45-bmi)),45)   