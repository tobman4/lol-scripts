import requests

from .lockfile import api_session

def get_gameflow_phase() -> str:
  response = api_session.get(
    url="lol-gameflow/v1/gameflow-phase"
  )

  if(not response.ok):
    return "UNKNOWN"
  
  return response.text