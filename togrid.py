import json

def build_grid(map_json):
    width = map_json["width"]
    height = map_json["height"]
    data = map_json["layers"][0]["data"]

    grid = []
    for y in range(height):
        row = data[y * width:(y + 1) * width]
        grid.append(row)

    return grid


def save_grid_to_file(grid, filename="grid.json"):
    with open(filename, "w") as f:
        json.dump(grid, f)

def extract_points(map_json, tile_size):
    points = {}

    for layer in map_json["layers"]:
        if layer["type"] == "objectgroup":
            for obj in layer["objects"]:
                name = obj["name"]

                x = int(obj["x"] // tile_size)
                y = int(obj["y"] // tile_size)

                points[name] = (y, x)

    return points

def save_points_to_file(points, filename="points.json"):
    with open(filename, "w") as f:
        json.dump(points, f)

with open("simpletiledmap.json") as f:
    map_json = json.load(f)

grid = build_grid(map_json)
save_grid_to_file(grid)
points = extract_points(map_json, 16)
save_points_to_file(points)