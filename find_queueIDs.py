
from io import TextIOWrapper
import json
from argparse import ArgumentParser, FileType

import requests
# from rich.console import Console

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = ArgumentParser(
  description="TODO"
)

parser.add_argument(
  "-l",
  dest="lockfile",
  default="C:\\Riot Games\\League of Legends\\lockfile",
  type=FileType("r")
)

parser.add_argument(
  "-f",
  dest="out",
  required=True,
  type=FileType("w")
)

parser.add_argument(
  "-q",
  dest="queueId",
  help="queue id to create lobby"
)

args = parser.parse_args()

def load_lockfile():
  
  data = args.lockfile.readline().strip().split(":")
  args.password = data[3]
  args.port = int(data[2])

def try_create_lobby(id: int):
  url = f"https://127.0.0.1:{args.port}/lol-lobby/v2/lobby"

  body = {
    "queueId": id
  }

  response = requests.post(
    url,
    verify=False,
    auth=("riot",args.password),
    headers={
      "content-type": "application/json"
    },
    data=json.dumps(body)
  )

  if(not response.ok):
    return None

  return response.json()

def get_lobby_info(data):
  config = data.get("gameConfig")
  
  return (
    config.get("gameMode"),
    config.get("mapId"),
    config.get("queueId")
  )

if __name__ == "__main__":
  load_lockfile()
  data = try_create_lobby(args.queueId)
  
  if(data is None):
    exit(1)

  csv_line = get_lobby_info(data)
  

  file: TextIOWrapper = args.out

  file.write(
    "id,gameMode,mapId,queueId\n"
  )
  file.write(str(args.queueId) + ",")

  str_line = map(lambda e: str(e), csv_line)
  file.write(
    ",".join(str_line) + "\n"
  )
