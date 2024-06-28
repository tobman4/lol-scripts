from argparse import ArgumentParser, FileType
import json

import rich.json
from rich.panel import Panel
from rich import pretty, console

from lol import *

parser = ArgumentParser("TODO")

parser.add_argument(
  "-l",
  default="C:\\Riot Games\\League of Legends\\lockfile",
  dest="lockfile",
  type=FileType("r")
)

args = parser.parse_args()

def render_data_block(name: str, data: any):
  if(data is None):
    c.print(f"[bold red]No {name} data![/bold red]")
    return

  json_str = json.dumps(data)
  p = Panel(
    rich.json.JSON(
      json_str,
      indent=2
    )
  )
  p.title = name
  c.print(p)

  pass

if __name__ == "__main__":
  
  # Prep
  data = {}
  # pretty.install()
  c = console.Console()

  lockfile.load_file(args.lockfile)

  # Collet data
  with c.status("Getting data...") as status:
    user = summoner.get_summoner()
    party = lobby.get_lobby()  
    gamephase = client.get_gameflow_phase()
    eog_data = eog.get_eog_data()
    session = champSelect.get_session()
    


  render_data_block("User", user)
  render_data_block("Lobby", party)
  render_data_block("EOG", eog_data)
  render_data_block("Champ select session", session)
  c.print(f"[bold]Phase:[/bold] {gamephase}")