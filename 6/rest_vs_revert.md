# ✅ Git Reset vs Revert

## 🎯 개요

Git에서 작업을 되돌릴 때 사용하는 대표적인 명령어 두 가지는 `reset`과 `revert`입니다. 두 명령어는 모두 커밋을 되돌리는 기능을 하지만, 작동 방식과 목적에 차이가 있습니다.

---

## 📌 reset

- **작업 히스토리 자체를 되돌림**
- **되돌리는 대상**: 스테이징 영역, 커밋
- **종류**:
  - `--soft`: 커밋만 되돌리고 스테이징은 유지
  - `--mixed` (기본): 커밋과 스테이징 영역을 되돌림
  - `--hard`: 커밋, 스테이징, 작업 디렉토리까지 모두 되돌림

❗ 주의: 협업 중에는 **절대 사용 금지**. 히스토리를 지워버리기 때문에 공유 저장소와 충돌 가능성.

---

## 📌 revert

- **커밋을 되돌리는 새로운 커밋 생성**
- **기존 히스토리를 보존하면서 되돌림**
- 안전하고 협업에 적합

---

## 🧪 언제 어떤 걸 사용해야 할까?

| 상황 | 권장 명령어 | 이유 |
|------|-------------|------|
| `git add` 되돌리기 (스테이징 취소) | `git reset HEAD <파일명>` | 스테이징만 취소하고 워킹 디렉토리는 유지 |
| `git commit` 되돌리기 (최근 커밋 수정) | `git reset --soft HEAD^` | 커밋만 취소하고 수정 사항은 유지 |
| `git push` 후 되돌리기 (공유된 커밋 취소) | `git revert <커밋 해시>` | 히스토리 보존하며 안전하게 되돌림 |
| `작업 디렉토리까지 다 되돌리기` | `git reset --hard` | 위험하지만 완전 초기화가 필요할 때만 사용 |

---

## 📝 예시 명령어

```bash
# 스테이징 영역에서 제거
git reset HEAD app.py

# 마지막 커밋을 되돌리고 커밋 전 상태로
git reset --soft HEAD^

# 푸시된 커밋을 되돌리기 (되돌리는 커밋 생성)
git revert <커밋 해시>

---

## 예시, git 커밋 후 되돌리기
.venvdk@DKui-MacBookAir AI-codyssey % git add 3/app.py
.venvdk@DKui-MacBookAir AI-codyssey % git commit -m "edit port"
[main 576b121] edit port
 1 file changed, 1 insertion(+), 1 deletion(-)
.venvdk@DKui-MacBookAir AI-codyssey % git log    
commit 576b12134dc4c6f61d991a729b28ba7d5c29ecd7 (HEAD -> main)
Author: dokyeong-Kim <tpxm0505@gmail.com>
Date:   Thu Jul 17 11:50:48 2025 +0900

    edit port

commit 9e5cb5dc0e4515b93271de5a64181a286810e35a
Author: dokyeong-Kim <tpxm0505@gmail.com>
Date:   Thu Jul 17 11:48:22 2025 +0900

    Edit port

commit c892574daec3a06a9bdccf9097bb186ec97f7e43
Author: dokyeong-Kim <tpxm0505@gmail.com>
Date:   Thu Jul 17 11:28:47 2025 +0900

    Revert "Task_3"
    
    This reverts commit bd08243692830a537b0a54f397dd420958901eba.
.venvdk@DKui-MacBookAir AI-codyssey % git revert 576b12134dc4c6f61d991a729b28ba7d5c29ecd7
[main 58dfe25] Revert "edit port"
 1 file changed, 1 insertion(+), 1 deletion(-)