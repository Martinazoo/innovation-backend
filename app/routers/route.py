from fastapi import APIRouter, HTTPException

from services.tiled_map import TiledMap
from services.astar import AStar

route_router = APIRouter(prefix="/route", tags=["route"])

tiled_map = TiledMap("tiledmap.json")
astar = AStar(tiled_map.grid)


@route_router.get("/get_route")
def get_route(start: str, end: str):

    if start not in tiled_map.points:
        raise HTTPException(400, f"Unknown start point: {start}")

    if end not in tiled_map.points:
        raise HTTPException(400, f"Unknown end point: {end}")

    start_tile = tiled_map.get_point(start)
    end_tile = tiled_map.get_point(end)

    path_tiles = astar.find_path(start_tile, end_tile)

    if not path_tiles:
        raise HTTPException(404, "No path found")

    path_pixels = [
        tiled_map.tile_to_pixel(tile)
        for tile in path_tiles
    ]

    return {
        "start": start,
        "end": end,
        "tiles": path_tiles,
        "pixels": path_pixels
    }