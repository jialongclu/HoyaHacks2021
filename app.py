from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {"HoyaHacks": "2021"}

if __name__ == '__main__':
    app.run(debug=True)