import json
import requests

import rich

from . import lockfile

def get_lobby():
  url = f"https://127.0.0.1:{lockfile.get_port()}/lol-lobby/v2/lobby"

  response = requests.get(
    url=url,
    verify=False,
    auth=("riot", lockfile.get_password())
  )

  if(not response.ok):
    return None
  
  return response.json()

def try_create_lobby(id: int):
  url = f"https://127.0.0.1:{lockfile.get_port()}/lol-lobby/v2/lobby"

  body = {
    "queueId": id
  }

  response = requests.post(
    url=url,
    verify=False,
    auth=("riot",lockfile.get_password()),
    headers={
      "content-type": "application/json"
    },
    data=json.dumps(body)
  )

  if(not response.ok):
    return None

  return response.json()

def leav_lobby():
  url = f"https://127.0.0.1:{lockfile.get_port()}/lol-lobby/v2/lobby"

  requests.delete(
    url,
    verify=False,
    auth=("riot",lockfile.get_password())
  )

def start_search():
  url = f"https://127.0.0.1:{lockfile.get_port()}/lol-lobby/v2/lobby/matchmaking/search"

  requests.post(
    url,
    verify=False,
    auth=("riot",lockfile.get_password()),
  )

def stop_search():
  url = f"https://127.0.0.1:{lockfile.get_port()}/lol-lobby/v2/lobby/matchmaking/search"

  requests.delete(
    url=url,
    verify=False,
    auth=("riot",lockfile.get_password())
  )

def get_search_state():
  url = f"https://127.0.0.1:{lockfile.get_port()}/lol-lobby/v2/lobby/matchmaking/search-state"

  response = requests.get(
    url=url,
    verify=False,
    auth=("riot", lockfile.get_password())
  )

  if(not response.ok):
    return None

  data = response.json()

  return data["searchState"]

def accept_ready_check():
  url = f"https://127.0.0.1:{lockfile.get_port()}/lol-matchmaking/v1/ready-check/accept"

  requests.post(
    url=url,
    verify=False,
    auth=("riot",lockfile.get_password())
  )

def stop_queue():
  url = f"https://127.0.0.1:{lockfile.get_port()}/lol-matchmaking/v1/search"

  requests.delete(
    url=url,
    verify=False,
    auth=("riot",lockfile.get_password())
  )