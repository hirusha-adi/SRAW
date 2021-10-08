from . import errors

import requests



class Fact:

    def __init__(self, rjson: bool = True):
        self.rjson = rjson


    def dog(self):
        req = requests.get("https://some-random-api.ml/facts/dog")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        return cont['fact']
    

    def cat(self):
        req = requests.get("https://some-random-api.ml/facts/cat")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        return cont['fact']
    

    def panda(self):
        req = requests.get("https://some-random-api.ml/facts/panda")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        return cont['fact']
    

    def fox(self):
        req = requests.get("https://some-random-api.ml/facts/fox")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        return cont['fact']
    

    def bird(self):
        req = requests.get("https://some-random-api.ml/facts/bird")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        return cont['fact']
    

    def koala(self):
        req = requests.get("https://some-random-api.ml/facts/koala")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        return cont['fact']






