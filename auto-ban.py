import time
import logging
from argparse import ArgumentParser, FileType

import rich
from rich.console import Console
from rich.logging import RichHandler
import rich.spinner

from lol import lockfile, champSelect

parser = ArgumentParser("Test script")

parser.add_argument(
  "-l",
  dest="lockfile",
  default="C:\\Riot Games\\League of Legends\\lockfile",
  type=FileType("r")
)

parser.add_argument(
  "-i",
  dest="championID",
  type=int,
  default=103,
  help="Champion ID to ban. Default is Ahri"
)

args = parser.parse_args()

if __name__ == "__main__":
  logging.basicConfig(handlers=[RichHandler()])
  lockfile.load_file(args.lockfile)
  console = Console()

  with console.status("[bold red]I am alive...[/bold red]") as status:
    while(True):
      session = champSelect.get_session()
      if(session is None):
        status.update("[bold yellow]Not in champ select zzz[/bold yellow]")
        time.sleep(15)
        continue
      else:
        status.update("[bold green]In champ select[/bold green]")
      
      player = champSelect.get_local_player()
      pending_actions = champSelect.get_current_action()
      
      for action in pending_actions:
        if(action["actorCellId"] == player["cellId"] and action["type"] == "ban"):
          # console.print("[bold red]Hammer time!![/bold red]")
          status.update("[bold red]Hammer time!!!!![/bold red]")
          action["championId"] = args.championID
          champSelect.complete_actions(action)

      # time.sleep(.1)