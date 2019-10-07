#!/usr/bin/env python3

import subprocess
import sys

TSHARK_NUMBER_OF_PACKETS = 100
TSHARK_COMMANDS = ['tshark', '-c', str(TSHARK_NUMBER_OF_PACKETS)]
TSHARK_OUTPUT_FILE = '/home/hduser/tshark-output.txt'

if __name__ == '__main__':
    print(f'Running tshark and getting {TSHARK_NUMBER_OF_PACKETS} packets...')

    # Write tshark stdout to output file
    with open(TSHARK_OUTPUT_FILE, 'w') as f:
        proc = subprocess.Popen(TSHARK_COMMANDS,
                stdout=f)
        proc.communicate()

    print('Done capturing packets.')

