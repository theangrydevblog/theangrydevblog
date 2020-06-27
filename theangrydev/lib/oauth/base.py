import os
import uuid
import time
import urllib.parse as urlparse

from urllib.parse import urlencode

class OAuthHandler:
    STATE = None

    def __init__(self, name, authorize_url, access_token_url, client_id, client_secret):
        self.name = name
        self.authorize_url = authorize_url
        self.access_token_url = access_token_url
        self.client_id = client_id 
        self.client_secret = client_secret

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name} : {self.authorize_url}"
    
    @property
    def state(self):
        '''
        Set state to be used by all OAuth 2.0 clients
        '''
        if not self.__class__.STATE:
            self.__class__.STATE = str(uuid.uuid4()).replace('-','_')

        return self.__class__.STATE
       
    def get_oauth_url(self):
        params = {
        "client_id": self.client_id,
        "state": self.state,
        }

        url_parts = list(urlparse.urlparse(self.authorize_url))
        url_parts[4] = urlencode(params)

        oauth_url = urlparse.urlunparse(url_parts)

        return oauth_url   

    ###########################################
    #    TO BE IMPLEMENTED BY SUBCLASS        #
    ###########################################

    def get_user_data(self):
        pass

