#!/usr/bin/python3

"""
import keyboard

def on_key_event(e):
    print(f'Key {e.name} {e.event_type}')

keyboard.hook(on_key_event)

# Wait for events
keyboard.wait('esc')
"""

import sys

for line in sys.stdin:
    # Process each line here
    print("You entered:", line.strip())
