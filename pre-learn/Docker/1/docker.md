### *참고  링크
https://docs.docker.com/get-started/docker-overview/#docker-architecture


# 1. Docker란 무엇인가요?
- Docker는 애플리케이션 개발, 배포 및 실행을 위한 개방형 플랫폼입니다. 
- Docker를 사용하면 애플리케이션과 인프라를 분리하여 소프트웨어를 신속하게 배포할 수 있습니다. 
- Docker를 사용하면 애플리케이션을 관리하는 것과 같은 방식으로 인프라를 관리할 수 있습니다. 
- Docker의 코드 배포, 테스트 및 배포 방법론을 활용하면 코드 작성과 프로덕션 실행 간의 지연 시간을 크게 줄일 수 있습니다.

# 2. 도커 아키텍처
Docker는 클라이언트-서버 아키텍처를 사용합니다. Docker 클라이언트는 Docker 데몬과 통신하며, 데몬은 Docker 컨테이너를 빌드, 실행 및 배포하는 중요한 작업을 수행합니다. 
Docker 클라이언트와 데몬은 동일한 시스템에서 실행될 수도 있고, Docker 클라이언트를 원격 Docker 데몬에 연결할 수도 있습니다. 
Docker 클라이언트와 데몬은 REST API, UNIX 소켓 또는 네트워크 인터페이스를 사용하여 통신합니다. 
또 다른 Docker 클라이언트인 Docker Compose를 사용하면 컨테이너 집합으로 구성된 애플리케이션을 작업할 수 있습니다.

![alt text](image.png)

