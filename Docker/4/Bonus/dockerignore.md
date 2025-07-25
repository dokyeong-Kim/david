# 📦 .dockerignore 파일의 목적과 필요성

## ✅ .dockerignore란?

`.dockerignore` 파일은 Docker 이미지 생성 시 **불필요한 파일이나 디렉토리를 제외**하기 위한 설정 파일입니다.  
`Dockerfile`의 `COPY` 또는 `ADD` 명령어가 실행될 때, `.dockerignore`에 정의된 항목들은 **컨테이너 이미지에 복사되지 않습니다.**

---

## 🎯 왜 사용하는가?

### 1. 이미지 최적화
- 실행에 필요하지 않은 파일들이 포함되지 않아 Docker 이미지의 **용량을 줄일 수 있습니다.**
- 불필요한 복사 작업이 줄어들어 **빌드 속도가 향상**됩니다.

### 2. 보안 강화
- `.git/` 디렉토리는 내부 커밋 이력이나 민감한 데이터가 포함될 수 있으므로, **이미지에 포함되면 보안에 취약**할 수 있습니다.

### 3. 빌드 성능 개선
- 빌드 컨텍스트에 포함되는 파일 수가 줄어들어 Docker가 처리해야 할 데이터 양이 줄고, **속도가 빨라집니다.**

---

## 📄 예시: .dockerignore 파일 내용

```dockerignore
.git
.gitignore
.dockerignore
Dockerfile
```

## 📌 제외 대상 설명
- .git/:	Git 저장소 관련, 실행에 필요 없고 보안 위험 존재
- .gitignore:	Git 설정 파일, 컨테이너 실행과 무관
- .dockerignore:	Docker 빌드 설정 파일, 컨테이너 실행에 필요 없음
- Dockerfile:	이미지 빌드시만 사용, 이미지 내부에 필요 없음

## ✅ 요약
.dockerignore는 .gitignore처럼 작동하여,
이미지 용량 최적화, 보안 강화, 빌드 속도 향상에 중요한 역할을 합니다.

**잘 정리된 .dockerignore는 효율적인 Docker 환경을 만드는 핵심 요소입니다.**