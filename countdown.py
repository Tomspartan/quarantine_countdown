from flask import Flask
from datetime import date
app = Flask(__name__)

@app.route('/')
def countdown():
    qdate = date(2020,3,16)
    today = date.today()
    delta = today - qdate
    return f"It is now day {delta.days} of quarantine."

if __name__ == '__main__':
    app.run()