from fastapi import APIRouter, HTTPException, Depends
import json
from services.astar import AStar
from database import get_db
from uuid import UUID
from sqlalchemy.orm import Session
from security import get_current_user
from models.user import UserDB
from schemas.route import RouteRequest


route_router = APIRouter(prefix="/route", tags=["route"])

with open("grid.json") as f:
    grid = json.load(f)

with open("points.json") as f:
    points = json.load(f)

astar = AStar(grid)

def path_to_points_string(path):
    return " ".join([f"{x},{y}" for x, y in path])
"""
@route_router.get("/path")
def get_path(start: str, end: str, db: Session = Depends(get_db), user_id: UUID = Depends(get_current_user)):
    if start not in points or start != "UserLoc":
        raise HTTPException(status_code=404, detail=f"Point '{start}' does not exist")

    if end not in points or end != "UserLoc":
        raise HTTPException(status_code=404, detail=f"Point '{end}' does not exist")

    start_pos = tuple(points[start])
    end_pos = tuple(points[end])

    path = astar.find_path(start_pos, end_pos)

    if not path:
        raise HTTPException(status_code=400, detail="No path available between the specified points")

    path_string = path_to_points_string(path)

    return {
        "start": start,
        "end": end,
        "path": path,
        "pathString": path_string  
    }
"""


@route_router.post("/path")
def get_path(route_request: RouteRequest, user_id: UUID = Depends(get_current_user), db: Session = Depends(get_db)):
    start = route_request.start
    end = route_request.end

    def resolve_position(point_name: str):
        if point_name == "UserLoc":
            db_user = db.query(UserDB).filter(UserDB.id == user_id).first()
            if not db_user:
                raise HTTPException(status_code=404, detail="User not found")
            return (int(db_user.posY), int(db_user.posX))
        
        if point_name not in points:
            raise HTTPException(status_code=404, detail=f"Point '{point_name}' does not exist")
        
        return tuple(points[point_name])

    start_pos = resolve_position(start)
    end_pos = resolve_position(end)

    path = astar.find_path(start_pos, end_pos)

    if not path:
        raise HTTPException(
            status_code=400,
            detail="No path available between the specified points"
        )

    path_string = path_to_points_string(path)

    return {
        "start": start,
        "end": end,
        "path": path,
        "pathString": path_string
    }