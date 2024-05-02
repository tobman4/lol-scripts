import json
from argparse import ArgumentParser

import requests
from rich.console import Console

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = ArgumentParser()

parser.add_argument(
  "-w",
  dest="password",
  required=True
)

parser.add_argument(
  "-p",
  type=int,
  dest="port",
  required=True
)

parser.add_argument(
  "-s",
  help="Try to start the queue before leaving",
  dest="try_start",
  action="store_true"
)


args = parser.parse_args()

def create_loby():
  
  url = f"https://127.0.0.1:{args.port}/lol-lobby/v2/lobby"

  body = {
    "queueId": 1090 # TFT queue id
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

def start_search():
  url = f"https://127.0.0.1:{args.port}/lol-lobby/v2/lobby/matchmaking/search"

  requests.post(
    url,
    verify=False,
    auth=("riot",args.password),
  )

def leav_loby():
  url = f"https://127.0.0.1:{args.port}/lol-lobby/v2/lobby"

  requests.delete(
    url,
    verify=False,
    auth=("riot",args.password)
  )


if __name__ == "__main__":

  console = Console()

  with console.status("Doing funny") as status:
    console.log("creating tft loby")
    create_loby()

    if(args.try_start):
      console.log("starting queue")
      start_search()

    console.log("leaving loby")
    leav_loby()