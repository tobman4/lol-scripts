import json
import requests

import rich

from . import lockfile

def get_lobby():
  url = lockfile.get_url("lol-lobby/v2/lobby")

  response = lockfile.get_session().get(
    url=url,
    verify=False,
    auth=("riot", lockfile.get_password())
  )

  if(not response.ok):
    return None
  
  return response.json()

def try_create_lobby(id: int):
  url = lockfile.get_url("lol-lobby/v2/lobby")

  body = {
    "queueId": id
  }

  response = lockfile.get_session().post(
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
  url = lockfile.get_url("lol-lobby/v2/lobby")

  lockfile.get_session().delete(
    url,
    verify=False,
    auth=("riot",lockfile.get_password())
  )

def start_search():
  url = lockfile.get_url("lol-lobby/v2/lobby/matchmaking/search")

  lockfile.get_session().post(
    url,
    verify=False,
    auth=("riot",lockfile.get_password()),
  )

def stop_search():
  url = lockfile.get_url("lol-lobby/v2/lobby/matchmaking/search")

  lockfile.get_session().delete(
    url=url,
    verify=False,
    auth=("riot",lockfile.get_password())
  )

def get_search_state():
  url = lockfile.get_url("lol-lobby/v2/lobby/matchmaking/search-state")

  response = lockfile.get_session().get(
    url=url,
    verify=False,
    auth=("riot", lockfile.get_password())
  )

  if(not response.ok):
    return None

  data = response.json()

  return data["searchState"]

def accept_ready_check():
  url = lockfile.get_url("lol-matchmaking/v1/ready-check/accept")

  lockfile.get_session().post(
    url=url,
    verify=False,
    auth=("riot",lockfile.get_password())
  )

def stop_queue():
  url = lockfile.get_url("lol-matchmaking/v1/search")

  lockfile.get_session().delete(
    url=url,
  )