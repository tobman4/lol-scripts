import json
from argparse import ArgumentParser, FileType

import requests
from rich.console import Console

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from lol import *

parser = ArgumentParser(
  description="Change lobby to tft then leav"
)

parser.add_argument(
  "-l",
  dest="lockfile",
  default="C:\\Riot Games\\League of Legends\\lockfile",
  type=FileType("r")
)

parser.add_argument(
  "-s",
  help="Try to start the queue before leaving",
  dest="try_start",
  action="store_true"
)


args = parser.parse_args()

def create_lobby():
  
  url = f"https://127.0.0.1:{lockfile.get_port()}/lol-lobby/v2/lobby"

  body = {
    "queueId": 1090 # TFT queue id
  }

  requests.post(
    url,
    verify=False,
    auth=("riot",lockfile.get_password()),
    headers={
      "content-type": "application/json"
    },
    data=json.dumps(body)
  )

def start_search():
  url = f"https://127.0.0.1:{lockfile.get_port()}/lol-lobby/v2/lobby/matchmaking/search"

  requests.post(
    url,
    verify=False,
    auth=("riot",lockfile.get_password()),
  )

def leav_lobby():
  url = f"https://127.0.0.1:{lockfile.get_port()}/lol-lobby/v2/lobby"

  requests.delete(
    url,
    verify=False,
    auth=("riot",lockfile.get_password())
  )


if __name__ == "__main__":
  lockfile.load_file(args.lockfile)

  console = Console()

  with console.status("Doing funny") as status:
    console.log("creating tft lobby")
    create_lobby()

    if(args.try_start):
      console.log("starting queue")
      start_search()

    console.log("leaving lobby")
    leav_lobby()
