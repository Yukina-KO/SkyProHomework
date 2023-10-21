import json

# Функция для загрузки инфо из json
def load_data():
    with open("lessons/Lesson_7/Students.json") as file:
        students = json.load(file)
    file.close()
    with open("lessons/Lesson_7/Professions.json") as file:
        professions = json.load(file)
    file.close()

    return students, professions

# Функция для получения студента по индексу
def find_student(students, index):
    response = "Error"
    for student in students:
        if student["pk"] == index:
            response = students[index-1]
            break

    return response

# Функция для отображения имени студента и его скилов
def show_student_info(student):
    print("Студент " + student['full_name'])
    skills = ""
    skills_len = len(student["skills"]) - 1
    count = 0
    # Цикл для отображения скилов в строчку и через запятую
    # Нечто подобное будет использоваться ниже (не смогла их объединить, т.к. перебираемые значения имеют разные типы/индексы/ключи)
    while count <= skills_len:
        if count != skills_len:
            skills += student["skills"][count] + ", "
        else:
            skills += student["skills"][count]
        count += 1
    print("Знает " + skills)

    return student['full_name'], student["skills"]

# Функция которая смотрит, есть введенная специальность или нет
def check_profession(professions, profession):
    response = "Error"
    for prof in professions:
        if prof["title"] == profession:
            response = prof['skills']
            break

    return response

# Функция для отображения проф. пригодности
def profession_for_student(student, student_skills, profession_skills):
    # Преобразование ко множеству
    stud_skills_list = set(student_skills)
    prof_skills_list = set(profession_skills)
    # Получаем что студент знает
    student_prof_know = stud_skills_list.intersection(prof_skills_list)
    # И что не знает
    student_prof_dont_know = prof_skills_list.difference(stud_skills_list)
    # Вычисляю процент проф. пригодности
    print("Пригодность " + str(int(100 / len(profession_skills) * len(student_prof_know))) + "%")
    # Отображаю инфу и вызываю функцию для красивого отображения
    print(student + " знает " + skills_string_struct(student_prof_know))
    print(student + " не знает " + skills_string_struct(student_prof_dont_know))

# Функция для скилов (чтобы все были через запятую и в одну строку)
def skills_string_struct(data):
    data = list(data)
    count = 0
    data_len = len(data) - 1
    response = ""
    while count <= data_len:
        if count != data_len:
            response += data[count] + ", "
        else:
            response += data[count]
        count += 1
    return response