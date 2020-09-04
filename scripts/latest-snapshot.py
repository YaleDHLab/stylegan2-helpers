import glob2
import sys

# Get the latest snapshot

fakes = sorted(glob2.glob("./results/**/network-snapshot-[0-9]*.pkl"))

if len(fakes) < 1:
    print("Found no snapshots", file=sys.stderr)
    exit(1)

print (fakes[-1])
