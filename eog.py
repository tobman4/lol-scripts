import time
import logging
from argparse import ArgumentParser

from rich.table import Table
from rich.console import Console

import util
from lol import lockfile, eog

parser = ArgumentParser("End of Game stats viewer")
parser.setup_env()

args = parser.parse_args()

if __name__ == "__main__":
  util.init(args)
  data = eog.get_eog_data()

  table = Table(Title="Players")
  table.add_column("Role")
  table.add_column("Riot ID")
  table.add_column("Champion")
  table.add_column("Level")

    # Team 1
  for player in data["teams"][0]["players"]:
    table.add_row(
      player["selectedPosition"],
      f"{player["riotIdGameName"]}#{player["riotIdTagLine"]}",
      player["championName"]
      player["level"]
    )

  # Team 2
  for player in data["teams"][1]["players"]:
    table.add_row(
      player["selectedPosition"],
      f"{player["riotIdGameName"]}#{player["riotIdTagLine"]}",
      player["championName"]
      player["level"]
    )
    
  Console().print(table)
