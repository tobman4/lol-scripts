import json

import requests

from . import lockfile, summoner

def shallow_call(func):
  def wrapper():
    result = func()

    if(not result.ok):
      return None
  
    return result.json()

  return wrapper

@shallow_call
def get_session():
  url = lockfile.get_url("lol-champ-select/v1/session")
  
  return lockfile.get_session().get(
    url=url
  )

def get_current_action():
  session = get_session()

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

  path_url = lockfile.get_url(f"lol-champ-select/v1/session/actions/{action_id}")
  comlete_url = lockfile.get_url(f"lol-champ-select/v1/session/actions/{action_id}/complete")

  # Update action
  lockfile.get_session().patch(
    url=path_url,
    headers={
      "Content-Type": "application/json"
    },
    data=json.dumps(data)
  )

  # Complete
  lockfile.get_session().post(
    url=comlete_url
  )

def get_local_player():
  summoner_data = summoner.get_summoner()
  session = get_session()

  if(session is None):
    return None

  team = session["myTeam"]

  for player in team:
    if(player["puuid"] == summoner_data["puuid"]):
      return player

  return None

def reroll():
  url = lockfile.get_url("lol-champ-select/v1/session/my-selection/reroll")

  lockfile.get_session().post(
    url=url
  )


def swapFromBench(champId: int):
  url = lockfile.get_url(f"lol-champ-select/v1/session/bench/swap/{champId}")

  lockfile.get_session().post(
    url=url
  )