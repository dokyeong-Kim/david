
# 제곱 계산 프로그램
# 사용자로부터 숫자와 지수를 입력받고, 반복문을 사용해 제곱 결과를 출력함

def main():
    try:
        # 숫자 입력 받기 (소수도 가능)
        # 입력값을 float 형식으로 변환 (예: "3.5" → 3.5)
        # float란 부동소수점 숫자를 나타내는 자료형
        base = float(input("Enter number: "))
    except ValueError:
        # 숫자가 아닌 값을 입력하면 오류 메시지 출력
        print("Invalid number input. ")
        # return은 단순히 "종료"가 아니라, "값을 돌려주고 함수 실행을 끝내는 것"
        return
    
    try:
        # 지수 입력 받기 (반드시 정수여야 함)
        exponent = int(input("Enter exponent: "))
        # 음수 지수는 허용하지 않으므로, 예외 처리
        if exponent < 0:
            raise ValueError
    except ValueError:
        # 지수가 정수가 아니거나 음수일 경우 오류 메시지 출력 후 종료
        print("Invalid exponent input.")
        return 
    
    # 반복문을 사용하여 제곱 계산
    # 제곱 결과를 담을 변수 초기화 (곱셈의 항등원: 1)
    # 항등원은 어떤 수와 곱해도 그 수가 그대로 나오는 값
    result = 1
    # exponent 횟수만큼 반복하여 base를 곱함
    for _ in range(exponent):
        # result = result * base
        result *= base
    # 최종 결과 출력
    print(f"Result: {result}")

# Python 프로그램의 시작점
# 직접 실행할 때만 main() 함수를 호출함
if __name__ == "__main__":
    main()

