"""Импортирование библиотек и пакетов"""
from ast import Continue
from urllib import response
import requests
from bs4 import BeautifulSoup
from re import search

"""Функция для получения содержимого страницы карточки"""
def get_html(url):
    r  = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    return r.text

"""Функция для записи данных карточки"""
def write_card(url):

    """Создание локальных переменных"""
    name = ''
    inn = ''
    phone = ''

    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    """Получение необходимых данных с карточки"""
    try:
        names = soup.find_all('div', {'class':'common-text__value common-text__value_no-padding'})
        com = [name.getText() for name in names] # Генерация списка из вышеупомянутого списка names

        """Проверка на то, чтобы вместо наименования не получить URL адрес компании"""
        if search('http', com[0]): 
            name = com[1]
        else:
            name = com[0].strip()
        
    except IndexError: # Обработка исключений
        Continue

    try:
        inn = soup.find_all('div', {'class':'ml-1 common-text__value'})[0].getText().strip()
    except IndexError:
        Continue

    try:
        numbers = soup.find_all('div', {'class':'common-text__value'})
        phones = [number.getText() for number in numbers]
        for tel in phones:
                if search('mail', tel): # поиск элемента содержащего mail, так как страница не имеет четкой структуры, но при этом номер телефона всегда следует за электронной почтой
                    a = phones.index(tel) # получение индекса элемента с электронной почтой
                    b = a + 1 # получение индекса элемента с номером телефоном

                    phone = phones[b].strip() # присваивание переменной phone одного элемента из списка с удалением отступов

                
    except IndexError: #обработка исключения
        Continue
    
    return [name, inn, phone] # возвращение списка


