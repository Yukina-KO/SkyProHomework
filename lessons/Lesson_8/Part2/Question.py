class Question:
    def __init__(self, textQuestion, complexity, correctAnswer, isQuestionShow = False, playerAnswer = None):
        self.textQuestion = textQuestion
        self.complexity = complexity
        self.correctAnswer = correctAnswer
        self.isQuestionShow = isQuestionShow
        self.playerAnswer = playerAnswer
        self.points = self.getPoints()

    def getPoints(self):
        """ Метод для вычисления очков за сложность """
        difficultyScore = 10
        points = self.complexity.split("/")
        return int(points[0]) * difficultyScore

    def isCorrect(self):
        """ Метод для определения корректного ответа """
        if self.playerAnswer == self.correctAnswer:
            return True
        else:
            return False

    def buildQuestion(self):
        """ Метод для вывода вопроса и сложности """
        message = f"Вопрос: {self.textQuestion}\nСложность {self.complexity}"
        return message

    def buildPositiveFeedback(self):
        """ Метод для вывода информации при правильном ответе """
        message = f"Ответ верный, получено {self.points} баллов"
        return message

    def buildNegativeFeedback(self):
        """ Метод для вывода информации при не правильном ответе """
        message = f"Ответ неверный, верный ответ - {self.correctAnswer}"
        return message