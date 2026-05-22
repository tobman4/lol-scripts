import time
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
    name = f"{players["gameName"]}#{player["gameTag"]}"
    if(name == target):
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

if __name__ == "__main__":
  args = parser.parse_args()
  util.init(args)



  while True:
    
    if(not look_for_targer(args.target)):
      time.sleep(3)
      continue
    
    exit(0)
