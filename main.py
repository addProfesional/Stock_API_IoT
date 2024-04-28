# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.server  import iniciar, ssl_context
from src.database.Database import db
import os

app = iniciar()

with app.app_context():
    db.create_all()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    useSSL = os.environ.get('USE_SSL_TLS')
    if useSSL == True:
        print('Servidor usando SSL...')
        app.run(debug=True, ssl_context=ssl_context,  host='0.0.0.0')
    else:
        print('Servidor no usa SSL...')
        app.run(debug=True, host='0.0.0.0')

    #app.run()
    #app.run(debug=True, ssl_context=ssl_context)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
