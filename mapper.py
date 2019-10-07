#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Get the source IP address as the 3rd entry (index 2) in tshark output
    # And print it as a key-value pair of sourceIP<TAB> count
    line = line.strip().split(' ')
    source_ip = line[2]
    # Print the key-value pair to stdout
    print(f'{source_ip}\t1')


