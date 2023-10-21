import functions

# Переменные для хранения json файлов
students, professions = functions.load_data()

# Будущая информация студента и профессии (по запросу пользователя)
student_info = []
profession_info = []

# Ввод номера студента
# While true нужен для правильного ввода, иначе вопрос будет задаваться из раза в раз
while True:
    student_number = int(input("Введите номер студента: "))
    student_response = functions.find_student(students, student_number)

    # Проверка ответа функции (был/не был найден)
    if student_response == "Error":
        print("У нас нет такого студента\nПопробуйте еще раз...\n")
    else:
        student_info = student_response
        break

# Переменные для хранения имени студента и его скилов
name, skills = functions.show_student_info(student_info)

# Ввод профессии
# While true нужен для правильного ввода, иначе вопрос будет задаваться из раза в раз
while True:
    profession = input("Выберите специальность для оценки студента " + name + "\n")
    profession_response = functions.check_profession(professions, profession)

    # Проверка ответа функции (был/не был найден)
    if profession_response == "Error":
        print("У нас нет такой специальности\nПопробуйте еще раз...\n")
    else:
        profession_info = profession_response
        break

# Вызов функции, которая отобразит инфо о пригодности и что умеет/не умеет студент
functions.profession_for_student(name, skills, profession_info)
     