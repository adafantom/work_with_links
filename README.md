# Посчитайте клики по ссылкам

Код позволяет получить сокращенную ссылку или количество ее посещений 

## Среда

### Требования

Python3 уже должен быть установлен. 

Для запуска программы необходимо указать свой токен API Bitly в файле ```.env``` в переменную BITLY_API_KEY, которая затем используется с помощью библиотеки  ```python-dotenv```.

Используйте pip(или pip3, если есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
```
## Запуск

Запуск в Linux(Python 3) или Windows: 

```bash
$ python main.py
``` 
Пользователь вводит обычную ссылку и получает сокращенную ссылк в виде https://bit.ly/47PuwUo
При вводе сокращенной ссылки пользователь получает количество переходов по ней. 

## Цели проекта

Этот код был написан в образовательных целях как часть онлайн-курса для веб-разработчиков на dvmn.org .
