
from io import TextIOWrapper
import json
from time import sleep
from argparse import ArgumentParser, FileType

import requests
# from rich.console import Console

from lol import *

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

# parser.add_argument(
#   "-q",
#   dest="queueId",
#   help="queue id to create lobby"
# )

parser.add_argument(
  "-s",
  type=int,
  required=True,
  dest="start"
)

parser.add_argument(
  "-e",
  type=int,
  required=True,
  dest="end"
)

parser.add_argument(
  "-d",
  type=int,
  default=1,
  dest="delay"
)

args = parser.parse_args()

def get_lobby_info(data):
  config = data.get("gameConfig")
  
  return (
    config.get("gameMode"),
    config.get("mapId"),
    config.get("queueId")
  )

def write_info(id: int):
  data = lobby.try_create_lobby(id)
  if(data is None):
    return

  csv_line = get_lobby_info(data)
  str_line = map(lambda e: str(e), csv_line)

  file: TextIOWrapper = args.out
  file.write(str(id) + ",")
  file.write(
    ",".join(str_line) + "\n"
  )

if __name__ == "__main__":
  lockfile.load_file(args.lockfile)

  if(args.end < args.start):
    print("end cant be less then start")
    exit(1)

  file: TextIOWrapper = args.out
  file.write(
    "id,gameMode,mapId,queueId\n"
  )

  i = args.start
  while(i <= args.end):
    print(f"Trying queue id {i}")
    write_info(i)
    i+=1
    sleep(args.delay);

  file.close()
