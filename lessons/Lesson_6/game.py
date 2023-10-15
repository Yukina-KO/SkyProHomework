from gameClass import Game

# Решила вспомнить ООП экспериментально. Задачу можно растягивать и дальше
# и данные не перетирать, а создавать некие новые "Сессии" и с ними работать
# Буду рада любым комментариям :)
session = Game()

while True:
    # перетирание старых значений
    session.playerPoints = 0
    session.checkPlayer = False
    session.playerName = ""
    session.showMenu()
    isMenuInteraction = False
    numAction = ""
    # цикл для проверки правильного ввода
    while True:
        if isMenuInteraction == False:
            numAction = input()
        if numAction == "1" or isMenuInteraction == True:
            isMenuInteraction = True
            name = input("\nВведите ваше имя: ")
            response = session.checkName(name)
            if response == "1":
                break
            elif response == "2":
                continue
        elif numAction == "2":
            session.showLeadBoard()
            session.showMenu()
        elif numAction == "3":
            break
        else:
            print("Выберите действие 1, 2 или 3...\n")

    if numAction == "3":
        break

    print("\n--- Игра началась! ---\n")
    session.showWords()

    print("Вы набрали: " + str(session.playerPoints))

    session.addNewResult()

    session.showLeadBoard()
