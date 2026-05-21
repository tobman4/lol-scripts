import requests

from .lockfile import api_session

def get_summoner():
  result = api_session.get(
    url="lol-summoner/v1/current-summoner"
  )

  if(not result.ok):
    return None

  return result.json()