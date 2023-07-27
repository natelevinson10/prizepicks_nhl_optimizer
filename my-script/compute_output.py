import requests, json
import scipy.stats as st
import statistics
from decimal import Decimal, ROUND_UP

def z_score_query_sorted(IDs, players, query):
    query = query
    wks = 10
    out = []
    not_enough_data = []
    print(f"STAT LINE: {query.upper()}\n---------------------------------------------")
    
    #check if player is in IDs, if so view player's stats on NHL.com
    for player in players:
        if player in IDs.keys():
            playerID = IDs[str(player)]["ID"]
            url = f"https://statsapi.web.nhl.com/api/v1/people/{str(playerID)}/stats?stats=gameLog&expand=stats.team&season=20222023&site=en_nhl"

            payload={}
            headers = {
            'authority': 'api.nhle.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://www.nhl.com',
            'referer': 'https://www.nhl.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
            }

            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()

            i = 0
            total = 0
            arr = []

            #compute avg of player's specified stat line over X weeks as well as weekly data over last X weeks
            while (i < (int(wks))):
                if ((len(data["stats"][0]["splits"])) < wks):
                    i+=1
                    continue
                total += data["stats"][0]["splits"][i]["stat"][query]
                arr.append(data["stats"][0]["splits"][i]["stat"][query])
                i+=1
            avg = total/wks
            
            #get standard deviation and Z score using last X weeks array as data set, compute probability of prizepicks line with cumulitive normal distribution
            try:
                SD = statistics.stdev(arr)
                Z = (players[player] - avg) / SD
                p_values = 1 - st.norm.cdf(Z)

                out.append({"player": f"{player}", "stat": p_values, "avg": avg, "arr": arr, "pproj": players[player], "ID": IDs[str(player)]["ID"]})
            except statistics.StatisticsError:
                not_enough_data.append({"player": f"{player}", "pproj": players[player]})
    newlist = sorted(out, key=lambda d: d['stat'], reverse = True) 
    
    #for each player, print their outputted data and convert into a percentige rounded to the hundredths decimal place 
    j = 0
    while j < len(newlist):
        print(f"{newlist[j]['player']: <23}-> | {Decimal((newlist[j]['stat'])*100).quantize(Decimal('.01'))}% | 10 game avg: {newlist[j]['avg']:.2f} | proj: {str(newlist[j]['pproj']): <3} | {str(newlist[j]['arr'][:10])}")
        j+=1
    if any(not_enough_data):
        print(f"not enough games played: \n{not_enough_data}")
    print("---------------------------------------------\n")