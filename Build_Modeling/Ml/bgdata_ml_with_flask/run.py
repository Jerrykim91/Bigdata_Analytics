
# febric3을 이용하여 리눅스 서버에 자동 셋업 
# 리눅스, git, 페브릭으로 작성된 스크립트 
# 사용화시, 최초 셋업 및 업데이트 관리시 사용 

#####

# 본파일은 엔트리 파일 (수행 진입로)

from service.start import app


if __name__ == '__main__':
    app.run(debug=True)