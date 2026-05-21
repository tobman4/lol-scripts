import time

from argparse import ArgumentParser, FileType

import util
from lol import lockfile, champSelect

parser = ArgumentParser("Test script")
parser.setup_env()

args = parser.parse_args()

if __name__ == "__main__":
  util.init(args)

  player = champSelect.get_local_player()
  if(player is None):
    print("Not in champ select")
    exit(1)
  
  champId = player["championId"]
  print(f"Selected champ: {champId}")

  champSelect.reroll()

  time.sleep(.2)

  champSelect.swapFromBench(champId)
