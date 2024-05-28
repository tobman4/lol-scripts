import json
import requests

import rich

from . import lockfile

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
