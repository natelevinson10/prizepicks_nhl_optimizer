import requests, json

def get_IDs():

    #z = pg count, PIDs dict of player name : ID
    z = 0
    PIDs = {}

    #make req to first z(10) pages of NHL.com /stats endpoint
    while z < 10:
        url = f"https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goals%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22assists%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22playerId%22,%22direction%22:%22ASC%22%7D%5D&start={z*100}&limit={(z+1)*100}&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20222023%20and%20seasonId%3E=20222023"

        payload={}
        headers = {
        'authority': 'api.nhle.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://www.nhl.com',
        'referer': 'https://www.nhl.com/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        
        #convert response to json, iterate through obj and add each player and ID pair to IDs dict
        data = response.json()
        i = 0
        while i < len(data["data"]):
            name = data["data"][i]["skaterFullName"]
            value = data["data"][i]["playerId"]
            PIDs[name] = {"ID": value}
            i+=1
        z+=1
    return PIDs