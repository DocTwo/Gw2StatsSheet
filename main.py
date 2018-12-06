import requests
from REST import RestClient

client = RestClient()
client.GetJson("account","?access_token=someapikey")