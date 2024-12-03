# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""

import requests

def fetch_metadata(url):
    """
    Returns the "data" dictionary of OpenGraph metadata found in HTML of given url
    """
    final_url = "https://opengraph.lewagon.com/"
    params = {'url' : url}
    response = requests.get(final_url, params)
    if response.status_code != 200:
        return {}
    return response.json()
