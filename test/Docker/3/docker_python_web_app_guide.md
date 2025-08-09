
# Python 웹 앱 컨테이너 실행 및 이미지 저장 과정

작성일: 2025-07-25

---

## ✅ 과정 개요

DockerHub에서 `python:3` 이미지를 기반으로 웹 앱을 실행하고, 실행된 컨테이너를 이미지로 저장하여 재사용하는 과정을 정리한 문서입니다.

---

## 📌 1. python:3 이미지 다운로드

```bash
docker pull python:3
```

---

## 📌 2. 컨테이너 실행

- 컨테이너 이름: `python3-test`
- 포트 설정: `호스트 8000 → 컨테이너 80 포트`
- bash 쉘 접속

```bash
docker run -it -p 8000:80 --name python3-test python:3 bash
```

---

## 📌 3. 다른 터미널에서 프로젝트 디렉토리 복사

- 복사할 로컬 경로: `~/Documents/AI-codyssey/7/david`
- 복사 대상 컨테이너: `python3-test`
- 복사 위치: `/app`

```bash
docker cp ~/Documents/AI-codyssey/7/david python3-test:/app
```

---

## 📌 4. 컨테이너 접속 후 앱 실행

```bash
docker exec -it python3-test bash
cd /app
#pip install -r requirements.txt
python3 app.py
```

웹브라우저에서 접속 주소: `http://localhost:8000`

---

## 📌 5. 컨테이너 실행 중 이미지 저장

다른 터미널에서 아래 명령어 실행:

```bash
docker commit python3-test python_david
```

이미지 저장 확인:

```bash
docker images
```

---

## 📌 6. 실행 로그 예시

```
192.168.65.1 - - [25/Jul/2025 07:22:04] "GET / HTTP/1.1" 200 -
192.168.65.1 - - [25/Jul/2025 07:22:04] "GET /static/david.jpg HTTP/1.1" 200 -
192.168.65.1 - - [25/Jul/2025 07:22:05] "GET /favicon.ico HTTP/1.1" 404 -
```

---

## ✅ 배운 점 요약

- `docker cp`: 로컬 파일을 컨테이너로 복사할 수 있다.
- `docker exec -it ... bash`: 컨테이너 내부에서 명령어 실행 가능
- `docker commit`: 현재 상태의 컨테이너를 이미지로 저장하여 재사용 가능
- 컨테이너가 실행 중인 상태에서도 다른 터미널에서 docker 명령어 사용 가능

---

