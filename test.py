from argparse import ArgumentParser, FileType

from lol import *

parser = ArgumentParser("Test script")

parser.add_argument(
  "-l",
  dest="lockfile",
  required="true",
  type=FileType("r")
)

args = parser.parse_args()

if __name__ == "__main__":
  print(f"Lockfile: {args.lockfile}")
  lockfile.load_file(args.lockfile)

  password = lockfile.get_password()
  print(f"Password: {password}")

  port = lockfile.get_port()
  print(f"Port: {port}")
  pass
