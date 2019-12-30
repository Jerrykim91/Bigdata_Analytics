
from flask import Flask, render_template, request, redirect
import cx_Oracle as oci  # conda install cx_Oracle

conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding="utf-8")
cursor = conn.cursor()
print('==checkpoint==')


app = Flask(__name__)


@app.route("/")
def index():
    sql = "SELECT * FROM MEMBER"
    cursor.execute(sql)
    data = cursor.fetchall() #[(),(),()]
    #return render_template('list.html', list = data )
    print('==check point1==')
    # k = 0
    # for i in data:
    #     j = i[3] # 인덱싱
    #     #print(j)
    #     k += j
    # print(k)
    sum = 0 # 안에 들어가는거랑 밖에 있는거랑 차이가 나네 
    for tmp in data:
        sum += tmp[3]
    print(sum)


    print('==check point2==')
    print(type(data))
    #print(data)
    return "index page"


@app.route("/join",methods=['GET'] )
def join():
    return render_template('join.html')


@app.route("/join", methods=['POST']) 
def join_post():

    ID   = request.form['id']
    PW   = request.form['pw']
    NAME = request.form['name']
    AGE  = request.form['age']
    print("=={}:{}:{}:{}==".format(ID,PW,NAME,AGE))
    sql = "INSERT INTO MEMBER VALUES(:id, :pw, :na, :ag, SYSDATE)"
    cursor.execute(sql, id=ID, pw=PW, na=NAME, ag=AGE  )
    conn.commit()

    return redirect('/')
  
if __name__ == '__main__':
    app.run(debug=True)

