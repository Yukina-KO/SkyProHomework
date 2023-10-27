from Question import Question
import json
import random

questionsListFromJSON = []
questionsListObject = []

countCorrectAnswer = 0
countPoints = 0
countQuestions = 0

def loadJSON():
    """ Функция для получения списка вопросов из json """
    global questionsListFromJSON
    with open("lessons/Lesson_8/Part2/QuestionList.json") as file:
        questionsListFromJSON = json.load(file)

def getQuestions():
    """ Функция для создания экземпляров класса Questions() """
    global countQuestions
    for question in questionsListFromJSON:
        questionsListObject.append(Question(question["q"], question["d"] + "/5", question["a"]))
    countQuestions = len(questionsListObject)

def showQuestions():
    """ Функция для вывода вопроса и сложности пользователю """
    random.shuffle(questionsListObject)
    for question in questionsListObject:
        print(f"\n{question.buildQuestion()}")
        inputAnswer(question)

def inputAnswer(question):
    """ Функция для записи ответа пользователя и определение его корректности """
    global countCorrectAnswer
    global countPoints
    question.playerAnswer = input("Ответ: ")
    if question.isCorrect() == True:
        print(question.buildPositiveFeedback())
        countCorrectAnswer += 1
        countPoints += question.points
    else:
        print(question.buildNegativeFeedback())

def showResults():
    """ Функция для вывода финального результата после иры """
    print("\nВот и все!")
    print(f"Отвечено {countCorrectAnswer} вопроса из {countQuestions}\nНабрано баллов: {countPoints}")


loadJSON()
getQuestions()
print("\nИгра начинается!")
showQuestions()
showResults()