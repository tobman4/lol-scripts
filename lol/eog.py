import requests

from . import lockfile

def get_eog_data():
  url = lockfile.get_url("lol-end-of-game/v1/eog-stats-block")

  response = lockfile.get_session().get(
    url=url
  )

  if(not response.ok):
    return None
  
  return response.json()