import random
import logging
from argparse import ArgumentParser
import time

from lol import lobby
import util


parser = ArgumentParser("test", description="test")
util.setup_env(parser)

parser.add_argument(
  "-i", "--interval",
  type=int,
  default=2,
  help="Interval between checks (in seconds)"
)

args = parser.parse_args()


def social_distancing():
  data = lobby.get_lobby()
  if(not data):
    raise Exception("Not in lobby")
  
  my_puuid = data["localMember"]["puuid"]
  my_index = data["localMember"]["subteamIndex"]


  if(len(data["members"]) <= 1):
    logging.info("No one else in lobby :(")
    return

  for member in data["members"]:


    if(member["subteamIndex"] == my_index and member["puuid"] != my_puuid):
      
      new_inext = random.randint(1, 6)
      sub_index = random.randint(1, 3)
      logging.info(f"Moving to subteam {new_inext}")
      lobby.move_sub_team(new_inext, sub_index)


if __name__ == "__main__":  
  util.init(args)

  while True:
    social_distancing()
    time.sleep(args.interval)