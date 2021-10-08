from . import errors

import requests
import os



class Animals:
    def __init__(self, link: bool = True, fact: bool = True):
        self.link = link
        self.fact = fact

    def dog(self):
        req = requests.get("https://some-random-api.ml/animal/dog")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.link:
            yield cont['image']

        if self.fact:
            yield cont['fact']


    def cat(self):
        req = requests.get("https://some-random-api.ml/animal/cat")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.link:
            yield cont['image']
            
        if self.fact:
            yield cont['fact']


    def panda(self):
        req = requests.get("https://some-random-api.ml/animal/panda")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.link:
            yield cont['image']
            
        if self.fact:
            yield cont['fact']


    def fox(self):
        req = requests.get("https://some-random-api.ml/animal/fox")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.link:
            yield cont['image']
            
        if self.fact:
            yield cont['fact']


    def red_panda(self):
        req = requests.get("https://some-random-api.ml/animal/red_panda")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.link:
            yield cont['image']
            
        if self.fact:
            yield cont['fact']


    def koala(self):
        pass


    def bird(self):
        pass


    def raccoon(self):
        pass


    def kangaroo(self):
        pass









