import argparse
import json
import csv
import logging
import sys

import rich
import rich.json

import util
import lol.inventory

parser = argparse.ArgumentParser(description="Dump Inventory")
parser.setup_env()

parser.add_argument(
    "--format",
    choices=["console", "json", "csv"],
    default="console",
    help="Output format"
)
parser.add_argument(
    "--output",
    type=argparse.FileType('w'),
    default=sys.stdout,
    help="Output file path for json or csv"
)

def main():
    args = parser.parse_args()
    util.init(args)

    data = lol.inventory.get_loot_items()

    for item in data:
        if item.get("expiryTime", -1) != -1:
            logging.warning(f"Item {item.get('lootName')} has expiryTime != -1: {item.get('expiryTime')}")

    if args.format == "json":
        json.dump(data, args.output, indent=4)
        args.output.write('\n')
    elif args.format == "csv":
        fieldnames = ["lootName", "displayCategories", "expiryTime", "storeItemId"]
        writer = csv.DictWriter(args.output, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        for item in data:
            writer.writerow(item)
    elif args.format == "console":
        rich.print(rich.json.JSON(json.dumps(data)))

if __name__ == "__main__":
    main()
