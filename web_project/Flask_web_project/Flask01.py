# 서버 열기 

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return " index page"

print(__name__) # __main__ 

# 메인 인지 아닌지 판별 
if __name__ == '__main__':
    app.run()