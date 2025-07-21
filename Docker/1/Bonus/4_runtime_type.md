# 컨테이너 런타임 종류 (CNCF Landscape 기준)

컨테이너 런타임(Container Runtime)은 컨테이너를 생성하고 실행하는 데 필요한 저수준 기능을 제공하는 핵심 구성요소입니다. CNCF Landscape에는 여러 런타임이 소개되어 있으며, 대표적으로 다음 3가지가 많이 사용됩니다.

---

## 1. containerd

- **설명**: Docker에서 분리되어 CNCF 프로젝트로 독립한 고성능 컨테이너 런타임입니다.
- **특징**
  - OCI(Open Container Initiative) 표준 준수
  - Kubernetes와 통합 가능 (CRI plugin 제공)
  - 이미지 pull, 컨테이너 실행/중지 등 다양한 기능 내장
- **사용 예**: Docker, Kubernetes (기본 런타임으로 사용)

🔗 https://containerd.io

---

## 2. CRI-O

- **설명**: Kubernetes에서만 사용할 수 있도록 설계된 컨테이너 런타임으로, 경량화와 보안에 중점을 둠.
- **특징**
  - Kubernetes CRI(Container Runtime Interface)를 직접 구현
  - containerd보다 더 작고 단순
  - runc를 실행 엔진으로 사용
- **사용 예**: Red Hat OpenShift, Fedora CoreOS 등

🔗 https://cri-o.io

---

## 3. gVisor

- **설명**: Google에서 개발한 보안 중심의 샌드박스형 컨테이너 런타임
- **특징**
  - 사용자 공간에서 커널 인터페이스를 직접 구현
  - 완전한 커널 격리 제공 → VM 수준의 보안
  - 성능은 다소 떨어지지만 보안이 중요한 환경에 적합
- **사용 예**: 보안이 중요한 서비스, 클라우드 플랫폼

🔗 https://gvisor.dev

---

## 🔚 요약

| 런타임     | 특징 요약                        | 주요 사용처          |
|------------|-----------------------------------|------------------------|
| containerd | Docker에서 파생, 범용 고성능 런타임 | Docker, Kubernetes     |
| CRI-O      | Kubernetes 전용, 경량 런타임       | OpenShift 등           |
| gVisor     | 사용자 공간 커널로 보안 강화       | 클라우드 보안 환경 등 |

---

🔗 참고  
- CNCF Landscape: https://landscape.cncf.io  
- Open Container Initiative: https://opencontainers.org/

---

# containered에 대해
## 🧩 “추상화”란?

**복잡한 내부 동작을 감추고, 사용자는 단순한 인터페이스만 사용하는 것을 말해요.**

예시:
docker run hello-world 이렇게 한 줄로 입력하면,
내부적으로는 다음 작업이 자동으로 일어나요:

이미지가 없다면 자동으로 다운로드 (docker pull)

컨테이너를 생성

설정 구성 (파일 시스템, 환경변수, 네트워크)

명령어 실행 (/hello 같은 실행 파일)

이 모든 걸 직접 일일이 처리하지 않고, docker run 한 줄이면 다 해주는 거예요.
👉 이게 바로 **컨테이너 생성 과정을 "추상화"**한 것이에요.

---
## ⚙️ “자동화”란?

**매번 반복되는 설정을 사람이 하지 않아도 시스템이 자동으로 처리하는 걸 말해요.**

컨테이너 이름 자동 생성 (nifty_carver, youthful_kapitsa 등)

포트 바인딩이나 네트워크 설정 기본값 제공

이미지가 없으면 자동으로 다운로드

사용자가 신경 쓰지 않아도 도커나 런타임이 대신 처리해주는 것이죠.

### 💡 요약
**"컨테이너 생성을 추상화하고 자동화한다"**
는 말은
사용자가 복잡한 컨테이너 생성 과정을 일일이 다루지 않고,
간단한 명령어 또는 API 호출만으로 쉽게 컨테이너를 만들고 실행할 수 있게 해준다는 뜻이에요.