import requests

import lockfile

def get_eog_data():
  url = f"https://127.0.0.1:{lockfile.get_port()}/lol-end-of-game/v1/eog-stats-block"

  response = requests.get(
    url=url,
    verify=False,
    auth=("riot",lockfile.get_password())
  )

  if(not response.ok):
    return None
  
  return response.json()