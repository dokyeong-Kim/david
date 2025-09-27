import pandas as pd
import matplotlib.pyplot as plt


# 1. CSV 파일 읽기

# pandas 라이브러리를 사용해 CSV 파일을 읽는다.
# train_df, test_df라는 DataFrame 객체가 만들어진다.
# 제약사항에 따라 외부 라이브러리 사용은 원칙적으로 금지이지만, **데이터 분석(pandas)**은 예외로 허용된다.
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

# shape는 (행 개수, 열 개수)를 반환한다.
# 이를 통해 데이터가 정상적으로 불러와졌는지 1차 확인할 수 있다.
print('=== 1. 파일 읽기 ===')
print('train.csv shape:', train_df.shape)
print('test.csv shape:', test_df.shape)
print()

# 2-1. 두 파일 병합
# pd.concat()을 사용하면 DataFrame을 세로 방향으로 이어붙일 수 있다.
# ignore_index=True 옵션으로 행 번호를 새로 매긴다.
merged_df = pd.concat([train_df, test_df], ignore_index=True)

print('=== 2. 병합된 데이터 확인 ===')
print('merged_df shape:', merged_df.shape)
print(merged_df.head())
print()

# 2-2. 병합된 파일 저장
# 병합된 DataFrame을 새로운 CSV 파일로 저장한다.
# index=False를 지정해 불필요한 인덱스 열이 저장되지 않도록 한다.
merged_df.to_csv('merged.csv', index=False)
print('병합된 파일이 저장되었습니다 → merged.csv')
print()

# 3. 전체 데이터 수량 파악
# len(merged_df)는 행(row)의 총 개수를 의미한다.
# 즉, train과 test를 합쳤을 때 전체 데이터 수량을 파악할 수 있다.
print('=== 3. 전체 데이터 수량 ===')
print('전체 행 개수:', len(merged_df))
print()


# 4. Transported 항목과 가장 관련성 높은 변수 찾기
# (Transported가 bool이면 int로 변환)
# Transported는 원래 True/False 값인데, 상관계수를 계산하려면 숫자형이 필요하므로 int로 변환한다.
if train_df['Transported'].dtype == 'bool':
    train_df['Transported'] = train_df['Transported'].astype(int)

# 수치형 변수와의 상관계수 확인
# select_dtypes(include='number')를 사용하면 숫자형 변수만 선택할 수 있어, 경고 메시지 없이 안전하게 상관관계를 계산할 수 있다.
# corr()는 피어슨 상관계수를 계산한다.
# 이로써 Transported와 가장 관련이 높은 컬럼을 찾는다.
corr = train_df.select_dtypes(include='number').corr()['Transported'].sort_values(ascending=False)
print('=== 4. Train 데이터에서 Transported와의 상관관계 ===')
print(corr)
print()

# 5-1. 나이대별 Transported 여부 시각화
bins = [0, 19, 29, 39, 49, 59, 69, 79, 120]
labels = ['10대', '20대', '30대', '40대', '50대', '60대', '70대', '80+']
train_df['AgeGroup'] = pd.cut(train_df['Age'], bins=bins, labels=labels, right=True)

# 5-2.나이대별 Transported 비율 계산
age_grouped = train_df.groupby('AgeGroup')['Transported'].value_counts(normalize=True).unstack()

print('=== 5. 연령대별 Transported 비율 (Train 데이터 기준) ===')
print(age_grouped)
print()

# 5-3. 시각화
age_grouped.plot(kind='bar', stacked=True, figsize=(8, 5))

plt.title('연령대별 Transported 여부 (Train 데이터)')
plt.ylabel('비율')
plt.xlabel('연령대')
plt.legend(title='Transported', labels=['Not Transported', 'Transported'])
plt.show()