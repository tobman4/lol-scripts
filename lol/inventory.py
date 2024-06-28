import json
from typing import List

import requests

from . import lockfile

def get_all_loot(type: str = ""):
  url = lockfile.get_url("lol-loot/v1/player-loot")
  result = lockfile.get_session().get(
    url=url
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

  url = lockfile.get_url(f"lol-loot/v1/recipes/CHAMPION_RENTAL_disenchant/craft?repeat={count}")
  result = lockfile.get_session().post(
    url=url,
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