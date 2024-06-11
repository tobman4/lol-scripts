from argparse import ArgumentParser

from lol import summoner

if __name__ == "__main__":

  user = summoner.get_summoner()
  print(user)
