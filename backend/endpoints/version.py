# Imports
import json
from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi import responses


class JSONResponse(responses.JSONResponse):
    def json(self):
        return json.loads(self.body.decode("utf-8"))


# Create router
router = APIRouter(
    prefix="/version",
    tags=["version"],
)


async def app_version():
    """
    Endpoint to get the latest version of Honkai: Star Rail.
    This endpoint fetches the latest game package information from the Hoyoverse API.
    """
    version_url = "https://sg-hyp-api.hoyoverse.com/hyp/hyp-connect/api/getGamePackages?launcher_id=VYTpXlbWo8"
    import httpx

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(version_url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json().get("data", {}).get("game_packages", [])
            if not data:
                return {
                    "error": "No game packages found",
                    "status_code": 404,
                }
            # Get game package with game.biz = "hkrpg_global"
            game_package = next(
                (pkg for pkg in data if pkg.get("game").get("biz") == "hkrpg_global"),
                None,
            )
            if not game_package:
                return {
                    "error": "Game package not found",
                    "status_code": 404,
                }
            # Return the latest version
            main = game_package.get("main").get("major")
            return {
                "version": main.get("version"),
                "packages": main.get("game_pkgs", []),
            }
    except httpx.RequestError as e:
        return {
            "error": str(e),
            "status_code": 500,
        }
    except httpx.HTTPStatusError as e:
        return {
            "error": str(e),
            "status_code": e.response.status_code,
        }


@router.get("/", response_class=JSONResponse)
async def get_version(app_version: Annotated[dict, Depends(app_version)]):
    """
    Endpoint to get the latest version of Honkai: Star Rail.
    """
    version_url = "https://sg-hyp-api.hoyoverse.com/hyp/hyp-connect/api/getGamePackages?launcher_id=VYTpXlbWo8"
    import httpx

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(version_url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json().get("data", {}).get("game_packages", [])
            if not data:
                return JSONResponse(
                    status_code=404, content={"error": "No game packages found"}
                )
            # Get game package with game.biz = "hkrpg_global"
            game_package = next(
                (pkg for pkg in data if pkg.get("game").get("biz") == "hkrpg_global"),
                None,
            )
            if not game_package:
                return JSONResponse(
                    status_code=404, content={"error": "Game package not found"}
                )
            # Return the latest version
            main = game_package.get("main").get("major")
            latest_version = {
                "version": main.get("version"),
                "packages": main.get("game_pkgs", []),
            }
            return JSONResponse(content=latest_version)
    except httpx.RequestError as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    except httpx.HTTPStatusError as e:
        return JSONResponse(
            status_code=e.response.status_code, content={"error": str(e)}
        )


@router.get("/current", response_class=JSONResponse)
async def get_current_version():
    """
    Read current version from data.json
    """
    import json
    from pathlib import Path

    data_file = Path(__file__).parent.parent / "data.json"
    if not data_file.exists():
        return JSONResponse(status_code=404, content={"error": "Data file not found"})

    with open(data_file, "r") as file:
        data = json.load(file)

    return JSONResponse(
        content={"version": data.get("version", {"error": "Version not found"})}
    )


@router.get("/outdated", response_class=JSONResponse)
async def is_outdated():
    """
    Check if the current version is outdated compared to the latest version.
    """

    # Get the current version
    current_version_response = await get_current_version()
    if current_version_response.status_code != 200:
        return current_version_response
    current_version = current_version_response.json()
    if isinstance(current_version, dict):
        current_version = current_version.get("version")
    if not current_version:
        return JSONResponse(
            status_code=404, content={"error": "Current version not found"}
        )

    # Get the latest version
    latest_version_response = await get_version()
    if latest_version_response.status_code != 200:
        return latest_version_response
    latest_version = latest_version_response.json()
    if isinstance(latest_version, dict):
        latest_version = latest_version.get("version")
    if not latest_version:
        return JSONResponse(
            status_code=404, content={"error": "Latest version not found"}
        )

    # Compare versions
    if not isinstance(current_version, str) or not isinstance(latest_version, str):
        return JSONResponse(
            status_code=400, content={"error": "Invalid version format"}
        )
    latest_parts = list(map(int, latest_version.split(".")))
    current_parts = list(map(int, current_version.split(".")))
    if latest_parts > current_parts:
        return JSONResponse(
            content={
                "outdated": True,
                "latest_version": latest_version,
                "current_version": current_version,
                "packages": latest_version_response.json().get("packages", []),
            }
        )
    return JSONResponse(content={"outdated": False})
