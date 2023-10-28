class Player:
    """ Класс для работы с текущим игроком """
    def __init__(self, name):
        self.name = name
        self.wordsListIsUsed = []

    def countWordsListIsUsed(self):
        """ Метод для определения количества угаданных пользователем слов """
        return len(self.wordsListIsUsed)

    def addWordToList(self, playerWord):
        """ Метод для добавления угаданного слова пользователем """
        self.wordsListIsUsed.append(playerWord)

    def wordIsUsedCheck(self, playerWord):
        """ Метод для определения, было ли уже угадано введенное слово или нет """
        if playerWord not in self.wordsListIsUsed:
            self.addWordToList(playerWord)
            print("Верно")
        else:
            print("Это слово вы уже называли")

    def __repr__(self):
        """ Метод для вывода аннотации при выводе экземпляра класса """
        return f"В этом экземпляре класса от Player находится игрок \"{self.name}\" с угаданными им словами {self.wordsListIsUsed}"