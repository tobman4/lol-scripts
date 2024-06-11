import requests

from . import lockfile

def get_summoner():
  url = f"https://127.0.1:{lockfile.get_port()}/lol-summoner/v1/current-summoner"

  result = requests.get(
    url=url,
    verify=True,
    auth=("riot", lockfile.get_password())
  )

  if(not result.ok):
    return None

  return result.json()
