def main():
    # 사용자에게 숫자 여러 개를 입력받기 (입력은 문자열 형태로 들어옴)
    try:
        nums = input("Enter numbers: ")  # 예: "3 5 1 9"

        # 입력된 문자열을 공백 기준으로 나누고(split), 각 요소를 실수(float)로 변환해서 리스트로 저장
        # 예: ["3", "5", "1"] → [3.0, 5.0, 1.0]
        num_list = [float(n) for n in nums.split()]

        # 리스트의 첫 번째 값을 초기값으로 설정
        min_val = num_list[0]
        max_val = num_list[0]

        # 리스트를 순회하면서 최소값과 최대값을 직접 구함
        for n in num_list:
            if n < min_val:
                min_val = n  # 더 작은 값이 있으면 최소값 갱신
            if n > max_val:
                max_val = n  # 더 큰 값이 있으면 최대값 갱신

        # 최종 결과 출력
        print("Min:", min_val, "Max:", max_val)

    except ValueError:
        # 숫자가 아닌 값이 입력됐을 경우 오류 메시지 출력
        print("Invalid number input.")
        return

# 직접 실행했을 때만 아래 main() 함수가 호출됨
if __name__ == "__main__":
    main()


