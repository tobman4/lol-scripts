import time

from argparse import ArgumentParser, FileType

from lol import lockfile, champSelect

parser = ArgumentParser("Test script")

parser.add_argument(
  "-l",
  dest="lockfile",
  default="C:\\Riot Games\\League of Legends\\lockfile",
  type=FileType("r")
)

args = parser.parse_args()

if __name__ == "__main__":
  lockfile.load_file(args.lockfile)

  player = champSelect.get_local_player()
  if(player is None):
    print("Not in champ select")
    exit(1)
  
  champId = player["championId"]
  print(f"Selected champ: {champId}")

  champSelect.reroll()

  time.sleep(.2)

  champSelect.swapFromBench(champId)