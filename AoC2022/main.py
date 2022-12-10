import argparse
from datetime import datetime
import days  # noqa

parser = argparse.ArgumentParser("Advent of Code")
parser.add_argument("--day", help="The day to run. If omitted defaults to today", type=int)
args = parser.parse_args()

if __name__ == '__main__':
    if args.day is not None:
        day = args.day
    else:
        day = datetime.now().day
    exec(f"""
d = days.Day{day}()
d.run()
    """, {}, globals())
