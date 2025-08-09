# 🐳 Windows에서의 Docker 컨테이너: 리눅스 vs 윈도우

Docker Desktop은 Windows 환경에서도 컨테이너를 사용할 수 있도록 지원합니다. 이때 사용 가능한 컨테이너는 크게 두 종류입니다:

- **Linux 컨테이너**
- **Windows 컨테이너**

이 둘의 차이점을 아래 표와 함께 비교합니다.

---

## ✅ 주요 차이점

| 항목 | 리눅스 컨테이너 | 윈도우 컨테이너 |
|------|------------------|------------------|
| **운영체제 커널** | Linux 커널 기반 | Windows NT 커널 기반 |
| **지원 플랫폼** | Windows, macOS, Linux | Windows 전용 |
| **호환성** | 대부분의 오픈소스 앱, 개발툴, 서버 | Windows 전용 앱 (.NET Framework 등) |
| **Docker 이미지** | Ubuntu, Alpine, Python 등 다양 | Windows Server Core, Nano Server 등 |
| **성능** | 경량, 빠른 실행 속도 | 상대적으로 무거움 |
| **기본 실행 모드** | Docker Desktop 기본값 (WSL2 기반) | 설정 변경 필요 |
| **실행 환경** | WSL2 또는 Hyper-V로 가상 리눅스 실행 | Windows OS에서 직접 실행 |
| **용도 예시** | Flask, Node.js, nginx 등 리눅스 기반 앱 개발 | 기존 .NET Framework 앱, IIS 웹서버 등 |

---

## 🔄 전환 방법 (Docker Desktop)

- 리눅스 컨테이너 사용 중:
  - 오른쪽 클릭 → "Switch to Windows containers"
- 윈도우 컨테이너 사용 중:
  - 오른쪽 클릭 → "Switch to Linux containers"

※ 전환 시 Docker 데몬이 재시작됨

---

## 💡 어떤 걸 써야 할까?

| 상황 | 추천 컨테이너 |
|------|----------------|
| 대부분의 웹 개발, Python/Node 앱 | ✅ 리눅스 컨테이너 |
| Windows 전용 앱 (예: .NET Framework, WPF 등) | ✅ 윈도우 컨테이너 |

---

## 📌 참고

- Docker Desktop은 기본적으로 **리눅스 컨테이너 모드**로 실행됩니다.
- 윈도우 컨테이너는 일부 Windows OS에서만 사용 가능합니다 (예: Windows 10/11 Pro, Enterprise).

