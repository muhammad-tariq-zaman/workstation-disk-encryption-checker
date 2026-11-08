"""Workstation disk encryption status.

Usage: python3 main.py workstations.csv
CSV columns: host,encrypted (yes/no),method.
ENCRYPTED with a named method, METHOD UNKNOWN when encrypted but
no method recorded, NOT ENCRYPTED otherwise. Not-encrypted first.
"""
import argparse, csv, sys

def check(rows):
    out = []
    for row in rows:
        encrypted = row["encrypted"].strip().lower() == "yes"
        method = row["method"].strip()
        if encrypted and method:
            verdict = "ENCRYPTED"
        elif encrypted:
            verdict = "METHOD UNKNOWN"
        else:
            verdict = "NOT ENCRYPTED"
        out.append((row["host"], method or "-", verdict))
    order = {"NOT ENCRYPTED": 0, "METHOD UNKNOWN": 1, "ENCRYPTED": 2}
    return sorted(out, key=lambda r: order[r[2]])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for host, method, verdict in check(list(csv.DictReader(f))):
            print(f"{host}: {verdict} ({method})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
