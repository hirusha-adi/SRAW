from . import errors

import requests
from urllib import parse



class Misc:

    def __init__(self, rjson: bool = False):
        self.rjson = rjson


    def lyrics(self, title: str, cancer = None, lyrics_only: bool = False):
        params_query = {}
        linka = "https://some-random-api.ml/lyrics"

        if bool(title) == True:
            params_query['title'] = title
        else:
            raise errors.NoTitleProvided
        
        if bool(cancer) == True:
            params_query['cancer'] = cancer

        query_string = parse.urlencode(params_query)

        req = requests.get(f"{linka}?{query_string}")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        if lyrics_only == True:
            return cont['lyrics']
        
        return (cont['title'], cont['author'], cont['lyrics'], cont['thumbnail']['genius'], cont['links']['genius'])




    







