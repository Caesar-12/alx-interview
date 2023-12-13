#!/usr/bin/python3
"""Script that reads from stdin and compute metrics"""

import sys
from datetime import datetime
import random

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
                status, size = int(details[7]), int(details[8])
                dat = "{} {}".format(details[2][1:], details[3][:-1])
                date_t = datetime.strptime(dat, '%Y-%m-%d %H:%M:%S.%f')
            except NameError:
                 continue

            right_str = '{} - [{}] "{}" {} {}'.format(ip,
                                                        dat,
                                                        mid_str,
                                                        status,
                                                        size)
            if line is right_str:
                continue
            print("{}: {}".format(status, random.randrange(1,5)))
            lines += 1
            if lines == 10:
                print("Total size: {}".format(int(details[5])))
                lines = 1
    except KeyboardInterrupt:
            print("Total size: {}".format(int(details[5])))

metric_compute()
