import time
from datetime import datetime
from argparse import ArgumentParser,FileType

from rich.console import Console

from lol import *

parser = ArgumentParser("Test script")

parser.add_argument(
  "-l",
  default="C:\\Riot Games\\League of Legends\\lockfile",
  dest="lockfile",
  required="true",
  type=FileType("r")
)

parser.add_argument(
  "-m",
  help="TODO",
  default=30,
  dest="max_queue",
  type=int
)

parser.add_argument(
  "-b",
  help="TODO",
  default=5,
  dest="break_time",
  type=int
)

args = parser.parse_args()

if __name__ == "__main__":
  console = Console()

  lockfile.load_file(args.lockfile)

  console.log("Starting queue")
  lobby.start_search()
  start_time = datetime.now()

  while(True):
    sec_in_queue = (datetime.now() - start_time).total_seconds()
    state = lobby.get_search_state()
    # console.log(f"[{sec_in_queue:.2f}]: {state}")

    if(sec_in_queue > args.max_queue and state == "Searching"):
      console.log(f"[{sec_in_queue:.2f}] Queue to long")
      lobby.stop_search()
      time.sleep(args.break_time)

      console.log("[0] Restarting queue")
      lobby.start_search()
      start_time = datetime.now()

    if(state == "Found"):
      console.log(f"[{sec_in_queue:.2f}] Found game")
      lobby.accept_ready_check()
      exit(0)

    time.sleep(2)