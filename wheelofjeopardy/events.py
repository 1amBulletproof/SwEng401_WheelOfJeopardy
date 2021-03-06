"""
From Design Document:
...abstraction to facilitate communication
between the GUI and the game state systems...

Classes subscribe to events, and other classes broadcast them.
When an event is broadcast, all the subscribers of that event
receive the message and any included arguments.
"""

import os

class Events(object):
    def __init__(self):
        self.subscriptions = {}

    def subscribe(self, channel, func):
        if channel in self.subscriptions:
            self.subscriptions[channel].append(func)
        else:
            self.subscriptions[channel] = [func]

    def broadcast(self, channel, *args):
        if self._log_events():
            print(channel)

        if channel in self.subscriptions:
            for func in self.subscriptions[channel]:
                func(*args)

    # private

    def _log_events(self):
        return os.getenv('LOG_EVENTS', 'false').lower() == 'true'
