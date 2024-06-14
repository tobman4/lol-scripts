import requests

from . import lockfile

def get_gameflow_phase() -> str:
  url = f"https://127.0.0.1:{lockfile.get_port()}/lol-gameflow/v1/gameflow-phase"

  response = requests.get(
    url=url,
    verify=False,
    auth=("riot",lockfile.get_password())
  )

  if(not response.ok):
    return "UNKNOWN"
  
  return response.text