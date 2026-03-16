import json
from pathlib import Path

TILE_SIZE = 16

BASE_DIR = Path(__file__).resolve().parents[2]

class TiledMap:
    def __init__(self, json_path: str):
        self.data = json.loads((BASE_DIR / "tiledmap.json").read_text())

        self.width = self.data["width"]
        self.height = self.data["height"]

        self.tile_layer = next(
            layer for layer in self.data["layers"] if layer["type"] == "tilelayer"
        )

        self.grid = self._build_grid()

        self.points = {
            "E1": (10, 20),
            "M320": (40, 50),
            "M321": (60, 70),
            "C1": (15, 35),
            "S1": (100, 120),
        }

    def _build_grid(self):
        data = self.tile_layer["data"]

        grid = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                tile = data[y * self.width + x]

                walkable = tile == 0
                row.append(walkable)

            grid.append(row)

        return grid

    def get_point(self, name: str):
        return self.points[name]

    def tile_to_pixel(self, tile):
        x, y = tile
        return (x * TILE_SIZE, y * TILE_SIZE)