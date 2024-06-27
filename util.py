import re
import time
import random
import logging
from argparse import Namespace

from rich.logging import RichHandler

def add_logging(args: Namespace):
  
  logging.basicConfig(
    level="DEBUG",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()]
  )

def sleep_for_range(txt: str):
  rx = "^(\d+)(?::(\d+))?$"
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