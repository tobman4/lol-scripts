
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

  requests.post(
    url,
    verify=False,
    auth=("riot",args.password),
    headers={
      "content-type": "application/json"
    },
    data=json.dumps(body)
  )


if __name__ == "__main__":
  try_create_lobby(args.queueId)
