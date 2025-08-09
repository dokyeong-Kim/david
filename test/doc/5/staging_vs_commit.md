# Git: 스테이징 영역 추가와 커밋의 차이

## 1. 기본 개념

Git은 변경 내용을 저장하기 위해 두 단계를 거칩니다:

1. **스테이지 영역에 추가 (git add)**
2. **커밋 (git commin)**

---

## 2. 스테이징 영역에 추가 ('git add')

- **역할**: 변경된 파일을 Git이 추적할 수 있도록 **임시 저장**하는 단계
- **목적**: 어떤 파일을 커밋할지 **선택**할 수 있음 
- **예시**: 

'''bash

git add index.html #파일 추가
git add style.css #또 다른 파일 추가

git commit -m "Add login feature" # 두 파일 커밋
```

# Git: push, reset, log 명령어 개념 정리

## 3. 'git push' - 원격 저장소로 전송

- **역할**: 로컬에서 커밋한 내용을 원격 저장소(GitHub)으로 **전송**
- **목적**: 다른 사람과 공유하거나 백업을 위해 원격 저장소에 업로드
- **예시**: 

'''bask
git push origin main

## 4. git log - 커밋 이력 보기

## 5. git reset - 커밋 또는 스테이징 취소

#### 5-1. --soft 
최근 커밋을 취소하고, 변경사항은 스테이징 상태 유지

git reset -- soft HEAD ~1

#### 5-2. --mixed (기본 옵션)
최근 커밋과 스테이징을 모두 취소, 작업 파일은 그대로

git reset -- mixed HEAD ~1

#### 5-3. --hard 
커밋도, 스테이징도, 작업 파일도 전부 되돌림 (되돌릴 수 없음 주의)

git reset -- hard HEAD ~1
