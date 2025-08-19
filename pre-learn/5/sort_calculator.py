def main():
    # 사용자로부터 숫자들을 입력받음 (공백으로 구분)
    try:
        nums = input("Enter numbers: ")
        # 입력받은 문자열을 공백 기준으로 나누어 리스트로 변환
        # 각 요소를 float(실수)로 변환해 리스트 생성
        num_list = [float(n) for n in nums.split()]


        # 선택 정렬 알고리즘으로 오름차순 정렬
            # 가장 작은 걸 "선택해서 자리 잡기"	
            # 맨 앞부터 정해가며 작은 값 찾아 교체
        n = len(num_list)

        # 아무것도 입력안했을 때 예외처리
        if n==0:
            print("Invalid input.")
            return

        for i in range(n):
            min_idx = i # 현재 위치를 최소값 인덱스로 가정
            for j in range(i + 1, n): # 현재 위치 i 다음부터 리스트 끝까지 탐색
                if num_list[j] < num_list[min_idx]:
                    min_idx = j # 더 작은 값이 있으면 인덱스 갱신
            # 가장 작은 값과 현재 위치의 값을 교환
            num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]

        
        # 버블 정렬 알고리즘으로 오름차순 정렬
            # 큰 걸 계속 "뒤로 밀어내기"
            # 끝에서부터 큰 값을 버블처럼 띄움
        # n = len(num_list)
        # for i in range(n):
            # for j in range(0, n - i - 1): # 아직 정렬되지 않은 범위만
                #if num_list[j] > num_list[j + 1]:
                    # 두 값을 교환
                    # num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
        
        # 정렬된 리스트 출력
        print("Sorted:", num_list)
        
    except ValueError:
        # 숫자가 아닌 값이 입력된 경우 예외 처리
        print("Invalid number input.")
        return

if __name__ == "__main__":
    main()
