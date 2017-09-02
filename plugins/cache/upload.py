from __future__ import print_function

from ansible import constants as C

from ansible.plugins.cache.base import BaseCacheModule
from websocket import create_connection
import json
import traceback


class CacheModule(BaseCacheModule):

    def __init__(self, *args, **kwargs):
        self.create_connection()
        self.cache = {}

    def create_connection(self):
        try:
            self.ws = None
            self.ws = create_connection(C.CACHE_PLUGIN_CONNECTION)
        except BaseException:
            print (traceback.format_exc())

    def get(self, key):
        return self.cache[key]

    def set(self, key, value):
        self.cache[key] = value
        def send():
            if self.ws is None:
                print ("Fact upload disabled")
            else:
                self.ws.send(json.dumps(['Facts', dict(key=key,
                                                       value=value)]))
        try:
            send()
        except BaseException:
            try:
                self.create_connection()
                send()
            except BaseException:
                print (traceback.format_exc())

    def keys(self):
        pass

    def contains(self, key):
        pass

    def delete(self, key):
        pass

    def flush(self):
        pass

    def copy(self):
        pass
