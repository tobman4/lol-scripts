import re
import time
import random
import logging
from argparse import Namespace, ArgumentParser, FileType

from rich.logging import RichHandler
from lol.lockfile import api_session

def setup_env(self: ArgumentParser):
  self.add_argument(
    "-l",
    dest="lockfile",
    default="C:\\Riot Games\\League of Legends\\lockfile",
    type=str,
    help="Path to the lockfile"
  )
  self.add_argument(
    "--log-level",
    dest="log_level",
    default="DEBUG",
    type=str,
    help="Logging level (e.g., DEBUG, INFO)"
  )

ArgumentParser.setup_env = setup_env

def init(args: Namespace):
  logging.basicConfig(
    level=args.log_level,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()]
  )
  if hasattr(args, "lockfile"):
    api_session.load_lock(args.lockfile)

def sleep_for_range(txt: str):
  rx = r"^(\d+)(?::(\d+))?$"
  res = re.search(rx,txt)


  if(res is None):
    logging.error(f"Invalid time format \"{txt}\"")
    raise Exception(f"Invalid time format \"{txt}\"")

  min_time = res.group(1)
  max_time = res.group(2)  
  sleep_time = 0

  if(max_time is None):
    sleep_time = int(min_time)
  else:
    sleep_time = random.randrange(
      start=int(min_time),
      stop=int(max_time)
    )

  logging.info(f"Sleeping for {sleep_time}s")
  time.sleep(sleep_time)