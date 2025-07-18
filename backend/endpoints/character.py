# Imports
from fastapi import APIRouter
import httpx
from models.character import Character

# Create router
router = APIRouter(
    prefix="/characters",
)


@router.get("/", response_model=list[Character], summary="Get all characters")
async def get_characters():
    endpoint_url = "https://api.hakush.in/hsr/data/character.json"
    async with httpx.AsyncClient() as client:
        response = await client.get(endpoint_url)
        response.raise_for_status()
        data = response.json()
        characters = [
            Character(id=int(char_id), **item) for char_id, item in data.items()
        ]
        return characters
