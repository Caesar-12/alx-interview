#!/usr/bin/python3
"""Script that reads from stdin and compute metrics"""

import sys
from datetime import datetime

"""
import keyboard

def key_interrupt():
    keyboard.wait('ctrl' + 'c')
"""

def metric_compute():
    """Compute metrics"""
    mid_str = "GET /projects/260 HTTP/1.1"
    lines = 1
    try:
        for line in sys.stdin:
            input_str = line.strip()
            details = input_str.split()
            try:
                ip = str(details[0])
                status, size = int(details[4]), int(details[5])
                dat = datetime.strptime(details[2], '%Y-%m-%d %H:%M:%S.%f')
            except ValueError:
                 continue

            right_str = '{} - [{}] "{}" {} {}'.format(details[0],
                                                        details[2],
                                                        mid_str,
                                                        details[4],
                                                        details[5])
            if line != right_str:
                continue
            print("{}: {}".format(details[4]))
            lines += 1
            if lines == 10:
                print("Total size: {}".format(int(details[5])))
                lines = 1
    except KeyboardInterrupt:
            print("Total size: {}".format(int(details[5])))

