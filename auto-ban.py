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

  while(True):
    session = champSelect.set_session()
    if(session is None):
      time.sleep(15)
      continue

    player = champSelect.get_local_player()
    pending_actions = champSelect.get_current_action()

    for action in pending_actions:
      if(action["actorCellId"] == player["cellId"] and action["type"] == "ban"):
        action["championId"] = 103
        champSelect.complete_actions(action)
    
    time.sleep(.5)