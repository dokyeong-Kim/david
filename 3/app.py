# Flask는 웹 서버를 만들기 위한 pythom 프레임워크
from flask import Flask, request, Response

# 운영체제 환경변수 사용을 위해 os 모듈 import
import os

# BytesIO는 메모리 버퍼(파일처럼 작동하느냬를 생성할 수 있게 해주는 도구
# 나중에 gTTS로 생성된 mp3 형태로 저장되는데, 파일을 만들고 싶지 않기 때문에 진짜 파일을 안만들고 파일처럼 저장할 수 있게 해주는 도구
from io import BytesIO

# gTTS : Google Text-to-Speech API (텍스트 to 음성 변환 라이브러리)
from gtts import gTTS
# 기본 언어 설정을 가져온다. 환경변수 'DEFAULT_LANG'가 없으면 'ko'(한국어)로 설정
# os.getenv(environment variable)가 운영체제에 설정된 환경변수 값을 꺼내오는 함수
DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')

# Flask 애플리케이션 인스턴스를 생성
app = Flask(__name__)

# "/" 경로에 접근했을 때 실행되는 함수 정의
@app.route('/')
def home():
    # 음성으로 변환할 텍스트 정의
    text = "Hello. DevOps"

    # 사용자가 URL에 lang 파라미터를 넣으면 그 값을 사용하고, 없으면 기본값 사용
    # *args는 요청 중에 쿼리 문자열 부분만 딕셔너리 처럼 제공하는 속성
    # *쿼리 파라미터란 URL에 ? 뒤에 오는 부분으로
    # 예: http://localhost/?lang=en
    # request.args.get('lang')는 URL에서 'lang' 파라미터의 값을 가져오고, 없으면 DEFAULT_LANG를 사용
    lang = request.args.get('lang', DEFAULT_LANG)

    # 메모리 위에 mp3 파일을 담기 위한 가상의 파일 객체 생성
    fp = BytesIO()

    # 텍스트를 mp3로 변환해 BytesIO 버퍼에 저장
    # gTTS(text, lang=lang).write_to_fp(fp) 가 올바른 코드라고 함
    gTTS(text, lang=lang).write_to_fp(fp)

    # mp3 데이터를 클라이언트 응답으로 보냄. 브라우저가 바로 음성 재생
    return Response(fp.getvalue(), mimetype='audio/mpeg') #페이지 전달 없이 바로 재생

# 직접 실행했을 때만 Flask 서버를 실행
if __name__ == '__main__':
    # 모든 네트워크에서 접근 가능하고, 포트는 80 -> 5000)
    app.run('0.0.0.0', 5000)