# Phonebook

Телефонный справочник. Реализованы функции:
- Вывод постранично записей из справочника на экран
- Добавление новой записи в справочник
- Возможность редактирования записей в справочнике
- Поиск записей по одной или нескольким характеристикам

Интерфейс реализован через консоль. Данные хранятся в csv файле. Для работы с данными
справочника используется библиотека pandas. В проекте применяется ООП, валидация данных
с помощью pydantic. 

### В данном проекте использовались следущие инструменты:

  - Python v3.11
  - pandas v2.0
  - pydantic v2.3
  - poetry

## Setup and run:
1. Перейдите в директорию, в которую будете клонировать репозиторий.
2. В зависимости от того, каким менеджером зависимостей Вы пользуетесь, выполните следующие
команды:

При управлении зависимостями через [poetry](https://python-poetry.org/):
```bash
git clone https://github.com/Vladimir-Ivanov-92/phonebook.git
cd phonebook
poetry install --without dev
poetry shell
```

С помощью pip:
```bash
git clone https://github.com/Vladimir-Ivanov-92/phonebook.git
cd phonebook
python3 -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
```

3. Запуск приложения:
```bash
cd phonebook
python3 main.py
```

### Демонтрация работы программы:
1. Главное меню и постраничный вывод данных

![Весь справочник.png](readme_image%2F%D0%92%D0%B5%D1%81%D1%8C%20%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA.png)
2. Добавление записи в справочник

![Добавление строки.png](readme_image%2F%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8.png)
3. Поиск по номеру:

![Поиск по номеру.png](readme_image%2F%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%20%D0%BF%D0%BE%20%D0%BD%D0%BE%D0%BC%D0%B5%D1%80%D1%83.png)
4. Поиск по условию

![Поиск по условию.png](readme_image%2F%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%20%D0%BF%D0%BE%20%D1%83%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D1%8E.png)
5. Поиск по нескольким условиям

![Поиск по нескольким условиям.png](readme_image%2F%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%20%D0%BF%D0%BE%20%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%B8%D0%BC%20%D1%83%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D1%8F%D0%BC.png)

6. Редактирование записи

![Обновление данных.png](readme_image%2F%D0%9E%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85.png)