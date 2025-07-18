# priority_calculator.py 보너스 과제

# 사칙연산을 수행하는 기본 함수 정의
# 덧셈
def add(a, b):
    return a + b

# 뺄셈
def subtract(a, b):
    return a - b

# 곱셈
def multiply(a, b):
    return a * b

# 나눗셈 - 0으로 나누는 경우 예외 발생
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero.")
    return a / b

# 수식을 계산하는 함수
# 연산자 우선순위와 괄호를 고려한 계산 수행
# 토큰: 공백으로 나눈 문자열 리스트
# 예: ['(', '4', '+', '5', ')', '*', '2']
def evaluate_expression(tokens):
    # 연산을 수행하는 헬퍼 함수 정의
    # operators: 연산자 스택
    # values: 숫자 스택
    def apply_operator(operators, values):
        # 연산자 스택에서 마지막 연산자를 꺼냄
        op = operators.pop()

        # 숫자 스택에서 마지막 두 숫자를 꺼냄 (b는 마지막, a는 그 이전)
        b = values.pop()
        a = values.pop()

        # 꺼낸 연산자에 따라 알맞은 연산 수행 후 결과를 다시 숫자 스택에 저장
        if op == '+':
            values.append(add(a, b))
        elif op == '-':
            values.append(subtract(a, b))
        elif op == '*':
            values.append(multiply(a, b))
        elif op == '/':
            values.append(divide(a, b))  # divide는 0 나눗셈 처리 포함

    # 연산자의 우선순위 정의
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    values = []     # 숫자 스택
    operators = []  # 연산자 스택

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token == '(':  # 여는 괄호는 무조건 스택에 넣음
            operators.append(token)

        elif token == ')':  # 닫는 괄호가 나오면, 여는 괄호를 만날 때까지 계산
            while operators and operators[-1] != '(':  # 여는 괄호가 나올 때까지 반복
                apply_operator(operators, values)
            operators.pop()  # 여는 괄호 제거

        elif token in precedence:  # 연산자인 경우
            # 현재 연산자보다 우선순위가 높은 연산자가 스택에 있으면 계산
            while (operators and operators[-1] in precedence and
                   precedence[operators[-1]] >= precedence[token]):
                apply_operator(operators, values)
            # 현재 연산자를 연산자 스택에 추가
            operators.append(token)

        else:
            # 숫자인 경우 float으로 변환하여 스택에 저장
            try:
                values.append(float(token))
            except ValueError:
                raise ValueError("Invalid input.")

        i += 1

    # 남은 연산자들 계산
    while operators:
        apply_operator(operators, values)

    # 최종 결과 반환
    return values[0]

# 프로그램 실행 메인 함수 정의
def main():
    try:
        expr = input("Enter expression: ")  # 사용자 입력 받기

        # 공백 없는 입력은 잘못된 형식으로 간주
        if ' ' not in expr:
            print("Invalid input. Please separate numbers and operators with spaces.")
            return

        tokens = expr.split()  # 공백 기준으로 나눠 토큰 리스트 생성
        result = evaluate_expression(tokens)  # 수식 계산 실행
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Division by zero.")  # 0으로 나눈 경우
    except Exception:
        print("Invalid input.")  # 숫자/연산자 외의 잘못된 입력

# 이 파일이 직접 실행될 때만 main() 함수 실행
if __name__ == "__main__":
    main()
