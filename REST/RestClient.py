import requests

class RestClient():

    def GetJson(self, parameter, apikey, url="https://api.guildwars2.com/v2"):
        response = requests.get(self.url+self.parameter+self.apikey)
        return response.json()