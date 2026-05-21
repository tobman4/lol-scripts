import requests

from .lockfile import api_session

def get_eog_data():
  response = api_session.get(
    url="lol-end-of-game/v1/eog-stats-block"
  )

  if(not response.ok):
    return None
  
  return response.json()