![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<img src="https://dvmn.org/assets/img/logo.8d8f24edbb5f.svg" alt= “” width="195" height="50">
# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка.
Python3 должен быть уже установлен.

Рекомендуется использовать среду окружения [venv](https://docs.python.org/3/library/venv.html) 
для изоляции проекта.

Используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей
```console
$ pip install -r requirements.txt
```

## Запуск

- Скачайте код
- Запустите сайт командой 
```console
$ python main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Внесение изменений на сайт

- Все данные о винах и напитках беруться из `excel` файла, путь к файлу в `settings.py`.
--- Excel файл:
  если есть запись в колонке **Акция**, то картинка пометиться лейбой **Выгодная цена**.
- картинки храняться в директории `images/`
- Вывод разбивается на блоки по категориям
- Если нет данных о сорте, то строка не выводиться


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте 
![Devman](https://dvmn.org/assets/img/logo.8d8f24edbb5f.svg)[Devman](https://dvmn.org).
