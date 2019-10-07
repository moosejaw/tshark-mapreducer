import subprocess
import sys

TSHARK_COMMANDS = ['tshark', '-c', '7500']
TSHARK_OUTPUT_FILE = '~/tshark-output.txt'

if __name__ == '__main__':
    with open(TSHARK_OUTPUT_FILE, 'w') as f:
        f.write(subprocess.check_output(TSHARK_COMMANDS,
                shell=True,
                stderr=subprocess.STDOUT))
