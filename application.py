from flask import Flask, escape, request
import sqlite3
import os

VERSION='0.3.4'

print('hilo'+VERSION)

# conn = sqlite3.connect('/db-data/chinook.db')

# c = conn.cursor()
# c.execute("SELECT * FROM artists")
# print(c.fetchall())


# print(os.getcwd())
# print(os.listdir('/web-data/'))

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'hi {VERSION}, {escape(name)}!'


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=80)
