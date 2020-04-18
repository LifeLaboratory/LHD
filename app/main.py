from app import app
from app.users import view
from app.person import view
from app.rating import view
from app.game import view


if __name__ == "__main__":
    app.run(debug=True, port=80)
