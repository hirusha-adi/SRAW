from . import errors

import requests



class Animals:
    
    def __init__(self, link: bool = True, fact: bool = True, rjson: bool = False):
        self.link = link
        self.fact = fact
        self.rjson = rjson


    def dog(self):
        req = requests.get("https://some-random-api.ml/animal/dog")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        if self.link and self.fact:
            return (cont['image'], cont['fact'])
        
        if self.link:
            return cont['image']

        if self.fact:
            return cont['fact']
             

    def cat(self):
        req = requests.get("https://some-random-api.ml/animal/cat")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        if self.link and self.fact:
            return (cont['image'], cont['fact'])
        
        if self.link:
            return cont['image']
            
        if self.fact:
            return cont['fact']


    def panda(self):
        req = requests.get("https://some-random-api.ml/animal/panda")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont

        if self.link and self.fact:
            return (cont['image'], cont['fact'])
        
        if self.link:
            return cont['image']
            
        if self.fact:
            return cont['fact']


    def fox(self):
        req = requests.get("https://some-random-api.ml/animal/fox")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont

        if self.link and self.fact:
            return (cont['image'], cont['fact'])
        
        if self.link:
            return cont['image']
            
        if self.fact:
            return cont['fact']


    def red_panda(self):
        req = requests.get("https://some-random-api.ml/animal/red_panda")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI

        if self.rjson == True:
            return cont

        if self.link and self.fact:
            return (cont['image'], cont['fact'])
        
        if self.link:
            return cont['image']
            
        if self.fact:
            return cont['fact']


    def koala(self):
        req = requests.get("https://some-random-api.ml/animal/koala")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont

        if self.link and self.fact:
            return (cont['image'], cont['fact'])
        
        if self.link:
            return cont['image']
            
        if self.fact:
            return cont['fact']


    def bird(self):
        req = requests.get("https://some-random-api.ml/animal/birb")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        if self.link and self.fact:
            return (cont['image'], cont['fact'])
        
        if self.link:
            return cont['image']
            
        if self.fact:
            return cont['fact']


    def raccoon(self):
        req = requests.get("https://some-random-api.ml/animal/raccoon")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        if self.link and self.fact:
            return (cont['image'], cont['fact'])
        
        if self.link:
            return cont['image']
            
        if self.fact:
            return cont['fact']


    def kangaroo(self):
        req = requests.get("https://some-random-api.ml/animal/kangaroo")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        if self.link and self.fact:
            return (cont['image'], cont['fact'])
        
        if self.link:
            return cont['image']
            
        if self.fact:
            return cont['fact']









