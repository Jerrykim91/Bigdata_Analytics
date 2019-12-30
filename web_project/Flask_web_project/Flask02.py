# 서버 열기 => 

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return " index page"


@app.route("/join")
def join():
    return " join page"


if __name__ == '__main__':
    app.run(debug=True)
# Dev시에는 debug = True 배포시에는 debug = False
