# quadratic


Заданиe ниже нужно выполнить используя **любой веб-фреймворк Python (Flask, FastApi, Django)** и любую базу данных.
Результат выполнения задач нужно опубликовать на Github, Gitlab или Bitbucket, и прислать ссылку на опубликованный код.

### Задание

Напишите сервис, который будет находить корни квадратного уравнения ax^2 + bx + c = 0. Самостоятельно определите
наиболее оптимальную структуру возвращаемых данных.

В качестве входных данных в сервис передаются значения a, b, c.

### Как запустить

***В mysql:***

* create database quadratic;

***В терминале:***

* source venv/bin/activate
* pip install -r requirements.txt
* flask db init
* В migration/env.py заменить *"# from myapp import mymodel"* на
  *"from models import \*"* - 21 строка
* Чтобы не получить ошибку - нужно убедиться, что БД создана
* flask db migrate
* flask db upgrade
* Запустить файл main.py



* Сервер доступен на: http://127.0.0.1:5000/
* Имя созданной таблицы после миграции: coefficients  


