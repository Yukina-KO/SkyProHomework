from Classes.BasicWord import BasicWord
import requests
import random
import json

chars = [
	'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 
	'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
]

def loadRandomWord():
    """ Функция для загрузки json с сайта или файла """
    try:
        response = requests.get('https://www.jsonkeeper.com/b/2GVM')
        response = response.json()
    except:
        print("Ошибка получения данных с jsonkeeper.com")
        print("Все слова взяты из файла")
        with open("lessons/FinalWork2/Words.json", encoding='utf-8') as file:
            response = json.load(file)

    getRandomIndex = random.randrange(0, len(response))
    randomWord = response[getRandomIndex]
    word = BasicWord(randomWord['word'], randomWord['subwords'])

    return word

def checkWordChars(word):
    """ Функция для проверки слова (является ли введенное слово - словом) """
    for char in word:
        if char not in chars:
            return False
            
    return True