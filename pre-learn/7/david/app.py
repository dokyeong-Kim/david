from flask import Flask, render_template, request   # Flask 웹 프레임워크에서 필요한 모듈 가져오기
from gtts import gTTS                               # Google Text-to-Speech 모듈 가져오기
import base64                                       # 음성 데이터를 브라우저에서 재생 가능하도록 인코딩하는 데 사용
import io                                           # 메모리에서 파일 객체를 다루기 위한 모듈
import datetime                                     # 로그에 시간 기록을 위한 모듈
import re                                           # 정규표현식 모듈 (입력 검증용)

# 사용자 정의 예외 클래스 정의 (입력 검증 실패 시 사용)
class ValidationError(Exception):
    pass

# 허용된 문자 정규표현식 (언어별 문자셋)
# 각 언어에 맞는 문자만 입력되도록 제한
STRICT_CHARSETS = {
    'ko': r'^[가-힣\s]+$',                       # 한글 + 공백 허용
    'en': r'^[a-zA-Z\s]+$',                     # 영어 + 공백 허용
    'ja': r'^[ぁ-んァ-ン一-龥\s]+$',             # 일본어 + 공백 허용
    'es': r'^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]+$',       # 스페인어 + 공백 허용
}

# 입력 유효성 검사를 예외 방식으로 구현
def validate_input(text, lang):
    if not text.strip():
        raise ValidationError("⚠️ 텍스트를 입력해주세요.")

    if lang not in STRICT_CHARSETS:
        raise ValidationError("⚠️ 지원하지 않는 언어가 선택되었습니다.")

    pattern = STRICT_CHARSETS[lang]
    if not re.fullmatch(pattern, text):
        raise ValidationError("⚠️ 입력 내용과 선택한 언어가 일치하지 않거나 허용되지 않는 문자가 포함되어 있습니다.")

# Flask 애플리케이션 생성
app = Flask(__name__)

# 허용된 언어 코드 목록 정의
ALLOWED_LANGUAGES = {'ko', 'en', 'ja', 'es'}

# 루트 경로 ('/')에 대한 라우팅 정의
# 라우팅: 네트워크에서 경로를 선택하는 프로세스
# GET 요청 시: 입력 폼 페이지 렌더링 (서버에서 데이터 요청)
# POST 요청 시: TTS 변환 수행 및 결과 출력 (서버에 데이터 제출 or 생성 시 사용)
@app.route('/', methods=['GET', 'POST'])
def index():
    # POST 요청인 경우
    if request.method == 'POST':
        # 입력된 텍스트를 폼 데이터에서 가져옴
        # strip() : 공백 제거 포함
        text = request.form.get('input_text', '').strip()
        # 선택된 언어(lang)를 폼 데이터에서 가져옴
        # 기본값은 한국어(ko)
        lang = request.form.get('lang', 'ko')

        try:
            # 언어와 입력 텍스트 유효성 검사 (문제 있으면 예외 발생)
            validate_input(text, lang)

            # gTTS 객체 생성 후 음성 변환 수행
            tts = gTTS(text=text, lang=lang)    # 사용자 입력과 언어로 gTTS 객체 생성
            mp3_fp = io.BytesIO()               # 메모리 버퍼에 저장할(=임시 저장할) 파일 객체 생성
            tts.write_to_fp(mp3_fp)             # gTTS로 생성한 음성 데이터를 메모리에 저장
            mp3_fp.seek(0)                      # 파일 포인터를 처음으로 이동시켜 데이터 전체 접근

            # mp3 데이터를 base64 인코딩하여 HTML에서 재생 가능하도록 변환
            encoded_audio = base64.b64encode(mp3_fp.read()).decode('utf-8')

            # 사용자 입력 로그 파일에 저장 (input_log.txt)
            with open("input_log.txt", "a", encoding="utf-8") as log_file:
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log_file.write(f"[{timestamp}] Text: {text} | Lang: {lang}\n")

            # 변환된 음성과 함께 템플릿(index.html) 렌더링 -> 사용자에게 바로 재생되는 오디오 제공 + 저장 링크
            return render_template("index.html", audio=encoded_audio, audio_filename="tts_output.mp3")

        # 입력 유효성 검사 실패 또는 gTTS 예외 발생 시 에러 메세지 출력
        except ValidationError as ve:
            return render_template("index.html", error=str(ve))
        except Exception:
            return render_template("index.html", error="⚠️ 음성 변환에 실패했습니다.")

    # GET 요청일 경우: 음성 입력 폼만 렌더링하여 사용자에게 보여줌
    # 웹사이트 처음 접속 시
    else:
        return render_template("index.html")
    
# '/menu' 라우트: menu.html 페이지를 렌더링
# 문제5에서 요구한 메뉴 화면 추가 기능에 해당합니다.
@app.route('/menu')
def menu():
    # 'templates' 폴더에 있는 'menu.html' 파일을 렌더링하여 반환합니다.
    return render_template('menu.html')

# Flask 애플리케이션 실행 설정
# host='0.0.0.0': 외부 접속 허용, port=80: 포트 80번 고정
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)