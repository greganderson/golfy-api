import uuid

from fastapi import FastAPI

from models.course import Course
from models.player import Player, PlayerRequest, PlayerResponse


app = FastAPI()

players: dict[uuid.UUID, Player] = {}
courses: dict[uuid.UUID, Course] = {}

@app.get("/players")
async def get_players() -> list[Player]:
    return players.values()

@app.post("/players")
async def create_player(player: PlayerRequest) -> PlayerResponse:
    player_id = uuid.uuid4()
    players[player_id] = Player(id=player_id, name=player.name, handicap=player.handicap)
    return PlayerResponse(id=player_id)

@app.put("/players/{player_id}")
async def update_player(player_id: uuid.UUID, updated_player: PlayerRequest) -> PlayerResponse:
    players[player_id] = Player(id=player_id, name=updated_player.name, handicap=updated_player.handicap)
    return PlayerResponse(id=player_id)

@app.delete("/players/{player_id}")
async def delete_player(player_id: uuid.UUID) -> None:
    players.pop(player_id)

#@app.get("/courses")
#@app.post("/courses")
#@app.put("/courses/{course_id}")
#@app.delete("/courses/{course_id}")