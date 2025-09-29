import os
import json

def main():
    base_dir = os.path.dirname(__file__)  
    log_file = os.path.join(base_dir, "mission_computer_main.log")
    json_file = os.path.join(base_dir, "mission_computer_main.json")

    try:
        # 1. 로그 파일 읽기
        with open(log_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # 2. 로그 내용 출력
        print("=== 로그 파일 내용 ===")
        for line in lines:
            print(line.strip())

        # 3. 콤마(,) 기준 분리 → 리스트 변환
        log_list = []
        for line in lines:
            parts = line.strip().split(",", 1)
            if len(parts) == 2:
                datetime, message = parts
                log_list.append([datetime.strip(), message.strip()])

        # 4. 리스트 출력
        print("\n=== 리스트 객체 출력 ===")
        print(log_list)

        # 5. 시간 역순 정렬
        sorted_list = sorted(log_list, key=lambda x: x[0], reverse=True)
        print("\n=== 시간 역순 정렬 결과 ===")
        print(sorted_list)

        # 6. Dict 변환
        log_dict = {dt: msg for dt, msg in sorted_list}
        print("\n=== Dict 변환 결과 ===")
        print(log_dict)

        # 7. JSON 저장
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(log_dict, f, ensure_ascii=False, indent=4)
        print(f"\n=== JSON 저장 완료 ===\n{json_file}")

        # 8. 사고 원인 추론
        print("\n=== 사고 원인 추론 ===")
        cause_keywords = ["explosion", "unstable", "failure", "shutdown", "powered down", "emergency", "anomaly"]

        causes = []
        for dt, msg in sorted_list:  # 최신 → 오래된 순으로 검사
            lower_msg = msg.lower()
            if any(keyword in lower_msg for keyword in cause_keywords):
                causes.append(f"[{dt}] {msg}")

        if causes:
            print("추론된 사고 원인 로그:")
            for c in causes:
                print("-", c)
        else:
            print("사고 원인을 나타내는 특이 로그가 없습니다.")

        # 9. Markdown 보고서 저장
        report_file = os.path.join(base_dir, "log_analysis.md")

        with open(report_file, "w", encoding="utf-8") as f:
            f.write("# 🚀 미션 컴퓨터 사고 분석 보고서\n\n")

            f.write("## 1. 개요\n")
            f.write("- **시스템**: 미션 컴퓨터 (Mission Computer)\n")
            f.write(f"- **로그 파일**: {log_file}\n")
            f.write("- **분석 목적**: 로그 데이터를 기반으로 사고 발생 원인을 규명하고 재발 방지 대책을 마련한다.\n\n")

            f.write("## 2. 사고 관련 로그\n")
            if causes:
                f.write("아래 로그들이 사고와 관련된 것으로 분석됨:\n\n")
                for c in causes:
                    f.write(f"- {c}\n")
            else:
                f.write("사고와 관련된 특이 로그가 발견되지 않았습니다.\n")

            f.write("\n## 3. 결론 및 대책\n")
            if causes:
                f.write("- **추론된 원인**: 위 로그에서 확인된 사건(예: 폭발, 불안정, 전원 차단 등)\n")
                f.write("- **재발 방지 대책**:\n")
                f.write("  1. 문제 원인이 된 장비/시스템 정밀 점검\n")
                f.write("  2. 이상 징후 발생 시 조기 알람 시스템 강화\n")
                f.write("  3. 주요 시스템 이중화 및 안전 설계 보강\n")
            else:
                f.write("- 사고 원인이 발견되지 않았으므로 추가 점검 필요\n")

        print(f"\n=== Markdown 보고서 저장 완료 ===\n{report_file}")

    except FileNotFoundError:
        print(f"[에러] 로그 파일이 존재하지 않습니다: {log_file}")
    except UnicodeDecodeError:
        print("[에러] 파일을 UTF-8로 읽는 데 실패했습니다. (디코딩 오류)")
    except Exception as e:
        print(f"[예외 발생] {e}")

if __name__ == "__main__":
    main()
