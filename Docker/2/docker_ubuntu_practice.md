# 🧪 Ubuntu 20.04 실습 단계별 정리

## 📦 1. Ubuntu 이미지 검색 및 확인

### ✅ Docker 명령어로 Ubuntu 이미지 검색
```bash
docker search ubuntu
```

### ✅ DockerHub에서 ubuntu 검색
- 사이트: https://hub.docker.com/_/ubuntu
- **Overview 탭**에서 정보 확인
- “Docker Official Image” 로고 확인 (✅ 공식 이미지임)

---

## ⬇️ 2. Ubuntu 20.04 이미지 다운로드 및 정보 확인

### ✅ `20.04` 태그 확인
- DockerHub의 `Tags` 탭에서 `20.04` 검색

### ✅ 이미지 다운로드
```bash
docker pull ubuntu:20.04
```

### ✅ 이미지 상세 정보 확인
```bash
docker inspect ubuntu:20.04
```

### ✅ 이미지 히스토리 출력
```bash
docker history ubuntu:20.04
```

---

## 🚀 3. 컨테이너 실행 및 파일 생성 테스트

### ✅ Ubuntu:20.04 이미지로 bash 쉘과 함께 컨테이너 실행
```bash
docker run -it --name test ubuntu:20.04 bash
```

### ✅ 컨테이너 내부에서 파일 생성
```bash
echo "hello docker" > /test.txt
```

### ✅ 생성된 파일 확인
```bash
ls 
cat /test.txt
```

### ✅ bash 종료 및 컨테이너 삭제
```bash
exit
docker rm test
```

---

## 🔁 4. 파일 유지 여부 확인

### ✅ 동일 이름으로 컨테이너 재실행
```bash
docker run -it --name test ubuntu:20.04 bash
```

### ✅ 이전에 생성한 파일이 유지되지 않음 확인
```bash
ls 
```

---

## 💡 배운 점: Docker 개념 요약

- 컨테이너는 이미지에서 새롭게 **생성되는 일회성 환경**이다.
- 컨테이너 내부에서 만든 데이터는 **삭제되면 사라짐** (영속성 없음).
- 같은 이미지에서 컨테이너를 다시 실행하면 **초기 상태**에서 시작됨.
- 파일이나 상태를 유지하려면 **볼륨 또는 커밋 이미지**를 사용해야 함.

---
