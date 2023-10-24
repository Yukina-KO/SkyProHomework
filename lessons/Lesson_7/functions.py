import json

frontendProfessionsList = ["front end", "frontend", "front-end", "web-developer", "web developer", "frontend developer", "front-end developer", "front end developer"]
backendProfessionsList = ["back end", "backend", "back-end", "backend-developer", "backend developer", "back-end developer", "back end developer"]
testerProfessionList = ["tester", "testing"]

def load_data():
    """ Функция для загрузки инфо из json """
    with open("lessons/Lesson_7/Students.json") as file:
        students = json.load(file)
    with open("lessons/Lesson_7/Professions.json") as file:
        professions = json.load(file)

    return students, professions

def find_student(students, index):
    """ Функция для получения студента по индексу """
    response = "Error"
    for student in students:
        if student["pk"] == index:
            response = students[index-1]
            break

    return response

def show_student_info(student):
    """ Функция для отображения имени студента и его скилов """
    print("Студент " + student['full_name'])
    skills = ", ".join(student["skills"])
    print("Знает " + skills)

    return student['full_name'], student["skills"]

def check_profession(professions, profession):
    """ Функция которая смотрит, есть введенная специальность или нет """
    response = "Error"
    for prof in professions:
        if profession.lower() in frontendProfessionsList:
            if prof["title"] == "Frontend":
                response = prof['skills']
                break
        elif profession.lower() in backendProfessionsList:
            if prof["title"] == "Backend":
                response = prof['skills']
                break
        elif profession.lower() in testerProfessionList:
            if prof["title"] == "Testing":
                response = prof['skills']
                break

    return response

def profession_for_student(student, student_skills, profession_skills):
    """ Функция для отображения проф. пригодности """
    percentMax = 100

    student_skills_list = set(student_skills)
    profession_skills_list = set(profession_skills)

    student_know_professions = student_skills_list.intersection(profession_skills_list)
    student_dontKnow_professions = profession_skills_list.difference(student_skills_list)

    print("Пригодность " + str(int(percentMax / len(profession_skills) * len(student_know_professions))) + "%")

    if not bool(student_know_professions):
        print(student + " ничего не знает из необходимого :(")
    else:
        print(student + " знает " + ", ".join(list(student_know_professions)))
    if not bool(student_dontKnow_professions):
        print(student + " все знает :)")
    else:
        print(student + " не знает " + ", ".join(list(student_dontKnow_professions)))
