# 서버 열기 => 

from flask import Flask, render_template, request, redirect
import cx_Oracle as oci  # conda install cx_Oracle

#--------------------------------------------------------------
# 아이디/암호@서버주소:포트번호/SID **
conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding="utf-8")
# Connection 으로부터 Cursor(커서) 생성
cursor = conn.cursor()
print('==checkpoint==')
#--------------------------------------------------------------

app = Flask(__name__)

# index 화면 
@app.route("/")
def index():
    return " index page"

# get, post 
# 크롬으로 친건 => get 
@app.route("/join",methods=['GET'] )
def join():

    # 화면 보여줘 
    return render_template('join.html')

# 회원가입 누르면 
@app.route("/join", methods=['POST']) # POST 에서는 렌더링 하면 안된다 .
def join_post():

#--------------------------------------------------------------
    # DB에 값을 넣고 
    ID   = request.form['id']
    PW   = request.form['pw']
    NAME = request.form['name']
    AGE  = request.form['age']
    print("=={}:{}:{}:{}==".format(ID,PW,NAME,AGE))
    sql = "INSERT INTO MEMBER VALUES(:id, :pw, :na, :ag, SYSDATE)"
    cursor.execute(sql, id=ID, pw=PW, na=NAME, ag=AGE  )
    conn.commit()
#--------------------------------------------------------------


# 오라클 DB 접속
# 추가 sql문 작성 => insert, select, ,  
# sql문 수행
    
    # http://127.0.0.1/ 크롬에서 입력한거처럼 동작 
    # 메인 화면으로 이동 
    return redirect('/')
    # return render_template('join.html') => 렌더링 

if __name__ == '__main__':
    app.run(debug=True)
# Dev시에는 debug = True 배포시에는 debug = False
