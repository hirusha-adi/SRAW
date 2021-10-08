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

    
    def base64(self, mode: str = "encode", query: str = None):
        params_query = {}
        linka = "https://some-random-api.ml/base64"

        if mode.lower().startswith('e'):
            params_query['encode'] = query
        
        if mode.lower().startswith('d'):
            params_query['decode'] = query

        query_string = parse.urlencode(params_query)

        req = requests.get(f"{linka}?{query_string}")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        if mode.lower().startswith('e'):
            return cont['base64']
        
        if mode.lower().startswith('d'):
            return cont['text']
    

    def joke(self):
        req = requests.get("https://some-random-api.ml/joke")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        if self.rjson == True:
            return cont
        
        return cont['joke']
        

    def pokemon(self, pokemon: str, dym = None, key = None):
        params_query = {}
        linka = "https://some-random-api.ml/pokedex"

        if bool(pokemon) == True:
            params_query['pokemon'] = pokemon
        else:
            raise errors.NoPokemonProvided
        
        if bool(dym) == True:
            params_query['dym'] = dym
        
        if bool(key) == True:
            params_query['dym'] = dym

        query_string = parse.urlencode(params_query)
        req = requests.get(f"{linka}?{query_string}")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        return cont
    

    def pokemon_iterable(self, pokemon: str, dym = None, key = None):
        """
        I tuly dont want anyone to use this
        """
        params_query = {}
        linka = "https://some-random-api.ml/pokedex"

        if bool(pokemon) == True:
            params_query['pokemon'] = pokemon
        else:
            raise errors.NoPokemonProvided
        
        if bool(dym) == True:
            params_query['dym'] = dym
        
        if bool(key) == True:
            params_query['dym'] = dym

        query_string = parse.urlencode(params_query)

        req = requests.get(f"{linka}?{query_string}")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI
        
        yield cont["name"]
        yield cont["id"]
        yield cont["type"]
        yield cont["species"]
        yield cont["abilities"]
        yield cont["height"]
        yield cont["weight"]
        yield cont["base_experience"]
        yield cont["gender"]
        yield cont["egg_groups"]
        yield cont["sprites"]
        yield cont["description"]
        yield cont["generation"]

        yield cont["stats"]['hp']
        yield cont["stats"]['attack']
        yield cont["stats"]['defense']
        yield cont["stats"]['sp_atk']
        yield cont["stats"]['speed']
        yield cont["stats"]['total']
        
        yield cont["family"]['evolutionStage']
        try:
            for i in cont["family"]['evolutionLine']:
                yield i
        except:
            yield cont["family"]['evolutionLine']


    def minecraft(self, username: str = None, uuid_only: bool = False, name_hirstory_only: bool = False):
        params_query = {}
        linka = "https://some-random-api.ml/mc"

        if bool(username) == True:
            params_query['username'] = username

        query_string = parse.urlencode(params_query)
        req = requests.get(f"{linka}?{query_string}")

        if 300 > req.status_code >= 200:
            cont = req.json()
        else:
            raise errors.BadResponseFromAPI

        if self.rjson == True:
            return cont
        
        if uuid_only == True:
            return cont["uuid"]
        
        if name_hirstory_only == True:
            return cont["name_history"]

        return (cont["username"], cont["uuid"], cont["name_history"])

    
