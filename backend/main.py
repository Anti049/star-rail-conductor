# Imports
import os
from typing import AsyncGenerator
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi_utils.tasks import repeat_every
import hakushin
import yatta
from endpoints import version, character


# Handle periodic tasks
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Lifespan context manager for the FastAPI app.
    This can be used to handle startup and shutdown events.
    """
    # Perform startup tasks here if needed
    print("Starting FastAPI app...")
    # async with yatta.YattaAPI(lang=yatta.Language.EN) as client:
    #     version = await client.fetch_latest_version()
    #     characters = await client.fetch_characters()
    #     march7th = await client.fetch_character_detail(id=1001)
    #     stats = await client.fetch_manual_avatar()
    #     yatta_light_cones = await client.fetch_light_cones()
    #     relic_sets = await client.fetch_relic_sets()
    #     items = await client.fetch_items()
    #     print(f"Fetched {len(characters)} characters from Yatta API.")
    # async with hakushin.HakushinAPI(hakushin.Game.HSR, hakushin.Language.EN) as client:
    #     characters_hsr = await client.fetch_characters()
    #     march = await client.fetch_character_detail(character_id=1001)
    #     new = await client.fetch_new()
    #     light_cones = await client.fetch_light_cones()
    #     relics = await client.fetch_relic_sets()
    #     light_cone_detail = await client.fetch_light_cone_detail(light_cone_id=23000)
    yield
    # Perform shutdown tasks here if needed
    print("Shutting down FastAPI app...")


# Create FastAPI app
app = FastAPI(lifespan=lifespan)

# Add CORS middleware if needed
origins = ["http://localhost", "http://localhost:5656"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include endpoints
app.include_router(version.router)
app.include_router(character.router)


# Start application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=os.getenv("HOST", "localhost"),
        port=int(os.getenv("PORT", 5657)),
        log_level=os.getenv("LOG_LEVEL", "info"),
        reload=os.getenv("RELOAD", "false").lower() == "true",
    )
