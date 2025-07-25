import pandas as pd
import os

## 1단계 : .csv 파일을 불러와 내용을 출력하고 분석
# 파일 경로 설정
BASE_PATH = "/Users/dk/Documents/AI-codyssey/map"
category_path = os.path.join(BASE_PATH, "area_category.csv")
map_path = os.path.join(BASE_PATH, "area_map.csv")
struct_path = os.path.join(BASE_PATH, "area_struct.csv")

# CSV 파일 읽기
df_category = pd.read_csv(category_path)
df_map = pd.read_csv(map_path)
df_struct = pd.read_csv(struct_path)

# 내용 전체 출력
print("===== area_category.csv =====")
print(df_category.to_string(index=False), "\n")

print("===== area_map.csv =====")
print(df_map.to_string(index=False), "\n")

print("===== area_struct.csv =====")
print(df_struct.to_string(index=False), "\n")

# 간단 분석
print(">>> area_category.csv 정보:")
print(df_category.info(), "\n")

print(">>> area_map.csv 정보:")
print(df_map.info(), "\n")

print(">>> area_struct.csv 정보:")
print(df_struct.info(), "\n")

## 2단계 : 구조물 ID를 이름으로 변환
# 공백 제거
df_struct.columns = df_struct.columns.str.strip()
df_category.columns = df_category.columns.str.strip()

# category → struct 매핑 딕셔너리 생성
cat_map = dict(zip(df_category['category'], df_category['struct']))

# struct 컬럼 생성 (0은 NaN 처리), 기존 category 컬럼은 삭제
df_struct['struct'] = df_struct['category'].apply(lambda x: cat_map.get(x) if x != 0 else float('nan'))
df_struct = df_struct.drop(columns=['category'])

# 컬럼 순서 재배치: x, y, struct, area
df_struct = df_struct[['x', 'y', 'struct', 'area']]

# 결과 출력
print("===== 구조물 이름 변환된 area_struct (NaN은 구조물 없음) =====")
print(df_struct.to_string(index=False), "\n")

# 3단계 : area_map.csv 병합
df_merged = df_struct.merge(df_map, on=['x', 'y'], how='left')

# area 기준 정렬
df_merged = df_merged.sort_values(by='area')

# 컬럼 순서 재정렬
df_merged = df_merged[['area', 'x', 'y', 'struct', 'ConstructionSite']]

# 결과 출력
print("===== 세 데이터 병합 후 area 기준 정렬 =====")
print(df_merged.to_string(index=False), "\n")

## 4단계 : area == 1만 필터링
df_area1 = df_merged[df_merged['area'] == 1]

# 결과 출력
print("===== area == 1 필터링 결과 =====")
print(df_area1.to_string(index=False), "\n")

## (보너스) 구조물 종류별 요약 통계를 리포트로 출력
# NaN은 'None'으로 바꿔서 집계
df_stat = df_merged.copy()
df_stat['struct'] = df_stat['struct'].fillna('None')

# 전체 구조물 종류별 개수
struct_summary = df_stat['struct'].value_counts().reset_index()
struct_summary.columns = ['Structure Type', 'Count']

print("===== 📊 전체 구조물 종류별 개수 =====")
print(struct_summary.to_string(index=False), "\n")

# area별 구조물 종류 분포
area_struct_count = df_stat.groupby(['struct', 'area']).size().reset_index(name='Count')
area_struct_pivot = area_struct_count.pivot(index='struct', columns='area', values='Count').fillna(0).astype(int)

print("===== 📊 구조물 종류별 Area 분포 (Pivot Table) =====")
print(area_struct_pivot, "\n")
