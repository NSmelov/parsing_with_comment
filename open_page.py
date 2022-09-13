"""Импорт необходимых библиотек"""
from urllib import response
import requests
from bs4 import BeautifulSoup

"""Функция для получения HTML разметки страницы"""
def get_html(url):
    r  = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'}) # Здесь выполняется запрос с параметрами браузера для того, чтобы сервер не блокировал запросы
    return r.text # Возвращение текста страницы (HTML кода)


"""Функция для чтения каждой страницы с карточками для сбора ссылок на эти карточки"""
def write_links(links):
    for i in range(99):
        url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString=&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D0%BE%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber='+str(i + 1)+'&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&savedSearchSettingsIdHidden=&sortBy=UPDATE_DATE&fz223=on&placingWayList=&selectedLaws=&priceFromGeneral=&priceFromGWS=&priceFromUnitGWS=&priceToGeneral=&priceToGWS=&priceToUnitGWS=&currencyIdGeneral=-1&publishDateFrom=&publishDateTo=&applSubmissionCloseDateFrom=&applSubmissionCloseDateTo=&customerIdOrg=&customerFz94id=&customerTitle=&okpd2Ids=&okpd2IdsCodes=' # URL адреса для каждой страницы отличаются лишь одним параметром

        html = get_html(url) 
        soup = BeautifulSoup(html, 'lxml') # Вызов метода парсинга HTML странички
        href = soup.find_all('div', class_='registry-entry__header-mid__number') # Поиск элементов (дивизионов) с нужным классом

        """Цикл для формирования полноценных URL адресов, поскольку в начальных ссылках представлена лишь часть URL адреса"""
        for i in href:
            for link in i.find_all('a'):
                link = 'https://zakupki.gov.ru' + str(link['href'])
                
                links.append(link) # Добавление ссылок в общий список
