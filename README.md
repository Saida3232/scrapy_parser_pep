# scrapy_parser_pep

## O проекте
Scrapy_pep_parser -парсер документов PEP на базе фреймворка Scrapy.
С возможностью получения информации о названии, номере,статусе PEP с официального сайта документации PEP 
[peps.python.org](https://peps.python.org/)

На выходе вы получите два файла в формате csv :
Первый файл хранит список всех PEP: номер, название и статус.
2 -Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе.

## Стек использованных технологий
* Python
* Scrapy

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Saida3232/scrapy_parser_pep.git
```

Создать и активировать виртуальное окружение:
```
python3 -m venv env
#или 
py -3.9 -m  venv venv
```


```
source env/bin/activate
```

## Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

## Смело запускайте парсер
```
scrapy crawl pep
```
## Автор
Автор: [Saida](https://github.com/Saida3232)