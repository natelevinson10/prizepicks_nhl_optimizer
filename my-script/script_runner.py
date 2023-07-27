from NHL_data_scrape import *
from pp_data_scrape import *
from compute_output import *

#iterate through player prompts, pass into functions to return output data for each prompt 
t = 0
q1 = ["shots", "hits", "assists", "points", "goals", "blocked"]
q2 = ["Shots On Goal", "Hits", "Assists", "Points", "Goals", "Blocked Shots"]

#fetch prizepicks prompts and NHL.com data
players = get_players()
IDs = get_IDs()

while t < len(q1):

    #pass in retreived player data and current prompt into functions, move to next prompt
    stats = get_bets(players, q2[t])
    z_score_query_sorted(IDs , stats, q1[t])
    t+=1
