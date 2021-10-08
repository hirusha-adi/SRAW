from . import errors

import requests



class Image:

    def __init__(self, rjson: bool = False, image: bool = False):
        self.rjson = rjson
        self.image = image


    def dog(self):
        req = requests.get("https://some-random-api.ml/img/dog")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        if self.image == True:
            req_img = requests.get(f"{cont['link']}").content
            return req_img
        
        return cont['link']


    def panda(self):
        req = requests.get("https://some-random-api.ml/img/panda")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        if self.image == True:
            req_img = requests.get(f"{cont['link']}").content
            return req_img
        
        return cont['link']
    

    def red_panda(self):
        req = requests.get("https://some-random-api.ml/img/red_panda")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        if self.image == True:
            req_img = requests.get(f"{cont['link']}").content
            return req_img
        
        return cont['link']
    

    def birb(self):
        req = requests.get("https://some-random-api.ml/img/birb")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        if self.image == True:
            req_img = requests.get(f"{cont['link']}").content
            return req_img
        
        return cont['link']
    

    def fox(self):
        req = requests.get("https://some-random-api.ml/img/fox")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        if self.image == True:
            req_img = requests.get(f"{cont['link']}").content
            return req_img
        
        return cont['link']
    

    def koala(self):
        req = requests.get("https://some-random-api.ml/img/koala")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        if self.image == True:
            req_img = requests.get(f"{cont['link']}").content
            return req_img
        
        return cont['link']

    







