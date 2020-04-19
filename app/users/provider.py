import app.base.provider as bp


class Provider(bp.Provider):
    def __init__(self):
        super().__init__()
        self.table_name = 'users'
        self.field = ['login', 'password']

    def create(self, data):
        self.query = f'''
  insert into "{self.table_name}"
  (login, password)
  values (
    '{data.get('login')}'
    , '{data.get('password')}'
  )
  returning id_user
'''
        return self.execute()

    def check_user(self, data):
        where = f'''
  where true
    and '{data.get('login')}' = "login"
  limit 1
'''
        user = self.users(where)
        return user[0] if user else None

    def login(self, data):
        where = f'''
  where true
    and '{data.get('login')}' = "login"
    and '{data.get('password')}' = "password"
  limit 1
        '''
        user = self.users(where)
        return user[0] if user else None

    def profile(self, id_user):
        self.query = f'''
with info_user_game as (
    select
      id_user
      , count(1) as count_game
      , max(round) as max_point
    from game
    group by id_user
),
position_user as (
  select
      id_user
    , ROW_NUMBER () over (
        order by max_point
      ) as rating
  from info_user_game
  order by 2
),
game_history as (
  select
    array_agg(
        json_build_object(
            'id_game', id_game,
            'time', time,
            'round', round,
            'health', health,
            'food', food,
            'leisure', leisure,
            'communication', communication,
            'point', point,
            'pic', pic,
            'title', name
            )
        )
  from (
    select id_game
         , time_close as time
         , round
         , g.health
         , g.food
         , g.leisure
         , g.communication
         , point
         , p.pic
         , p.name
    from game g
    left join person p using(id_person)
    where id_user = {id_user}
    order by 2 desc nulls first
  ) g
)
select
  id_user
  , login as names
  , rating
  , coalesce(count_game, 0) as count_game
  , coalesce(max_point, 0) as max_point
  , pic
  , coalesce((select * from game_history limit 1), '{{}}'::json[]) as game_history
from users u
left join info_user_game iug using(id_user)
left join position_user pu using(id_user)
where id_user = {id_user}
limit 1
'''
        return self.execute()

    def users(self, where='where True'):
        self.query = f'''
  select 
    id_user
    , login
  from "{self.table_name}"
  {where}
        '''
        return self.execute()
