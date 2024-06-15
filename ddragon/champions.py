import logging

import requests

from . import version

_champs = None

def get_champions():
  global _champs

  if(_champs is None):
    ver = version.get_latest_version()

    logging.info(f"Loading https://ddragon.leagueoflegends.com/cdn/{ver}/data/en_US/champion.json")
    result = requests.get(f"https://ddragon.leagueoflegends.com/cdn/{ver}/data/en_US/champion.json")

    if(not result.ok):
      raise Exception("Faild to load https://ddragon.leagueoflegends.com/cdn/14.12.1/data/en_US/champion.json")
    
    _champs = result.json()["data"]

  return _champs

def get_by_name_detailed(name: str):
  ver = version.get_latest_version()
  result = requests.get(f"https://ddragon.leagueoflegends.com/cdn/{ver}/data/en_US/champion/{name}.json")

  if(not result.ok):
    raise Exception("Faild to load champion data")
  
  return result.json()

def get_by_name(name: str):
  champs = get_champions()

  if(name not in champs):
    raise KeyError(f"No champ named {name}")
  
  return champs[name]