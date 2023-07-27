# prizepicks_nhl_optimizer

Prizepicks NHL sports bet optimizer!

This tool is used to find the sports lines on prizepicks with the highest EV (expected value), and this is done by:
- scraping data from both prizepicks.com and NHL.com
- comparing player stats and projections to locate the lines with the best odds of hitting

Returns results for: ["Shots On Goal", "Hits", "Assists", "Points", "Goals", "Blocked Shots"]

To use this tool, navigate to https://api.prizepicks.com/projections?league_id=8&per_page=250&single_stat=true , the NHL best endpoint, and copy the whole response into the data.json file. Then, copy the path to that .json file and paste it into the path.py file. Finally, run script_runner.py in a terminal and wait for the results to compile: 


(ex. output from real data with statline Shots on Goal)
format : Name | Prob. of going OVER line | Prizepicks line | Array of last 10 games of statline from player
![image](https://github.com/natelevinson10/prizepicks_nhl_optimizer/assets/78764811/5fe8fadd-7ca8-470d-bad7-656b53702263)
