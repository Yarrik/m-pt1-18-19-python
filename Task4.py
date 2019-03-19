registr = {'Oleg': 'Yarotski' }
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

def mission():
    return  int(input("What kind of modification do you want to do?:\n1 -want to know about  all persons\n"
                  "2 -Look at data of certain person\n3 -Change data of person in the list\n "
                "4 -Delete person from list\n5 - Enter new person in the list\n"
                    "6 - out of system\nYour answer (number): "))

def mission_1(answer) :
    if answer == 1:
        print("There are next persons in list:")
        for key in List_of_persons:
            print(key)

def mission_2(answer) :
    if answer == 2:
        person = input("Enter full name of person: ")
        if person in List_of_persons:
            print("Name: {}\nAge: {}\nheight: {}\nweight: {}\nBMI: {}\nHobby: {}"
              .format(person, List_of_persons[person]['age'],
               List_of_persons[person]['height'],List_of_persons[person]['weight'],
               List_of_persons[person]['BMI'],List_of_persons[person]['Hobby']))
        else:
            print("Wrong Name of person")

def mission_3(answer):
    if answer == 3:
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

def mission_4 (answer):
    if answer == 4:
        del_person = input("Enter full name of person, what data delete: ")
        if del_person in  List_of_persons:
            del  List_of_persons[del_person]
            print("Person was delete. Now look at list:")
            for key in  List_of_persons:
                print(key)
        else:
            print("Wrong name")

def mission_5 (answer):
    if answer == 5:
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

def question():
    log = input("Enter your login: ")
    pas = input("enter your password: ")
    return log, pas


def login_required(main_funct):
    def wrapper():
        sign = input("Enter to the system? yes/no: ")
        if sign == 'yes':
            login, passw = question()
            while login not in registr or registr[login] != passw:
                print("Wrong login and password")
                login, passw = question()
            print("You enter to the system!")
            main_funct()              
    return wrapper()


@login_required
def main_function():
    while True:
        answer = mission()
        if answer == 6:
            print("out of system")
            break
        if answer not in range(1, 7):
            print("Wrong !!!!")
            continue
        mission_1(answer)
        mission_2(answer)
        mission_3(answer)
        mission_4(answer)
        mission_5(answer)



