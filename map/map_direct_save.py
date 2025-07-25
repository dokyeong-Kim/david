
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from collections import deque

# 데이터 불러오기
area_struct = pd.read_csv("map/area_struct.csv")
area_category = pd.read_csv("map/area_category.csv")
area_map = pd.read_csv("map/area_map.csv")

area_struct.columns = area_struct.columns.str.strip()
area_category.columns = area_category.columns.str.strip()
area_map.columns = area_map.columns.str.strip()

area_struct_named = area_struct.merge(area_category, on="category", how="left")
area_struct_named["struct_clean"] = area_struct_named["struct"].str.strip()
merged_all = area_struct_named.merge(area_map, on=["x", "y"], how="left")
merged_all.columns = merged_all.columns.str.strip()

apartment_building = merged_all[merged_all["struct_clean"].isin(["Apartment", "Building"])]
bandalgom = merged_all[merged_all["struct_clean"] == "BandalgomCoffee"]
my_home = merged_all[merged_all["struct_clean"] == "MyHome"]
construction_sites = merged_all[merged_all["ConstructionSite"] == 1]

# BFS 구현
walkable = merged_all[merged_all["ConstructionSite"] != 1]
walkable_set = set(zip(walkable["x"], walkable["y"]))
start = tuple(my_home[["x", "y"]].iloc[0])
goals = list(bandalgom[["x", "y"]].itertuples(index=False, name=None))

def bfs_path(start, goals, walkable_set):
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)
    while queue:
        current, path = queue.popleft()
        if current in goals:
            return path
        x, y = current
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (x+dx, y+dy)
            if neighbor in walkable_set and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

shortest_path = bfs_path(start, goals, walkable_set)

# 경로 저장
if shortest_path:
    pd.DataFrame(shortest_path, columns=["x", "y"]).to_csv("map/home_to_cafe.csv", index=False)

# 시각화 및 저장
fig, ax = plt.subplots(figsize=(10, 10))
max_x, max_y = merged_all["x"].max(), merged_all["y"].max()
ax.set_xticks(range(1, max_x + 2))
ax.set_yticks(range(1, max_y + 2))
ax.grid(True, which='both')
ax.invert_yaxis()

for _, row in construction_sites.iterrows():
    ax.add_patch(plt.Rectangle((row["x"] - 0.4, row["y"] - 0.4), 0.8, 0.8, color='gray'))

for _, row in apartment_building.iterrows():
    if (row["x"], row["y"]) not in construction_sites.set_index(["x", "y"]).index:
        ax.add_patch(plt.Circle((row["x"], row["y"]), 0.3, color='saddlebrown'))

for _, row in bandalgom.iterrows():
    if (row["x"], row["y"]) not in construction_sites.set_index(["x", "y"]).index:
        ax.add_patch(plt.Rectangle((row["x"] - 0.3, row["y"] - 0.3), 0.6, 0.6, color='green'))

for _, row in my_home.iterrows():
    if (row["x"], row["y"]) not in construction_sites.set_index(["x", "y"]).index:
        triangle = plt.Polygon([[row["x"], row["y"] - 0.3], [row["x"] - 0.3, row["y"] + 0.3], [row["x"] + 0.3, row["y"] + 0.3]], color='green')
        ax.add_patch(triangle)

if shortest_path:
    x_coords, y_coords = zip(*shortest_path)
    ax.plot(x_coords, y_coords, color='red', linewidth=2, label='Shortest Path')

ax.set_title("Shortest Path Map: MyHome to BandalgomCoffee")
ax.legend()
plt.savefig("map/map_final.png")
