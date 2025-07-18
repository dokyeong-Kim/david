# Git 기초 정리

## 1. 버전 관리 시스템 종료 3기지
버전 관리 시스템 (VCS: Version Control System)은 소스코드 변경 이력을 추적하고,
여러 사람이 협업할 수 있게 도와주는 도구다. 주요 방식은 아래와 같다:

### 1-1. 로컬 버전 관리 시스템 (Local VCS)
- 개념: 변경 이력을 로컬 컴퓨터에만 저장
- 장점: 빠르고 간단함
- 단점: 협업에 부적합하고, 백업이 어려움
- 예시: RCS, SCCS

### 1-2 중앙 집중식 버전 관리 시스템 (Centralized VCS)
- 개념: 중앙 서버에 모든 변경 이력을 저장하고, 사용자는 서버에서 받아서 사용
- 장점: 관리가 쉬움, 단일한 이력
- 단점: 서버 장애 시 작업 중단, 분산 작업 어려움
- 예시: Subversion (SVN), CVS

### 1-3. 분산 버전 관리 시스템 (Distributed VCS)
- 개념: 모든 사용자가 전체 변경 이력을 로컬에 복사해서 가짐
- 장점: 오프라인 작업 가능, 빠른 속도, 백업 용이
- 단점: 초기 진입 장벽이 다소 있음
- 예: Git, Mercurial

## 2. .git 디렉토리의 의미와 역할
.git 디렉토리는 Git 저장소의 핵심 데이터가 저장되는 숨김 풀더다.
Git 명령을 통해 실행되는 모든 작업은 .git 폴터 내부 데이터를 바탕으로 동작한다.

### 주요 역할:
- 버전 이력 관리: 커밋, 브랜치, 병합, 로그 등의 정보 저장
- 저장소 설정: Git 환경설정, 원격 저장소 주소, 후킹 스크립트 등 포함
- 객체 저장소: 실제 소스 코드 상태를 저장하는 objects, refs 등 포함

### 요약:
.git 폴더가 존재하면, 해당 폴더는 Git 저장소로 인식된다.
삭제되면 Git으로 관리되지 않으며, 이력도 모두 사라진다.

## 3. 작업 디렉토리에서 .git 디렉토리 삭제하고 상태 확인 후, 다시 복원해보기 (로그)
.venvdk@DKui-MacBookAir david % cp -r .git ../git_backup
.venvdk@DKui-MacBookAir david % rm -rf .git
.venvdk@DKui-MacBookAir david % git status
fatal: not a git repository (or any of the parent directories): .git
.venvdk@DKui-MacBookAir david % cp -r ../git_backup .git 
.venvdk@DKui-MacBookAir david % git status 
On branch main

No commits yet
