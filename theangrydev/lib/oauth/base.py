import os
import uuid
import time
import urllib.parse as urlparse

from threading import Lock
from urllib.parse import urlencode

class OAuthHandler:
    STATE_DURATION = max(3600, int(os.getenv('OAUTH_STATE_DURATION')))
    LATEST_EPOCH = time.monotonic()
    MUTEX = Lock()
    STATE = None

    def __init__(self, name, base_url, client_id, client_secret):
        self.name = name
        self.base_url = base_url
        self.client_id = client_id 
        self.client_secret = client_secret

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name} : {self.base_url}"
    
    @property
    def state(self):
        '''
        Set state to be used by all OAuth 2.0 clients
        '''
        caller_epoch = time.monotonic()
        if not self.__class__.STATE:
            self.__class__.STATE = str(uuid.uuid4())
        
        # Refresh if state is about to expire in less than 10 seconds
        # Refresh if state as already expired
        # Acquire mutex before refreshing
        # TODO: Emit state refresh to all active Websocket clients
        if ((self.__class__.STATE_DURATION + self.__class__.LATEST_EPOCH) - caller_epoch <= 10) \
            or \
           ((caller_epoch - self.__class__.LATEST_EPOCH) > self.__class__.STATE_DURATION):
            self.__class__.MUTEX.acquire()
            try:
                self.__class__.LATEST_EPOCH = time.monotonic()
                self.__class__.STATE = str(uuid.uuid4())
            finally:
                self.__class__.MUTEX.release()

        return self.__class__.STATE
       
    def get_oauth_url(self):
        params = {
        "client_id": self.client_id,
        "state": self.state,
        }

        url_parts = list(urlparse.urlparse(self.base_url))
        url_parts[4] = urlencode(params)

        oauth_url = urlparse.urlunparse(url_parts)

        return oauth_url   

    ###########################################
    #    TO BE IMPLEMENTED BY SUBCLASS        #
    ###########################################

    def get_user_data(self):
        pass

