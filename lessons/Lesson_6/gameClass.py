import random

class Game:
    def __init__(self):
        # Флаг говорящий о том, есть ли играющий игрок в списке
        self.checkPlayer = False
        # Имя игрока (текущего на данной сессии)
        self.playerName = ""
        # Очки игрока за игру
        self.playerPoints = 0

    # Метод показывает меню выбора
    def showMenu(self):
        print("\n----- Меню -----\n\n"+
        "Введите номер, чтобы выбрать действие...\n\n" +
        "1. Начать игру\n" +
        "2. Посмотреть список лидеров\n" +
        "3. Выход\n"
        )

     # Метод для вывода списка лидеров (отсортированного)
    def showLeadBoard(self):
        playersStats = {}
        print("\n----- Список лидеров -----\n")
        with open("lessons/Lesson_6/stats.txt", "r") as file:
            for line in file:
                split = line.split()
                playersStats[split[0]] = split[1]
        file.close()
        sortPlayers = (list(reversed(sorted(playersStats.items(), key=lambda x: x[1]))))
        for items in sortPlayers:
            print("Игрок: " + items[0] + "  Очков: " + items[1])

    # Метод для проверки текущего игрока в записях файла
    # Идет отслеживание игрок старый или новый
    # Если старый, то об этом сообщается и предлагается продолжить за существующего или выбрать другое имя
    # Если новый, то об этом сообщается и предлагается продолжить за нового или выбрать другое имя
    def checkName(self, playerName):
        # Проверка наличия игрока в файле
        with open("lessons/Lesson_6/players.txt", "r") as fileR:
            for line in fileR:
                if line[0:len(line)-1] == playerName:
                    self.checkPlayer = True
        fileR.close()
            
        # Сообщение о новом/старом игроке    
        if self.checkPlayer == True:
            print("\nИгрок с таким именем уже существует! " +
            "Хотите продолжить с этим именем или выберете другое?\n")
        elif self.checkPlayer == False:
                print("\nВы новый Игрок! Хотите продолжить с " +
            "этим именем или выберете другое?\n")

        # Выбор действия для введенного имени
        print("Введите номер, чтобы выбрать действие...\n\n" +
            "1. Продолжить с текущим\n" +
            "2. Ввести другое\n"
            )

        # while true нужен для того, чтобы игрок точно ввел что его просят
        while True:
            playerEnter = input()
            # Действие, если игрок решил продолжить со старым именем
            if playerEnter == "1" and self.checkPlayer == True:
                print("\n--> Вы продолжаете игру как \"" + playerName + "\"" +"\n")
                self.playerName = playerName
                return "1"

            # Действие, если игрок решил продолжить с новым именем
            elif playerEnter == "1" and self.checkPlayer == False:
                with open("lessons/Lesson_6/players.txt", "a") as fileA:
                    fileA.write(playerName + '\n')
                    self.playerName = playerName
                    print("\n--> Новый игрок создан\n")
                fileA.close()
                return "1"

            # Действие, если игрок решил играть с другим именем (ему нужен повторный ввод)
            elif playerEnter == "2":
                self.checkPlayer = False
                return "2"
            
            # Действие, если была выбрана несуществующая команда
            else:
                print("\nВыберите действие 1 или 2...\n")
            
    # Метод для преобразования слова в рандомные символы из него же
    def randomCharsInWord(self, word):
        lenWord = len(word) - 1
        randomCharsInString = ""
        count = 1
        usedIndex = []
        while lenWord >= count:
            randomIndex = random.randint(0, lenWord - 1)
            if randomIndex not in usedIndex:
                randomCharsInString += word[randomIndex]
                usedIndex.append(randomIndex)
                count+=1
        return randomCharsInString
        
    # Метод для вывода игроку слов
    def showWords(self):
        with open("lessons/Lesson_6/words.txt", "r") as file:
            for word in file:
                randomChars = self.randomCharsInWord(word)
                print("\nУгадайте слово: " + randomChars)
                playerWord = input("Ответ: ")
                if playerWord == word[0:len(word) - 1]: # В конце каждого слова word присутствует конструкция "\n". Здесь она как раз не учитывается
                    print("Верно! Вы получаете 10 очков")
                    self.playerPoints += 10
                else:
                    print("Неверно! Верный ответ – " + word)
        file.close()

    # Метод для добавления нового результата
    def addNewResult(self):
        index = 0
        with open("lessons/Lesson_6/stats.txt", "r") as file:
            lines = file.readlines()
        file.close()
        with open("lessons/Lesson_6/stats.txt", "r") as fileR:
            for line in fileR:
                split = line.split()
                # Если игрок уже играл, то его данные перетираются
                if split[0] == self.playerName:
                    del lines[index]
                    with open("lessons/Lesson_6/stats.txt", "w") as fileW:
                        fileW.writelines(lines)
                    fileW.close()
                    break
                else:
                    index += 1

            # Занесение нового результата
            with open("lessons/Lesson_6/stats.txt", "a") as fileA:
                fileA.write(self.playerName + " " + str(self.playerPoints) + "\n")
            fileA.close()
        fileR.close()
        