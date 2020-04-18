# Структуруа базы данных

### Пользователь
```sql
  'id_user': str,
  'login': str,
  'password': str
```

### Игра
```sql
  'id_game': int,
  'id_user': int,
  'id_question': int,
  'time_open': timestamp,
  'time_close': timestamp,
  'time_close': timestamp,
  'round': int, # Номер раунда игры
  'Health': float,   # Здоровье
  'food': float,     # Питание
  'Leisure': float,  # Досуг
  'Communication': float,   # Общение
  'point': int, # количество очков
  'value': int, # количество денег
```


### Вопросы
```sql
  'id_question': int,
  'description': text,
  'left': {
    'Health': float,   # Здоровье
    'food': float,     # Питание
    'Leisure': float,  # Досуг
    'Communication': float,   # Общение
    'point': int, # количество очков
    'value': int, # количество денег
  },
  'right': {
    'Health': float,   # Здоровье
    'food': float,     # Питание
    'Leisure': float,  # Досуг
    'Communication': float,   # Общение
    'point': int, # количество очков
    'value': int, # количество денег
  }
```


### Персонажи
```sql
  'id_person': int,
  'name': str,
  'description': str, # описание персонажа
  'pic': str # ссылка на картинку
```


### Сессии пользователей
```sql
  'id_user': int,
  'id_session': text
```


### События
```sql
  'id_event': int,
  'description': text,
  'id_session': text
```

