import json

import requests

from .lockfile import api_session
from . import summoner

def get_current_action():
  response = api_session.get("lol-champ-select/v1/session")
  if not response.ok:
    return None
  session = response.json()

  if(session is None):
    return

  inProgress = []

  actions = session.get("actions")

  for action_group in actions:
    for action in action_group:
      if(action["isInProgress"] and not action["completed"]):
        inProgress.append(action)

  return inProgress

  pass

def complete_actions(data):
  action_id = data["id"]

  # Update action
  api_session.patch(
    url=f"lol-champ-select/v1/session/actions/{action_id}",
    headers={
      "Content-Type": "application/json"
    },
    data=json.dumps(data)
  )

  # Complete
  api_session.post(
    url=f"lol-champ-select/v1/session/actions/{action_id}/complete"
  )

def get_local_player():
  summoner_data = summoner.get_summoner()
  response = api_session.get("lol-champ-select/v1/session")
  if not response.ok:
    return None
  session = response.json()

  if(session is None):
    return None

  team = session["myTeam"]

  for player in team:
    if(player["puuid"] == summoner_data["puuid"]):
      return player

  return None

def reroll():
  api_session.post(
    url="lol-champ-select/v1/session/my-selection/reroll"
  )


def swapFromBench(champId: int):
  api_session.post(
    url=f"lol-champ-select/v1/session/bench/swap/{champId}"
  )