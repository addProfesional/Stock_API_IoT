# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.server  import iniciar, ssl_context
from src.database.Database import db

app = iniciar()

with app.app_context():
    db.create_all()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #app.run()
    app.run(debug=True, ssl_context=ssl_context)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
