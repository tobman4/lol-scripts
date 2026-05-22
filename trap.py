import time
import logging
from datetime import datetime
from argparse import ArgumentParser

import util

from lol import friends, lobby


parser = ArgumentParser("trap", description="invite somone then leave the lobby")
util.setup_env(parser)

parser.add_argument(
  "-t", "--target",
  required=True
)

def look_for_targer(target: str) -> (int, str):
  """
  Make sure target is online
  """
  players = friends.get_friendlist()

  for player in players:
    name = player["gameName"] + "#" + player["gameTag"]
    if(name == target):
      logging.debug(f"Found target {target} with availability {player['availability']}")

      return (player["summonerId"], player["id"]) if player["availability"] not in ["offline", "mobile"] else None
  
  raise Exception("Bad target riotID")

def triger_trap(summonerId: int, chatId: str):
  """
  Create lobby and invite target
  """
  logging.info(f"Creating lobby and inviting target with summonerId {summonerId}")

  lobby.try_create_lobby(420)
  lobby.invite_to_lobby(summonerId)
  friends.send_message("Hey dude want to play a game?")

def getaway():
  """
  Cleanup and go to sleep
  """
  start = datetime.now()

  while True:
    members = lobby.get_lobby_members()

    if(len(members) >= 2):
      logging.info("Target is here, scram!!")
      lobby.leav_lobby()
      return

    if((datetime.now() - start).total_seconds() > 30):
      lobby.leav_lobby()
      return

    logging.info(f"Waiting for target to join")
    time.sleep(5)

def main():

  while True:    

    (summonerId, chatId) = look_for_targer(args.target)

    if(not summonerId):
      time.sleep(3)
      continue
    
    triger_trap(summonerId, chatId)
    getaway()
    
    util.sleep_for_range("60:120")



if __name__ == "__main__":
  args = parser.parse_args()
  util.init(args)
  
  try:
    main()
  except KeyboardInterrupt:
    logging.info("Exiting...")
    exit(0)
