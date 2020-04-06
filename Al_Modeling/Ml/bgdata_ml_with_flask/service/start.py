
# 플라스크 
#---------------------------------------------------------
# 플라스크 기본구성 

# 1. 모듈 가지고오기 
from flask import Flask, render_template, request, jsonify
from service.ml import detect_lang
# entry가 run.py이면 
# from service.ml import detect_lang
# 2. flask 객체 생성
app = Flask(__name__)

# 3. 라우팅 
@app.route('/')
def home():
    return ' Hello Flask' 

# 3-1. 언어감지 처리 
# GET방식만 현재 되어 잇는데, POST도 지원하겟다
# 1개의 url로 여러 메소드를 지원 => restful
@app.route('/langTypeDetect',methods=['GET', 'POST'])
def langTypeDetect():
    if request.method == "POST":
        # 1. 원문 데이터 획득 (get, post방식으로 전달된 데이터 확득)
        # 인덱싱기법을 사용하지 않고, 함수로 값을 추출한다
        # 오류 발생시 에러가 나오지 않고, None으로 리턴되어 처리가능
        # print(request.form.get('ori1'))
        oriTxt = request.form['ori']
        print(request.form)

        if not oriTxt:
            return jsonify({'code':0, 'lang':'', 'desc':'원문데이터 누락'})
            
        # 2. 언어 감지
        lang, desc = detect_lang( oriTxt )
        # 2-1. 디비에 로그처리
        # 3. 응답
        return jsonify({'code': 1, 'lang':'en', 'desc':'영어'})
    else:
        # GET
        return render_template('index.html')

# 4. 서버 가동 
if __name__ == '__main__':
    app.run(debug=True)

#---------------------------------------------------------