import requests

from . import lockfile

def get_summoner():
  url = lockfile.get_url("lol-summoner/v1/current-summoner")

  result = lockfile.get_session().get(
    url=url
  )

  if(not result.ok):
    return None

  return result.json()