# 1. 임포트 import (flask , cx_Oracle)
# 1.1  아이디/암호@서버주소:포트번호/SID **
# 오라클.커낵트('admin/1234@192.168.99.100:32764/xe',encoding="utf-8")
# 위의 코드를 변수에 담고 Connection 으로부터 Cursor(커서) 생성
# 2. 메인 페이지 생성 (/)
# 3. 로그인 페이지 생성 (/login) = > get, post 이용 
# 4. get  => html을 통해서 페이지만 show 
# 5 .post => login. html 통해서 사용자 값을 받고 DB로 전달하는 과정 
# (5.1. 제대로 도는지 확인 하기 위해서 'check point'를 만든다.)
# 5.2.1 사용자로 부터 받은 값을 DB로 전달하여 업데이트 한다. 
# 5.2.2 전달하고자하는 값(request.form['id'])을 변수에 담고 
# sql 문을 작성 하고 변수에담아 커서.실행(sql, 전달하는 값 )
# cx_Oracle 커넥해서 커밋 !
# (5-1. 제대로 도는지 확인 하기 위해서 'check point'를 만든다.)
# 6. show =>  main page 혹은 wellcom page  
# 7. if __name__ == '__main__':app.run(debug=True)





from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@ app.route('/')
def main() : 
    return " home page"


@ app.route('/login', methods=['GET'])
def login() : 
    return render_template('login.html')

@ app.route('/login', methods=['POST'])
def login_past() : 
    print('check posting')
    return redirect('/')

if __name__ == '__main__':app.run(debug=True)




