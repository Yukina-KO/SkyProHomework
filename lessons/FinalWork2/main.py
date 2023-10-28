from Classes.Player import Player
import utils

def enterPlayerName():
    """ Функция для ввода имени игрока и создании экземпляра класса Player """
    global player
    playerName = input("Введите имя игрока: ")
    player = Player(playerName)
    print(f"Привет, {player.name}!")

def showGameInfo():
    """ Функция для генерации случайного слова и вывода игровой информации """
    global randomWord
    randomWord = utils.loadRandomWord()
    print(f"Составьте {randomWord.countNewWordsList()} слов из слова {randomWord.baseWord.upper()}")

    print("Слова должны быть не короче 3 букв")
    print("Чтобы закончить игру, угадайте все слова или напишите \"stop\"")
    print("Поехали!\n")


def enterWords():
    """ Функция для ввода слов пользователем """
    while True:
        playerWord = input("Введите слово: ").lower()
        if utils.checkWordChars(playerWord) == False and playerWord != "stop":
            print("Слово содержит пробелы, цифры, англ.буквы или неподлежащие символы")
            continue
        else:
            if playerWord == "stop" or playerWord == "стоп":
                break
            else:
                if randomWord.checkWord(playerWord) == False:
                    print("Такого слова нет")
                else:
                    player.wordIsUsedCheck(playerWord)

enterPlayerName()
showGameInfo()
enterWords()

print(f"\nИгра завершена. Угаданных слов: {player.countWordsListIsUsed()}!")
