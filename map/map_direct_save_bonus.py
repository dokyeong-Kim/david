import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from collections import deque

# 데이터 불러오기
area_struct = pd.read_csv('map/area_struct.csv')
area_category = pd.read_csv('map/area_category.csv')
area_map = pd.read_csv('map/area_map.csv')

# 전처리 및 병합
area_struct.columns = area_struct.columns.str.strip()
area_category.columns = area_category.columns.str.strip()
area_map.columns = area_map.columns.str.strip()

area_struct_named = area_struct.merge(area_category, on='category', how='left')
area_struct_named['struct_clean'] = area_struct_named['struct'].str.strip()
merged_all = area_struct_named.merge(area_map, on=['x', 'y'], how='left')
merged_all.columns = merged_all.columns.str.strip()

# 구조물 분류
apartment_building = merged_all[
    merged_all['struct_clean'].isin(['Apartment', 'Building'])
]
bandalgom = merged_all[merged_all['struct_clean'] == 'BandalgomCoffee']
my_home = merged_all[merged_all['struct_clean'] == 'MyHome']
construction_sites = merged_all[merged_all['ConstructionSite'] == 1]
walkable = merged_all[merged_all['ConstructionSite'] != 1]
walkable_set = set(zip(walkable['x'], walkable['y']))

# 구조물 노드 목록
structure_nodes = merged_all[
    (merged_all['struct_clean'].isin(['Apartment', 'Building', 'BandalgomCoffee', 'MyHome'])) &
    (merged_all['ConstructionSite'] != 1)
][['x', 'y', 'struct_clean']].drop_duplicates().reset_index(drop=True)

nodes = list(structure_nodes[['x', 'y']].itertuples(index=False, name=None))
start = tuple(my_home[['x', 'y']].iloc[0])

# BFS 거리 계산
def bfs_distance(start, end, walkable_set):
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    while queue:
        current, dist = queue.popleft()
        if current == end:
            return dist
        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (x + dx, y + dy)
            if neighbor in walkable_set and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return float('inf')

# BFS 경로 복원
def bfs_path(start, end, walkable_set):
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)
    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (x + dx, y + dy)
            if neighbor in walkable_set and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return []

# 거리 행렬 계산
distance_matrix = {
    (src, dst): bfs_distance(src, dst, walkable_set)
    for i, src in enumerate(nodes)
    for j, dst in enumerate(nodes)
    if i != j
}

# Nearest Neighbor 기반 TSP 경로
def tsp_nearest_neighbor(start, nodes, dist_matrix):
    unvisited = set(nodes)
    path = [start]
    unvisited.remove(start)
    current = start
    while unvisited:
        next_node = min(
            unvisited,
            key=lambda x: dist_matrix.get((current, x), float('inf'))
        )
        path.append(next_node)
        unvisited.remove(next_node)
        current = next_node
    return path

tsp_path = tsp_nearest_neighbor(start, set(nodes), distance_matrix)

# 실제 경로 재구성
tsp_full_path = []
for i in range(len(tsp_path) - 1):
    segment = bfs_path(tsp_path[i], tsp_path[i + 1], walkable_set)
    if i > 0:
        segment = segment[1:]  # 중복 제거
    tsp_full_path.extend(segment)

# 결과 CSV 저장
pd.DataFrame(tsp_full_path, columns=['x', 'y']).to_csv('map/tsp_path_bonus.csv', index=False)

#시각화
fig, ax = plt.subplots(figsize=(10, 10))

max_x, max_y = merged_all['x'].max(), merged_all['y'].max()
# 셀 경계를 정확히 맞추기 위한 설정
ax.set_xlim(0, max_x + 1)
ax.set_ylim(0, max_y + 1)

# 격자 라벨 설정
ax.set_xticks(range(0, max_x + 2))
ax.set_yticks(range(0, max_y + 2))

# y축 위에서 아래로 증가
ax.invert_yaxis()

# 셀 정사각형 유지
ax.set_aspect('equal')
ax.grid(True, which='both')


# 구조물 시각화
for _, row in structure_nodes.iterrows():
    x, y = row['x'], row['y']
    struct = row['struct_clean']
    if struct == 'MyHome':
        triangle = plt.Polygon(
            [[x, y - 0.3], [x - 0.3, y + 0.3], [x + 0.3, y + 0.3]],
            color='green'
        )
        ax.add_patch(triangle)
    elif struct == 'BandalgomCoffee':
        ax.add_patch(plt.Rectangle((x - 0.3, y - 0.3), 0.6, 0.6, color='green'))
    else:
        ax.add_patch(plt.Circle((x, y), 0.3, color='saddlebrown'))

# 건설 현장 시각화
for _, row in construction_sites.iterrows():
    ax.add_patch(plt.Rectangle((row['x'] - 0.4, row['y'] - 0.4), 0.8, 0.8, color='gray'))

# 경로 선
x_coords, y_coords = zip(*tsp_full_path)
ax.plot(x_coords, y_coords, color='red', linewidth=2)

# 시작점과 끝점 좌표
start_x, start_y = start
end_x, end_y = bandalgom[['x', 'y']].iloc[0]

# 구조물 위에 텍스트 표시
ax.text(start_x, start_y - 0.6, 'Start', color='black',
        fontsize=10, ha='center', fontweight='bold')

ax.text(end_x, end_y - 0.6, 'End', color='black',
        fontsize=10, ha='center', fontweight='bold')

# 범례 추가
legend_elements = [
    mpatches.Patch(color='gray', label='Construction Site'),
    Line2D([0], [0], marker='o', color='w', label='Apartment/Building',
           markerfacecolor='saddlebrown', markersize=10),
    mpatches.Patch(color='green', label='BandalgomCoffee (Square)'),
    Line2D([0], [0], marker='^', color='w', label='MyHome (Triangle)',
           markerfacecolor='green', markersize=10),
]

ax.legend(handles=legend_elements, loc='lower right')

# 타이틀 및 저장
ax.set_title('TSP Path (No Diagonal) Visiting All Structures')
plt.savefig('map/map_tsp_bonus.png')

