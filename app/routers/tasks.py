import asyncio

import httpx
from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["tasks", "examples"])


async def get_reddit_top_async(subreddit: str, data: dict) -> None:  # 2
    async with httpx.AsyncClient() as client:  # 3
        response = await client.get(  # 4
            f"https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5",
            headers={"User-agent": "recipe bot 0.1"},
        )

    subreddit_recipes = response.json()
    subreddit_data = []
    for entry in subreddit_recipes["data"]["children"]:
        score = entry["data"]["score"]
        title = entry["data"]["title"]
        link = entry["data"]["url"]
        subreddit_data.append(f"{str(score)}: {title} ({link})")
    data[subreddit] = subreddit_data


@router.get("/1")
async def test():
    data: dict = {}

    await asyncio.gather(  # 5
        get_reddit_top_async("recipes", data),
        get_reddit_top_async("easyrecipes", data),
        get_reddit_top_async("TopSecretRecipes", data),
    )

    return data


def get_reddit_top(subreddit: str, data: dict) -> None:
    response = httpx.get(
        f"https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5",
        headers={"User-agent": "recipe bot 0.1"},
    )  # 2
    subreddit_recipes = response.json()
    subreddit_data = []
    for entry in subreddit_recipes["data"]["children"]:
        score = entry["data"]["score"]
        title = entry["data"]["title"]
        link = entry["data"]["url"]
        subreddit_data.append(f"{str(score)}: {title} ({link})")
    data[subreddit] = subreddit_data


@router.get("/2")
def fetch_ideas() -> dict:
    data: dict = {}  # 3
    get_reddit_top("recipes", data)
    get_reddit_top("easyrecipes", data)
    get_reddit_top("TopSecretRecipes", data)

    return data
