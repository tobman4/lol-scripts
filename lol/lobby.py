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