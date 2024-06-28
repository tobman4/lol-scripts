import json
import os
from argparse import ArgumentParser, FileType

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

parser.add_argument(
  "-d",
  default="./dbg-data",
  dest="dir",
  type=str
)

args = parser.parse_args()

def ensure_dir(path: str):
  if(os.path.isdir(path)):
    return True
  
  if(os.path.exists(path)):
    print(f"{path} is not a dir");
    return False
  
  os.makedirs(path)
  return True

def write_data(name: str, data: any):
  path = os.path.join(args.dir, f"{name}.json")
  
  if(data is None):
    print(f"No {name} data")
    return

  print(f"Writing {path}")
  with(open(path, "w") as f):
    json.dump(data, f, indent=2)

def old_and_bad(name: str, data: any):
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
  
  if(not ensure_dir(args.dir)):
    exit(1)

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
    


  write_data("user", user)
  write_data("lobby", party)
  write_data("end-of-game", eog_data)
  write_data("champ-select", session)
  c.print(f"[bold]Phase:[/bold] {gamephase}")
