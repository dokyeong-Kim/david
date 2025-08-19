import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

map_path = os.path.join(BASE_DIR, "area_map.csv")
struct_path = os.path.join(BASE_DIR, "area_struct.csv")
category_path = os.path.join(BASE_DIR, "area_category.csv")

map_df = pd.read_csv(map_path)
struct_df = pd.read_csv(struct_path)
category_df = pd.read_csv(category_path)

struct_df = struct_df.merge(category_df, on="category", how="left")
merged_df = pd.merge(map_df, struct_df, on=["x", "y"], how="left")

# ✅ 컬럼 공백 제거
merged_df.columns = merged_df.columns.str.strip()

# area 정렬 후 area 1 필터링 → category 제거
merged_df_sorted = merged_df.sort_values(by="area")
area1_df = merged_df_sorted[merged_df_sorted["area"] == 1].drop(columns=["category"])

# ✅ NaN 명시적 처리 (원하면 문자열 'NaN'으로도 가능)
area1_df["struct"] = area1_df["struct"].fillna("NaN")

# ✅ struct 컬럼을 맨 앞으로 이동하고 정렬
cols = area1_df.columns.tolist()
cols.insert(0, cols.pop(cols.index("struct")))
area1_df = area1_df[cols].sort_values(by="struct")

# 저장
output_path = os.path.join(BASE_DIR, "area1_result.csv")
area1_df.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"✅ 결과가 area1_result.csv 파일로 저장되었습니다: {output_path}")

