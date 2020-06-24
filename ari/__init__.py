#
# Copyright (c) 2013, Digium, Inc.
#

"""ARI client library
"""

from ari.client import Client
import swaggerpy.http_client
try :
        import urlparse
except :
        import urllib.parse as urlparse

def connect(base_url, username, password):
    """Helper method for easily connecting to ARI.

    :param base_url: Base URL for Asterisk HTTP server (http://localhost:8088/)
    :param username: ARI username
    :param password: ARI password.
    :return:
    """
    split = urlparse.urlsplit(base_url)
    http_client = swaggerpy.http_client.SynchronousHttpClient()
    http_client.set_basic_auth(split.hostname, username, password)

    client = Client(base_url, http_client)
    return Client(base_url, http_client)
