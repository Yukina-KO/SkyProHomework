class BasicWord:
    """ Класс для работы со случайным словом из json """
    def __init__(self, baseWord, newWordsList):
        self.baseWord = baseWord
        self.newWordsList = newWordsList

    def checkWord(self, playerWord):
        """ Метод для нахождения введенного слова пользователем в списки допустимых слов """
        if playerWord in self.newWordsList:
            return True
        else:
            return False

    def countNewWordsList(self):
        """ Метод для определения количества возможных слов """
        return len(self.newWordsList)

    def __repr__(self):
        """ Метод для вывода аннотации при выводе экземпляра класса """
        return f"В этом экземпляре класса от BasicWord находится слово \"{self.baseWord}\" и список составных слов {self.newWordsList}."