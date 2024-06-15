from typing import List
import requests
import logging

_versions: List[str] | None = None

def get_versions():
  global _versions

  if(_versions is None):
    logging.info(f"Loading https://ddragon.leagueoflegends.com/api/versions.json");
    result = requests.get("https://ddragon.leagueoflegends.com/api/versions.json")

    if(not result.ok):
      raise Exception("Failed to load versions")

    _versions = result.json()

  return _versions

def get_latest_version():
  return get_versions()[0]

if __name__ == "__main__":
  print(get_latest_version())