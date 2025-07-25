import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from collections import deque
import os
# 데이터 불러오기
area_struct = pd.read_csv("area_struct.csv")
area_category = pd.read_csv("area_category.csv")
area_map = pd.read_csv("area_map.csv")

# 전처리 및 병합
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
walkable = merged_all[merged_all["ConstructionSite"] != 1]
walkable_set = set(zip(walkable["x"], walkable["y"]))

# 구조물 노드
structure_nodes = merged_all[
    (merged_all["struct_clean"].isin(["Apartment", "Building", "BandalgomCoffee", "MyHome"])) &
    (merged_all["ConstructionSite"] != 1)
][["x", "y", "struct_clean"]].drop_duplicates().reset_index(drop=True)

nodes = list(structure_nodes[["x", "y"]].itertuples(index=False, name=None))
start = tuple(my_home[["x", "y"]].iloc[0])
end = tuple(bandalgom[["x", "y"]].iloc[0])

# BFS 거리 계산
def bfs_distance(start, end, walkable_set):
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        current, dist = queue.popleft()
        if current == end:
            return dist
        x, y = current
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            neighbor = (x+dx, y+dy)
            if neighbor in walkable_set and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist+1))
    return float('inf')

# 경로 복원
def bfs_path(start, end, walkable_set):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        x, y = current
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            neighbor = (x+dx, y+dy)
            if neighbor in walkable_set and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return []

# 거리 행렬
distance_matrix = {
    (src, dst): bfs_distance(src, dst, walkable_set)
    for i, src in enumerate(nodes)
    for j, dst in enumerate(nodes) if i != j
}

# TSP Nearest Neighbor
def tsp_nearest_neighbor(start, nodes, dist_matrix):
    unvisited = set(nodes)
    path = [start]
    unvisited.remove(start)
    current = start
    while unvisited:
        next_node = min(unvisited, key=lambda x: dist_matrix.get((current, x), float("inf")))
        path.append(next_node)
        unvisited.remove(next_node)
        current = next_node
    return path

tsp_path = tsp_nearest_neighbor(start, set(nodes), distance_matrix)

# 실제 경로 조합
tsp_full_path = []
for i in range(len(tsp_path) - 1):
    segment = bfs_path(tsp_path[i], tsp_path[i+1], walkable_set)
    if i > 0:
        segment = segment[1:]
    tsp_full_path.extend(segment)

# CSV 저장
output_path = os.path.join(os.path.dirname(__file__), "home_to_cafe.csv")
pd.DataFrame(tsp_full_path, columns=["x", "y"]).to_csv(output_path, index=False)

# 시각화
fig, ax = plt.subplots(figsize=(10, 10))
max_x, max_y = merged_all["x"].max(), merged_all["y"].max()
ax.set_xticks(range(1, max_x + 2))
ax.set_yticks(range(1, max_y + 2))
ax.set_xlim(0.5, max_x + 0.5)
ax.set_ylim(0.5, max_y + 0.5)
ax.grid(True)
ax.invert_yaxis()

# 구조물 시각화
bandalgom_end_flag = False
for _, row in structure_nodes.iterrows():
    x, y, struct = row["x"], row["y"], row["struct_clean"]
    if struct == "MyHome":
        ax.add_patch(plt.Polygon([[x, y - 0.3], [x - 0.3, y + 0.3], [x + 0.3, y + 0.3]], color='green'))
        # 텍스트를 삼각형 위에 겹치지 않게 표시
        ax.text(x, y - 0.45, "Start", ha="center", va="center", fontsize=8, color="black")
    elif struct == "BandalgomCoffee":
        ax.add_patch(plt.Rectangle((x - 0.3, y - 0.3), 0.6, 0.6, color='green'))
        if not bandalgom_end_flag:
            ax.text(x, y - 0.45, "End", ha="center", va="center", fontsize=7, color="black")
            bandalgom_end_flag = True
    else:
        ax.add_patch(plt.Circle((x, y), 0.3, color='saddlebrown'))

# 공사장
for _, row in construction_sites.iterrows():
    ax.add_patch(plt.Rectangle((row["x"] - 0.4, row["y"] - 0.4), 0.8, 0.8, color='gray'))

# 경로
x_coords, y_coords = zip(*tsp_full_path)
ax.plot(x_coords, y_coords, color='red', linewidth=2)

# 범례
legend_elements = [
    mpatches.Patch(color='gray', label='Construction Site'),
    Line2D([0], [0], marker='o', color='w', label='Apartment/Building', markerfacecolor='saddlebrown', markersize=10),
    mpatches.Patch(color='green', label='BandalgomCoffee (Square)'),
    Line2D([0], [0], marker='^', color='w', label='MyHome (Triangle)', markerfacecolor='green', markersize=10)
]
ax.legend(handles=legend_elements, loc='lower right')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("map_final")
# 현재 파일과 같은 경로에 저장
output_img_path = os.path.join(os.path.dirname(__file__), "map_final.png")
plt.savefig(output_img_path)