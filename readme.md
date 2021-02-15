
# Агрегатор новостей Hacker News.
https://news.ycombinator.com

Приложение периодически парсит указанный сайти и агрегирует информацию о опубликованных постах.
Настройки периода обовления постов указаны в core.settings.py (по умолчанию 1 раз в час). Реализовано с помощью Celery Beat / RabbitMQ.

## Получить список постов
**Request: 
```json
GET /posts/
Accept: application/json

```
**Response **
```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 30,
    "next": "http://127.0.0.1:8000/posts/?limit=5&offset=5",
    "previous": null,
    "results": [
        {
            "id": 82,
            "title": "SolarWinds hack was 'largest and most sophisticated attack' ever: MSFT president",
            "url": "https://www.reuters.com/article/us-cyber-solarwinds-microsoft-idUSKBN2AF03R",
            "created": "2021-02-15T12:38:57.100133+03:00"
        },
        {
            "id": 83,
            "title": "Show HN: ustaxes.org – open-source tax filing webapp",
            "url": "https://github.com/thegrims/UsTaxes",
            "created": "2021-02-15T12:38:57.108168+03:00"
        },
        {
            "id": 84,
            "title": "Ercot nearly at capacity for Texas power grid",
            "url": "http://www.ercot.com/content/cdr/html/real_time_system_conditions.html",
            "created": "2021-02-15T12:38:57.115383+03:00"
        },
        {
            "id": 85,
            "title": "Is Your Linux Version Hiding Interrupt CPU Usage from You?",
            "url": "https://tanelpoder.com/posts/linux-hiding-interrupt-cpu-usage/#how-to-measure-interrupt-cpu-overhead-when-irq-time-accounting-is-disabled",
            "created": "2021-02-15T12:38:57.121914+03:00"
        },
        {
            "id": 86,
            "title": "Show HN: Khan-dl – Khan Academy Course Downloader",
            "url": "https://github.com/rand-net/khan-dl",
            "created": "2021-02-15T12:38:57.128754+03:00"
        }
    ]
}
```
## Сортировка
* Если ordering не указан, то по умолчанию сортировка выполняет по дате сохранения (created)
* Для вывода данных,отсортированных по атрибуту title в алфавитном порядке (по возрастанию), запрос будет выглядеть так:
   
    ```/posts/?ordering=title```
* Такой же запрос, но сортировка в обратном порядке:
   
    ```/posts/?ordering=-title```

## Вывод подмножества данных 

* Если limit и offset не указаны, то вернется только 5 постов.
* Для вывода 10ти постов запрос будет выглядеть так:
  
    ``` posts/?limit=10```
* Для пропуска (оффсета) 15ти последних постов запрос будет выглядеть так:
  
    ```  posts/?offset=15```
* Для вывода 10ти постов с пропуском 15ти, запрос будет выглядеть так:
  
    ``` posts/?limit=10&offset=15 ```
  

Параметры сортировка, лимита и оффсета могут использоваться совместно.
* Для вывода 10ти постов с пропуском 15ти, отсортированных по заголовку запрос будет выглядеть так:
  
    ``` posts/?ordering=title&limit=10&offset=15 ```
