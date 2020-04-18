from app import app
from app.users import view


if __name__ == "__main__":
    app.run(debug=True, port=80)
