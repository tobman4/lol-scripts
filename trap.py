import time
import logging
from argparse import ArgumentParser

import util

from lol import friends


parser = ArgumentParser("trap", description="invite somone then leave the lobby")
util.setup_env(parser)

parser.add_argument(
  "-t", "--target",
  required=True
)

def look_for_targer(target: str) -> bool:
  """
  Make sure target is online
  """
  players = friends.get_friendlist()

  for player in players:
    name = player["gameName"] + "#" + player["gameTag"]
    if(name == target):
      logging.info(f"Found target {target} with availability {player['availability']}")
      return player["availability"] not in ["offline", "mobile"]
  
  raise Exception("Bad target riotID")

def triger_trap():
  """
  Create lobby and invite target
  """
  pass

def getaway():
  """
  Cleanup and go to sleep
  """
def main():

  while True:    
    if(not look_for_targer(args.target)):
      time.sleep(3)
      continue
    
    exit(0)



if __name__ == "__main__":
  args = parser.parse_args()
  util.init(args)

  try:
    main()
  except KeyboardInterrupt:
    logging.info("Exiting...")
    exit(0)