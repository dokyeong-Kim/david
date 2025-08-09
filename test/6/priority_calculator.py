# priority_calculator.py

# 기본 연산 함수들 정의
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero.")
    return a / b

def main():
    try:
        # 사용자에게 수식 입력 받음 (예: "4 + 5 * 3 - 2")
        expr = input("Enter expression: ")

        # 괄호가 포함된 경우 예외 처리
        if '(' in expr or ')' in expr:
            print("Invalid input.")
            return

        # 공백 없이 입력한 경우 예외 처리
        if ' ' not in expr:
            print("Invalid input.")
            return

        # 공백 기준으로 나눠 리스트로 만듬
        parts = expr.split()

        # 예외처리_잘못된 형식 확인: 연산자와 숫자가 번갈아 와야 하므로 길이 값은 홀수여야 함
        if len(parts) % 2 == 0:
            print("Invalid input.")
            return

        # 숫자들과 연산자들을 나눠 저장
        numbers = []    # 숫자들 저장
        operators = []  # 연산자 저장

        # 길이 값만큼 반복
        for i in range(len(parts)):
            # 짝수 위치에는 숫자가 있어야 함
            if i % 2 == 0:
                try:
                    #사용자 입력에서 숫자 위치의 문자열을 실수로 변환하여 numbers 리스트에 담음
                    numbers.append(float(parts[i])) 
                # 예외처리
                except ValueError:
                    print("Invalid input.")
                    return
            # 홀수 위치에는 연산자(+,-,*,/)가 있어야 함
            else:
                # 예외처리
                if parts[i] not in ('+', '-', '*', '/'):
                    print("Invalid input.")
                    return
                # 예외가 아닌 경우는 operators 리스트에 담음
                operators.append(parts[i])

        # 1단계: 우선순위 높은 *와 / 먼저 계산
        i = 0
        while i < len(operators):
            op = operators[i] # 변수 지정
            if op == '*':
                result = multiply(numbers[i], numbers[i + 1]) # 곱하기 실행
                numbers[i:i+2] = [result]  # 결과로 두 숫자 자리를 대체
                operators.pop(i)           # 해당 연산자는 제거, pop(index)은 지정한 인덱스의 값을 꺼내고 삭제 / 지정X시, 리스트 마지막 값 
            elif op == '/':
                try:
                    result = divide(numbers[i], numbers[i + 1]) # 나누기 실행
                # 예외처리
                except ZeroDivisionError:
                    print("Error: Division by zero.")
                    return
                numbers[i:i+2] = [result]
                operators.pop(i)
            else:
                i += 1  # +나 -면 다음 연산자로 이동
                        # 연산하고 나면 i가 삭제되기 때문에 증가 안 함, 증가한다? +나 -이다.

        # 2단계: +와 - 계산
        i = 0
        while i < len(operators):
            op = operators[i]
            if op == '+':
                result = add(numbers[i], numbers[i + 1])
            elif op == '-':
                result = subtract(numbers[i], numbers[i + 1])
            numbers[i:i+2] = [result]
            operators.pop(i)

        # 결과 출력
        print("Result:", numbers[0])

    # 예외처리
    except Exception:
        print("Invalid input.")

# 실행
if __name__ == "__main__":
    main()
