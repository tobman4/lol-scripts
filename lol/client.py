import requests

from . import lockfile

def get_gameflow_phase() -> str:
  url = lockfile.get_url("lol-gameflow/v1/gameflow-phase")

  response = lockfile.get_session().get(
    url=url
  )

  if(not response.ok):
    return "UNKNOWN"
  
  return response.text