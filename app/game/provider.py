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
        return self.execute()[0]

    def get_game(self, id_user):
        """
        Метод получает информацию о текущей игре пользователя
        :return:
        """
        self.query = f'''
  with get_game as (
    select 
      id_question
      , round
      , health
      , food
      , leisure
      , communication
      , value
      , id_person
    from game
    where id_user = {id_user}
      and time_close is null
  )
  select 
    gg.*
    , q.description
    , q.left->>'description' as left_answer 
    , q.right->>'description' as right_answer 
    , p.name
    , p.pic
  from get_game gg
    join question q using(id_question)
    join person p using(id_person)
  limit 1
'''
        return self.execute()

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
        self.execute()

    def update_game_status(self, data):
        """
        Метод обновляет текущую игру
        :param data:
        :return:
        """
        self.query = f'''
  update game
    set 
      round = {data.get('round')}
      , health = {data.get('health')}
      , food = {data.get('food')}
      , leisure = {data.get('leisure')}
      , communication = {data.get('communication')}
      , point = {data.get('point')}
      , id_question = {data.get('id_question')}
    where "id_game" = {data.get('id_game')}
      and time_close is Null
        '''
        self.execute()

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
        self.query = f'''
  with question_count as (
    select count(1)
    from question
  ),
  new_question as (
    select *
    from question
    where id_question = random()*((select count from question_count limit 1)-1)+1
    limit 1
  ),
  get_game as (
    select 
      nq.id_question
      , id_game
      , round + 1 as round
      , greatest(0, g.health + (q.{data.get('answer')}->>'health')::int) as health
      , greatest(0, g.food + (q.{data.get('answer')}->>'food')::int) as food
      , greatest(0, g.leisure + (q.{data.get('answer')}->>'leisure')::int) as leisure
      , greatest(0, g.communication + (q.{data.get('answer')}->>'communication')::int) as communication
      , g.point + (q.{data.get('answer')}->>'point')::int as point
      , id_person
    from game g, new_question nq
     left join question q using(id_question)
    where id_user = {data.get('id_user')}
      and time_close is null
    limit 1
  )
  select 
      gg.*
    , q.description
    , q.left->>'description' as left_answer 
    , q.right->>'description' as right_answer 
    , p.name
    , p.pic
  from get_game gg
    join question q using(id_question)
    join person p using(id_person)
  limit 1
'''
        return self.execute()
