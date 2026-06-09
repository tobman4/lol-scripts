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

  table = Table(title="Players")
  table.add_column("Role")
  table.add_column("Riot ID")
  table.add_column("Champion")
  table.add_column("Level")

  for team in data["teams"]:
    for player in team["players"]:
      table.add_row(
        player["selectedPosition"],
        player["riotIdGameName"] + "#" + player["riotIdTagLine"],
        player["championName"],
        str(player["level"])
      )
    table.add_row() # Empty row to separate teams

  Console().print(table)
