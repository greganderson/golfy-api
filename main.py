import uuid

from fastapi import FastAPI

from models.course import Course
from models.player import Player


app = FastAPI()

players: dict[uuid.UUID, Player] = {}
courses: dict[uuid.UUID, Course] = {}

@app.get("/players")

#@app.post("/players")
#@app.put("/players/{player_id}")
#@app.delete("/players/{player_id}")
#
#@app.get("/courses")
#@app.post("/courses")
#@app.put("/courses/{course_id}")
#@app.delete("/courses/{course_id}")