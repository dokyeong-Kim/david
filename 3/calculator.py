# 계산기(실수형) 프로그램 구현

def main():
    expression = input("Enter expression: ")

    # 연산자 입력 받기 및 분리
    op = None
    for candidate in ('+', '-', '*', '/'):
        if candidate in expression:
            op = candidate
            break

    if not op:
            print("Invalid operator input.")
            return
        
    parts = expression.split(op)
    if len(parts) != 2:
        print("Invalid expression format.")
        return   
        
    # 숫자 분리하기
    try:
        a = float (parts[0].strip())
        b = float (parts[1].strip())
    except ValueError:
        print("Invalid number input.")
        return
        
    # 예외 처리
    if b == 0 and op == '/':
        print("Error: Division by zero.")
        return
        
    
    # 계산식 함수
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        # //은 정수 나눗셈을 의미
        return a // b
    
    # 연산 수행
    if op == '+':
        print("Result", add(a, b))
    elif op == '-':
        print("Result", subtract(a, b))
    elif op == '*':
        print("Result", multiply(a, b))
    elif op == '/':
        print("Result", divide(a, b))

# 실행코드
if __name__ == "__main__":
    main()
    