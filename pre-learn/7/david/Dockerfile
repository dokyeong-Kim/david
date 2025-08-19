# 1. 적절한 리눅스 기반 Python 베이스 이미지 사용 (slim은 경량화 버전)
FROM python:3.9-slim

# 2. 작업 디렉토리를 /app 으로 설정
WORKDIR /app

# 3. 현재 작업 디렉토리의 모든 파일을 컨테이너의 /app으로 복사
COPY . .

# 4. requirements.txt 파일을 이용해 필요한 패키지 설치
# --no-cache-dir 의미: pip이 설치 중 생기는 임시 캐시 파일 저장X 명령 -> 임시 캐시 파일 없어야 이미지 크기 감소
RUN pip install --no-cache-dir -r requirements.txt

# 5. 컨테이너에서 사용할 포트 정의
EXPOSE 80

# 6. 컨테이너 시작 시 실행할 명령어
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:80"]

# * gunicorn: WSGI(Python 웹 앱과 웹 서버 간 연결 표준) 서버, WHY: Flask 같은 앱은 개발 서버만 제공 → 실제 배포 시엔 WSGI 서버가 필요
# * main:app: main.py 안에 있는 app이라는 객체를 실행
# * --bind 0.0.0.0:80: 컨테이너의 모든 IP(0.0.0.0)에서 요청을 받아서 80번 포트로 서비스하겠다는 뜻
