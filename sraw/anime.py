from . import errors

import requests



class Anime:

    def __init__(self, rjson: bool = False, image: bool = False):
        self.rjson = rjson
        self.image = image


    def wink(self):
        req = requests.get("https://some-random-api.ml/animu/wink")

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
    

    def pat(self):
        req = requests.get("https://some-random-api.ml/animu/pat")

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


    def hug(self):
        req = requests.get("https://some-random-api.ml/animu/hug")

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



    







