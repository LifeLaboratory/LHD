# API:
### Работа с пользователем
```python
-> GET /api/user # получение списка пользователей
response:
{
  'users': [
    {
      'id_user': int,
      'login': str
    }
  ]
}

-> GET /api/user/profile  # получение своего профиля пользователя
response:
{
  'id_user': int,
  'login': str,
  'rating': int,  # какое место пользователь занимает в общем рейтинге
  'count_game': int,  # Количество игр
  'max_point': int,  # Максимальное количество очков
  'pic': str,
  'game_history': [
    {
      'id_game': int,
      'time': str,
      'round': int, # Номер раунда игры
      'health': float,   # Здоровье
      'food': float,     # Питание
      'leisure': float,  # Досуг
      'communication': float,   # Общение
      'point': int # Количество очков, заработанных за игру.
    }
  ]
}

-> GET /api/user/<int:id_user> # получение профиля пользователя
response:
{
  'id_user': int,
  'login': str,
  'rating': int,  # какое место пользователь занимает в общем рейтинге
  'count_game': int,  # количество игр
  'max_point': int,  # Максимальное количество очков
  'pic': str,
  'game_history': [
    {
      'id_game': int,
      'time': str,
      'round': int, # Номер раунда игры
      'health': float,   # Здоровье
      'food': float,     # Питание
      'leisure': float,  # Досуг
      'communication': float,   # Общение
      'point': int # Количество очков, заработанных за игру.
    }
  ]

}

-> POST /api/user/login # авторизация пользователя
{
  'login': str,
  'password': str
}
response:
{
  'session': str # сессия, с которой пользователь подключен
}

-> POST /api/user/register #  регистрация пользователя
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
-> GET /api/person # Список персонажей в игре
response:
{
  'id_person': int,
  'name': str,
  'description': str, # описание персонажа
  'pic': str, # ссылка на картинку
  'health': float,  # Здоровье
  'food': float,  # Питание
  'leisure': float,  # Досуг
  'communication': float,  # Общение
  'value': int,  # количество денег
}
```

### Рейтинг
```python
-> GET /api/rating # Рейтинг игр пользователей
response:
{
    'top': [
        {
            'id_user': int,
            'name': str,
            'time': str,
            'health': float,  # Здоровье
            'food': float,  # Питание
            'leisure': float,  # Досуг
            'communication': float,  # Общение
            'point': int,  # Количество очков, заработанных за игру.
            'value': int,  # количество денег
        }
    ]
}
```

### Игра
```python
-> GET /api/game # Получить данные о текущей игре
response:
{
  'id_question': int,
  'description': str,
  'left_answer': str,  # Первый ответ
  'right_answer': str,  # Второй ответ
  'round': int, # Номер раунда игры
  'health': float,   # Здоровье
  'food': float,     # Питание
  'leisure': float,  # Досуг
  'communication': float,   # Общение
  'point': int, # количество очков
  'value': int, # количество денег
  'call': bool, # можем ли позвонить? 
  'worked': bool, # можем ли работать? 
  'covid': bool, # заражены? 
}

-> POST /api/game # Запуск новой игры
{
  'id_person': int # идентификатор персонажа, с которым начинается игра
}

-> POST /api/game/question
{
  'answer': str # левый или правый ответ 
}
response 
{
  'id_question': int,
  'description': str,
  'left_answer': str,  # Первый ответ
  'right_answer': str,  # Второй ответ
  'round': int, # Номер раунда игры
  'health': float,   # Здоровье
  'food': float,     # Питание
  'leisure': float,  # Досуг
  'communication': float,   # Общение
  'point': int, # количество очков
  'value': int, # количество денег
  'call': bool, # можем ли позвонить? 
  'worked': bool, # можем ли работать? 
  'covid': bool, # заражены? 
  'event': str, # Событие, которое необходимо отобразить пользователю
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


-> POST /api/game/action # Выполнить действие
{
  'action': str # worked/call_friend/call_delivery
}
response:
{
  'id_question': int,
  'description': str,
  'left_answer': str,  # Первый ответ
  'right_answer': str,  # Второй ответ
  'round': int, # Номер раунда игры
  'health': float,   # Здоровье
  'food': float,     # Питание
  'leisure': float,  # Досуг
  'communication': float,   # Общение
  'point': int, # количество очков
  'value': int, # количество денег
  'call': bool, # можем ли позвонить? 
  'worked': bool, # можем ли работать? 
  'covid': bool, # заражены? 
}

```
