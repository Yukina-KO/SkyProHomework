import functions

# Переменные для хранения json файлов
students, professions = functions.load_data()

# Будущая информация студента и профессии (по запросу пользователя)
student_info = []
profession_info = []

def inputStudent():
    """ Функция для ввода номера студента """
    global student_info
    while True:
        while True:
            student_number = input("Введите номер студента: ")
            try:
                student_number = int(student_number)
                break
            except ValueError:
                print("Некорректный номер. Введите целое число")
                
        student_response = functions.find_student(students, student_number)

        if student_response == "Error":
            print("У нас нет такого студента\nПопробуйте еще раз...\n")
        else:
            student_info = student_response
            break

def inputProfession():
    """ Функция для ввода профессии студента """
    global profession_info
    while True:
        profession = input("Выберите специальность для оценки студента " + name + "\n")
        profession_response = functions.check_profession(professions, profession)

        if profession_response == "Error":
            print("У нас нет такой специальности\nПопробуйте еще раз...\n")
        else:
            profession_info = profession_response
            break


inputStudent()

# Переменные для хранения имени студента и его скилов
name, skills = functions.show_student_info(student_info)

inputProfession()

# Вызов функции, которая отобразит инфо о пригодности и что умеет/не умеет студент
functions.profession_for_student(name, skills, profession_info)
     