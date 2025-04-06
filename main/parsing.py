import requests
from bs4 import BeautifulSoup
from .models import War


def film_name(url):
    response = requests.get(url)
    data = BeautifulSoup(response.text, 'lxml')
    film_data = data.find_all('div', class_='white-box padding-box')
    film_data2 = data.find_all('p', style = 'background: white;')
    c = 0
    a = []
    a1 = []
    for i in film_data2:
        if i.text.strip() != '':
            a.append(i.text.strip())
    for i in a:
        if i.count('=') == 1:
            n = i.replace('=', '–')
            a1.append(n.split(' – '))
        elif i.count('-') == 1:
            n = i.replace('-', '–')
            a1.append(n.split(' – '))
        else:
            a1.append(i.split(' – '))
    c = 1
    for i in a1:
        if len(i) == 2:
            c += 1
        elif len(i) == 3:
            e = War.objects.get(id=c)
            e.month = i[0] + ' – ' + i[1]
            e.save()
            c += 1
url = 'http://www.zdsamara.ru/city/75-let-pobedy/osnovnye-daty-velikoy-otechestvennoy-voyny/'