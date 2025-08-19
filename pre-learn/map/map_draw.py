
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

# 데이터 불러오기
area_struct = pd.read_csv("map/area_struct.csv")
area_category = pd.read_csv("map/area_category.csv")
area_map = pd.read_csv("map/area_map.csv")

# 컬럼 정리 및 병합
area_struct.columns = area_struct.columns.str.strip()
area_category.columns = area_category.columns.str.strip()
area_map.columns = area_map.columns.str.strip()

area_struct_named = area_struct.merge(area_category, on="category", how="left")
area_struct_named["struct_clean"] = area_struct_named["struct"].str.strip()
merged_all = area_struct_named.merge(area_map, on=["x", "y"], how="left")
merged_all.columns = merged_all.columns.str.strip()

# 구조물 분류
apartment_building = merged_all[merged_all["struct_clean"].isin(["Apartment", "Building"])]
bandalgom = merged_all[merged_all["struct_clean"] == "BandalgomCoffee"]
my_home = merged_all[merged_all["struct_clean"] == "MyHome"]
construction_sites = merged_all[merged_all["ConstructionSite"] == 1]

# 시각화 시작
fig, ax = plt.subplots(figsize=(10, 10))

max_x, max_y = merged_all["x"].max(), merged_all["y"].max()
ax.set_xticks(range(1, max_x + 2))
ax.set_yticks(range(1, max_y + 2))
ax.grid(True, which='both')
ax.invert_yaxis()

# 건설 현장: 회색 사각형
for _, row in construction_sites.iterrows():
    x, y = row["x"], row["y"]
    ax.add_patch(plt.Rectangle((x - 0.4, y - 0.4), 0.8, 0.8, color='gray'))

# 아파트/빌딩: 갈색 원형
for _, row in apartment_building.iterrows():
    x, y = row["x"], row["y"]
    if not ((construction_sites["x"] == x) & (construction_sites["y"] == y)).any():
        ax.add_patch(plt.Circle((x, y), 0.3, color='saddlebrown'))

# 반달곰 커피점: 녹색 사각형
for _, row in bandalgom.iterrows():
    x, y = row["x"], row["y"]
    if not ((construction_sites["x"] == x) & (construction_sites["y"] == y)).any():
        ax.add_patch(plt.Rectangle((x - 0.3, y - 0.3), 0.6, 0.6, color='green'))

# 내 집: 녹색 삼각형
for _, row in my_home.iterrows():
    x, y = row["x"], row["y"]
    if not ((construction_sites["x"] == x) & (construction_sites["y"] == y)).any():
        triangle = plt.Polygon([[x, y - 0.3], [x - 0.3, y + 0.3], [x + 0.3, y + 0.3]], color='green')
        ax.add_patch(triangle)

# 범례 추가
legend_elements = [
    mpatches.Patch(color='gray', label='Construction Site'),
    Line2D([0], [0], marker='o', color='w', label='Apartment/Building',
           markerfacecolor='saddlebrown', markersize=10),
    mpatches.Patch(color='green', label='BandalgomCoffee (Square)'),
    Line2D([0], [0], marker='^', color='w', label='MyHome (Triangle)',
           markerfacecolor='green', markersize=10),
]

ax.legend(handles=legend_elements, loc='upper right')
ax.set_title("Full Map: All Structures with Legend Symbols")
ax.set_xlabel("X Coordinate")
ax.set_ylabel("Y Coordinate")

# 이미지로 저장
plt.savefig("map/map.png")
