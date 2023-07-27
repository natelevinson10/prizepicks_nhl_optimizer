import requests, json
from path import *

def get_players():

    f = open(path)
    data = json.load(f)

    x = 0
    namelist = []
    idlist = []

    #iterate through prizepicks endpoint data, loop through player names and IDs, append name and player ID to respective array
    while (x < len(data["included"])):
        jsonData = data["included"][x]
        id = jsonData["id"]
        name = jsonData["attributes"]["name"]
        if(len(id) != 2 and len(id) != 1 and len(id) != 3):
            namelist.append(name)
            idlist.append(id)
        x+=1

    res = {}
    #convert into dict with player : ID to cross reference with NHL.com dict
    for key in namelist:
        for value in idlist:
            res[key] = {"PrizePicks ID": value}
            idlist.remove(value)
            break  
    return res

def get_bets(res, query):
    stats = {}
    query = query
    f = open(path)
    data = json.load(f)
    x = 0

    #iterate through prizepicks data and categorize player prompts, assign values to type of prompt, prompt line, and player paired to prompt
    while (x < len(data["data"])):
        jsonData = data["data"][x]
        line_score = jsonData["attributes"]["line_score"]
        stat_type = jsonData["attributes"]["stat_type"]
        player = jsonData["relationships"]["new_player"]["data"]["id"]
        result = [key for key, value in res.items() if str(player) in value.values()] 
        if(stat_type == query):
            stats[result[0]] = line_score
        x+=1
    return stats

