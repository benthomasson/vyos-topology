

from ansible.plugins.cache.base import BaseCacheModule
from websocket import create_connection
import json
import traceback


class CacheModule(BaseCacheModule):

    def __init__(self, *args, **kwargs):
        self.create_connection()

    def create_connection(self):
        try:
            self.ws = None
            self.ws = create_connection("ws://127.0.0.1:8013/network_ui/ansible?topology_id=143")
        except BaseException:
            print (traceback.format_exc())

    def get(self, key):
        pass

    def set(self, key, value):

        def send():
            if self.ws is None:
                print ("Fact upload disabled")
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
