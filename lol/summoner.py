import requests

from . import lockfile

def get_summoner():
  url = f"https://127.0.0.1:{lockfile.get_port()}/lol-summoner/v1/current-summoner"

  result = lockfile.get_session().get(url=url)

  if(not result.ok):
    return None

  return result.json()