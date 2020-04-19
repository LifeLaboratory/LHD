import app.base.provider as bp


class Provider(bp.Provider):
    def __init__(self):
        super().__init__()
        self.table_name = 'rating'
        self.field = ['login, password, name', 'email']

    def get_top_users(self):
        self.query = f'''
  with get_users as(
      select
        distinct id_user
      from game
  )
  select
    gu.*
    , g.*
    , u.login as name
    , p.name as title 
    , p.description
    , p.pic
  from get_users gu
  join users u using(id_user)
  join lateral (
      select
        time_close as time
        , health
        , food
        , leisure
        , communication
        , point
        , value
        , id_person
      from game g
      where g.id_user = gu.id_user
      order by point desc
      limit 1
  ) g on True
  join person p using(id_person)
  order by point desc
'''
        return self.execute()
