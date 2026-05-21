import json
from typing import List

import requests

from .lockfile import api_session

def get_all_loot(type: str = ""):
  result = api_session.get(
    url="lol-loot/v1/player-loot"
  )

  if(not result.ok):
    return []

  data = result.json()
  return data

def get_loot_by_lootId(id: str):
  loot = get_all_loot()

  for item in loot:
    if(item["lootId"] == id):
      return item
  
  return None

def yolo_disenchant(itemIds: List[str], count: int = 1):

  result = api_session.post(
    url=f"lol-loot/v1/recipes/CHAMPION_RENTAL_disenchant/craft?repeat={count}",
    headers={
      "Content-Type": "application/json"
    },
    data=json.dumps(itemIds)
  )

  if(not result.ok):
    print(result.json())
    return None

  return result.json()

def craft():
  pass