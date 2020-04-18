import app.base.provider as bp


class Provider(bp.Provider):
    def __init__(self):
        super().__init__()
        self.table_name = 'game'
        self.field = []

    def start_game(self, data):
        """
        Метод запускает новую игру
        :param data:
        :return:
        """
        self.query = f'''
  insert into "{self.table_name}"
  (
    id_user
    , id_question
    , health
    , food
    , leisure
    , communication
    , value
    , id_person
  )
  values (
    {data.get('id_user')}
    , {data.get('id_question')}
    , coalesce({data.get('health')}, 10)
    , coalesce({data.get('food')}, 10)
    , coalesce({data.get('leisure')}, 10)
    , coalesce({data.get('communication')}, 10)
    , coalesce({data.get('value')}, 10)
    , {data.get('id_person')}
  )
  returning id_game
        '''
        return self.execute()

    def get_next_question(self, data):
        """
        Метод выбирает следующий вопрос для пользователя
        :return:
        """
        self.query = f'''
  with question_count as (
    select count(1)
    from question
  )
  select *
  from question
  where id_question = random()*((select count from question_count limit 1)-1)+1
  limit 1
'''
        return self.execute()

    def get_game(self):
        """
        Метод получает информацию о текущей игре пользователя
        :return:
        """
        pass

    def close_old_game(self, data):
        """
        Метод заканчивает старую игру пользователя
        :param data:
        :return:
        """
        self.query = f'''
  update game
    set time_close = now()
    where "id_user" = {data.get('id_user')}
      and time_close is Null
'''

    def get_question(self):
        """
        Метод возвращает текущий вопрос для игры
        :return:
        """
        pass

    def check_question(self, data):
        """
        Метод проверяет, верно ли ответил пользователь
        :param data:
        :return:
        """
        pass

