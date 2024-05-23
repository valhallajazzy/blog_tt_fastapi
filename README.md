# Blog's API  
![Screenshot](https://github.com/valhallajazzy/blog_tt_fastapi/blob/main/pic/blog_main.png)
В данном проекте реализовано API блога содержащий сущности:  
* Posts (Посты)  
* Categories (Категории)  
* Tags (Тэги)  
* Authors (Авторы)

Так же поддерживаются CRUD-запросы по всем сущностям  

## URLs для отправки API-запроса:  
`/authors` - путь к API авторов  
`/posts` - путь к API постов  
`/categories` - путь к API категорий  
`/tags` - путь к API тегов  

В продолжение всех путей CRUD-запросы выполняются по следующим префиксам:  

`/` - READ-запрос (GET)  
`/create` - CREATE-запрос (POST)  
`/update` - UPDATE-запрос(PATCH)  
`/delete` - DELETE-запрос(DELETE)  

#### !!! У сущностей `/categories` и `/tags` UPDATE-запроса нет.  
#### К Swagger возможно перейти по адресу `http://0.0.0.0:8004/docs#/`  

## Подготовка и запуск проекта
* Запускаем БД в docker-compose:  
```console
$ docker-compose up -d
```
* Создаем файл `.env` в корневой директории проекта и указываем переменную `DATABASE_URL`  
содержащую полный путь для подключения к базе данных:  
![Screenshot](https://github.com/valhallajazzy/blog_tt_fastapi/blob/main/pic/url_blog.png)
* Запускаем приложение из корневой директорий приложения:  
```console
$ python3 main.py
```
