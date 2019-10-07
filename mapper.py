#!/usr/bin/env python3
import sys

for line in sys.stdin:
    # Ignore line if empty (causes problems in reducer)
    if not line:
        continue

    # Get the source IP address as the 3rd entry (index 2) in tshark output
    # And print it as a key-value pair of sourceIP<TAB> count
    line = line.strip()

    # Remove an annoying consecutive whitespace in every other line
    line = ' '.join(line.split())
    line = line + '\n'

    # Get the source IP address
    source_ip = line[2]
    
    # Print the key-value pair to stdout
    print(f'{source_ip}\t1')

