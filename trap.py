import time
import logging
from argparse import ArgumentParser

import util

from lol import friends, lobby


parser = ArgumentParser("trap", description="invite somone then leave the lobby")
util.setup_env(parser)

parser.add_argument(
  "-t", "--target",
  required=True
)

def look_for_targer(target: str) -> int:
  """
  Make sure target is online
  """
  players = friends.get_friendlist()

  for player in players:
    name = player["gameName"] + "#" + player["gameTag"]
    if(name == target):
      logging.info(f"Found target {target} with availability {player['availability']}")

      return player["summonerId"] if player["availability"] not in ["offline", "mobile"] else None
  
  raise Exception("Bad target riotID")

def triger_trap(summonerId: int):
  """
  Create lobby and invite target
  """
  lobby.try_create_lobby(420)
  lobby.invite_to_lobby(summonerId)

def getaway():
  """
  Cleanup and go to sleep
  """
  while True:
    members = lobby.get_lobby_members()

    if(len(members) >= 2):
      logging.info("Target is here, scram!!")
      lobby.leav_lobby()
      return

    logging.info(f"Waiting for target to join")
    time.sleep(5)

def main():

  while True:    

    summonerId = look_for_targer(args.target)

    if(not summonerId):
      time.sleep(3)
      continue

    triger_trap(summonerId)
    getaway()
    
    exit(0)



if __name__ == "__main__":
  args = parser.parse_args()
  util.init(args)

  try:
    main()
  except KeyboardInterrupt:
    logging.info("Exiting...")
    exit(0)