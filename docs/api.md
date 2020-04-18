# API:
### Работа с пользователем
```python
GET /api/user # получение списка пользователей
response:
{
  'users': [
    {
      'id_user': int,
      'login': str
    }
  ]
}

GET /api/user/<int:id_user> # получение профиля пользователя
response:
{
  'id_user': int,
  'login': str,
  'rating': int,  # какое место пользователь занимает в общем рейтинге
  'game_history': [
    {
      'id_game': int,
      'time': str,
      'round': int, # Номер раунда игры
      'Health': float,   # Здоровье
      'food': float,     # Питание
      'Leisure': float,  # Досуг
      'Communication': float,   # Общение
      'point': int # Количество очков, заработанных за игру.
    }
  ]

}

POST /api/user/login # авторизация пользователя
{
  'login': str,
  'password': str
}
response:
{
  'session': str # сессия, с которой пользователь подключен
}

POST /api/user/register #  регистрация пользователя
{
  'login': str,
  'password': str
}
response:
{
  'session': str # сессия, с которой пользователь подключен
}
```

### Выбор персонажа
```python
GET /api/person # Список персонажей в игре
response:
{
  'id_person': int,
  'name': str,
  'description': str, # описание персонажа
  'pic': str # ссылка на картинку
}
```

### Рейтинг
```python
GET /api/rating # Рейтинг игр пользователей
response:
{
  "id_user": int, 
  "point": int
}
GET /api/rating/<int:id_user> # Рейтинг игр пользователя
response:
{
  'game_history': [
    {
      'id_game': int,
      'time': str,
      'round': int, # Номер раунда игры
      'Health': float,   # Здоровье
      'food': float,     # Питание
      'Leisure': float,  # Досуг
      'Communication': float,   # Общение
      'point': int, # Количество очков, заработанных за игру.
      'value': int, # количество денег
    }
  ]
}
```

### Игра
```python
GET /api/game # Получить данные о текущей игре
response:
{
  'id_question': int,
  'description': str,
  'round': int, # Номер раунда игры
  'Health': float,   # Здоровье
  'food': float,     # Питание
  'Leisure': float,  # Досуг
  'Communication': float,   # Общение
  'point': int, # количество очков
  'value': int, # количество денег
}

POST /api/game # Запуск новой игры
{
  'id_person': int # идентификатор персонажа, с которым начинается игра
}

POST /api/game/question
{
  'id_question': int,
  'answer': int 
}
response 
{
  'id_question': int,
  'description': str,
  'round': int, # Номер раунда игры
  'Health': float,   # Здоровье
  'food': float,     # Питание
  'Leisure': float,  # Досуг
  'Communication': float,   # Общение
  'point': int, # количество очков
  'value': int, # количество денег
}

GET /api/game/events # Получить события, которые произошли в игре
response 
{
  'event': [
    {
      'element': str, # какой элемент изменился
      'description': str # какое сообщение вывести
    }
  ]
}
```
