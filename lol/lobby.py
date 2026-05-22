import json
import requests

import rich

# from . import lockfile
from .lockfile import api_session

def get_lobby():
  response = api_session.get("lol-lobby/v2/lobby")

  if(not response.ok):
    return None
  
  return response.json()

def try_create_lobby(id: int):
  body = {
    "queueId": id
  }

  response = api_session.post(
    url="lol-lobby/v2/lobby",
    headers={
      "content-type": "application/json"
    },
    data=json.dumps(body)
  )

  if(not response.ok):
    return None

  return response.json()

def leav_lobby():
  api_session.delete("lol-lobby/v2/lobby")


def start_search():
  api_session.post("lol-lobby/v2/lobby/matchmaking/search")

def stop_search():
  api_session.delete("lol-lobby/v2/lobby/matchmaking/search")

def get_search_state():

  response = api_session.get("lol-lobby/v2/lobby/matchmaking/search-state")

  if(not response.ok):
    return None

  data = response.json()

  return data["searchState"]

def accept_ready_check():
  api_session.post("lol-matchmaking/v1/ready-check/accept")

def stop_queue():
  api_session("lol-matchmaking/v1/search")

def invite_to_lobby(summonerId: int):
  api_session.post(f"lol-lobby/v2/lobby/invitations", json=[{"toSummonerId": summonerId}])

def get_lobby_members():
  response = api_session.get("lol-lobby/v2/lobby/members")

  if(not response.ok):
    return []

  return response.json()