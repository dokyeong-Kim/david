# 🐳 Docker `hello-world` 실습 정리

이 문서는 `hello-world` 이미지를 활용하여 Docker 환경을 점검하고, 컨테이너 및 이미지 관련 명령어를 실습한 전체 과정을 정리한 문서입니다.

---

## ✅ 1. `hello-world` 이미지 실행

```bash
docker run hello-world
```

- 이미지를 처음 실행하면 자동으로 다운로드됩니다.
- 성공적으로 설치되었을 경우, 아래 메시지가 출력됩니다:

```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

---

## ✅ 2. 이미지 목록 확인

```bash
docker images
```

예시 출력:

```
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    ec153840d1e6   6 months ago   17kB
```

---

## ✅ 3. 컨테이너 목록 확인

```bash
docker ps -a
```

예시 출력:

```
CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      NAMES
7e0c438f565c   hello-world   "/hello"   15 minutes ago   Exited (0) 15 minutes ago   youthful_kapitsa
```

---

## ✅ 4. 컨테이너 상세 정보 확인

```bash
docker inspect <컨테이너_ID>
```

예시:

```bash
docker inspect 7e0c438f565c
```

---

## ✅ 5. 이미지 히스토리 확인

```bash
docker history hello-world
```

예시 출력:

```
IMAGE          CREATED        CREATED BY                SIZE      COMMENT
ec153840d1e6   6 months ago   CMD ["/hello"]            0B        buildkit.dockerfile.v0
<missing>      6 months ago   COPY hello / # buildkit   12.3kB    buildkit.dockerfile.v0
```

---

## ✅ 6. 컨테이너 삭제

```bash
docker rm <컨테이너_ID>
```

---

## ✅ 7. 이미지 삭제

컨테이너가 모두 삭제되어야 이미지 삭제 가능:

```bash
docker rmi <이미지_ID>
```

필요시 강제 삭제:

```bash
docker rmi -f <이미지_ID>
```

---

## 🔁 참고 명령어 요약

```bash
docker ps -a             # 모든 컨테이너 보기
docker images            # 모든 이미지 보기
docker rm <ID>           # 컨테이너 삭제
docker rmi <ID>          # 이미지 삭제
docker inspect <ID>      # 상세 정보 확인
docker history <이미지>  # 이미지 히스토리 보기
```
