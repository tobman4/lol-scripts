import json
from argparse import ArgumentParser, FileType

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

if __name__ == "__main__":
  lockfile.load_file(args.lockfile)

  console = Console()

  with console.status("Doing funny") as status:
    console.log("creating tft lobby")
    lobby.try_create_lobby(1090) # tft queueId is 1090

    if(args.try_start):
      console.log("starting queue")
      lobby.start_search()

    console.log("leaving lobby")
    lobby.leav_lobby()
