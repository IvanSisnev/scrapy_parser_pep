[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Practicum.Yandex](https://img.shields.io/badge/-Practicum.Yandex-464646?style=flat&logo=Practicum.Yandex&logoColor=56C0C0&color=008080)](https://practicum.yandex.ru/)
# Парсер PEP Python

## Описание проекта
Парсер Python Enhancement Proposals (PEP), расположенных по адресу: 

* *https://peps.python.org/*

## Развертывание проекта

1. Клонировать проект с GitHub.
2. Развернуть и активировать виртуальное окружение.
3. Установить зависимости из файла `requirements.txt`.

## Описание парсера

В проекте реализован парсер `pep`:

* собирает номера, названия и статусы всех PEP
* подсчитывает количества PEP каждого статуса
* подсчитывает общее количество PEP
* сохраняет в директорию `results` следующие данные:
  * номер, названия и статус каждого PEP
  * количества PEP каждого статуса, общее количество PEP

## Запуск парсера

Команда запуска парсеров: `scrapy crawl pep`

Команду запуска парсеров необходимо вводить в окне терминала, находясь в 
директории `scrapy_parser_pep`.