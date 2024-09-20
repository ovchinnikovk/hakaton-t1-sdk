# SDK для добаления нового функционала на сайт
- Приложение докеризировано

## Функции

- Добавляйте новые опросы в БД
- Обновление информации о существующих данных
- Отображение списка всех пользователей

## Запуск

1. Клонируйте репозиторий:
 ```
 https://github.com/ovchinnikovk/hakaton-t1-sdk.git
 ```
2. Перейдите в каталог проекта:
 ```
 cd hakaton-t1-sdk
 ```
3. Запустите приложение:
- Установите python
- Создайте виртуальную среду (venv):
```
python3 - Linux/macOS
python - Windows NT
pip3 - Linux/macOS
pip - Windows NT
```
```
python -m venv venv
```
- Активируйте виртуальную среду (venv) - Windows:
```
venv/Scripts/activate
```
- Активируйте виртуальную среду (venv) - Linux / GNU / BSD / Unix / macOS:
```
source venv/bin/activate
```
- Следуйте инструкциям:
```
pip install -r requirements.txt
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
- Запуск сервера
```
python manage.py runserver
```
## Использование
- Запуск сервера
```
python manage.py runserver
```
- Оставновка сервера
```
CTRL + C
```


## Тестирование

Чтобы запустить модульные тесты приложения, используйте следующую команду:

 ```
 python -m unittest tests
 ```
## Вклад

Если вы обнаружите какие-либо проблемы или у вас есть предложения по улучшению, смело открывайте новую проблему или отправляйте запрос на включение.

## Лицензия

Лицензировано под лицензией:

* MIT license (https://opensource.org/license/mit)

## Целевые ОС

- Windows NT 10/11
- GNU/Linux - Дистрибутивы
- BSD/Mach - macOS# hakaton-t1-sdk
