import math
import datetime
import requests
import urllib3
from bs4 import BeautifulSoup
from collections import OrderedDict
urllib3.disable_warnings()

from flask import Flask, render_template

# local
from config import Config
from db import Player_DB

# instantiate the app
app = Flask('app')
# config
conf = Config()
# db
player_db = Player_DB()


## Defaults
# set the current time
current_datetime = conf.current_datetime
# current gametracker url
# URL = 'https://www.gametracker.com/server_info/108.61.124.73:27035/top_players/?sort=1&order=DESC&searchipp=50'
URL = conf.gametrack_url



# Average 
def average(scores):
    return float(math.fsum(scores)/len(scores))

# Efficacy 
def calculate_efficacy(score, time, score_per_min):
    """
    # whats Efficacy in this data ?
    # what we have? 
    # 1. Score -> totals score
    # 2. Time -> total time played on the server
    # 3. score/min -> total score made per minute

    # Neo's efficacy algorightm
    # (Efficacy Coeficient - Time played / Total Score) + score_per_min
    # Efficacy coeficient is set to 1 for now
    """
    efficacy = float(1 - float(time)/int(score)) + float(score_per_min)

    return efficacy

# resolve dupe player issue
def clean_map(player_map):
    """ 
    need to calculate efficacy of players who play with multiple names
    doing this for the last time !!!
    """

    # new map
    updated_map = {}

    # self
    neo = conf.neo_anom

    # secret
    secret = conf.secret_anom

    # pom
    pom = conf.pom_anom

    neo_scores = []
    secret_scores = []
    pom_scores = []

    for player, efficacy in player_map.items():
        if player in neo:
            neo_scores.append(efficacy)
        elif player in secret:
            secret_scores.append(efficacy)
        elif player in pom:
            pom_scores.append(efficacy)
        else:
            updated_map[player] = efficacy
    
    # # dumb but its all i got
    neo_efficacy = average(neo_scores)
    pom_efficacy = average(pom_scores)
    secret_efficacy = average(secret_scores)

    # update the map with averages
    # players to use these names going forward
    updated_map['neo'] = neo_efficacy
    updated_map['Pom Pom M4n.'] = pom_efficacy
    updated_map['Secret105v'] = secret_efficacy

    # exists list
    # better way to find with just existing names
    constant_list = conf.constant_list

    # clean up the list in a better way
    player_list = []
    # new_map = {}
    for player, efficacy in player_map.items():
        new_map = {}
        if player in constant_list:
            new_map['name'] = player
            new_map['efficacy'] = efficacy
            player_list.append(new_map)


    # return new_map
    return player_list


# Main
if __name__ == "__main__":

    # page request
    page = requests.get(URL, verify=False)

    # if gametracker isnt reachable
    if page.status_code != 200:
        print("cannot access the gametrackers.com!!!")
    # is reachable
    else:
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table', attrs={'class':'table_lst table_lst_spn'})
        table_tr = table.find_all('tr')
        
        # main player map
        player_map = {}

        # ignore the first and last item in the list
        for tr in table_tr[1:-1]:
            td = tr.find_all('td')
            rank = td[0].text.strip()
            name = td[1].text.strip()
            nbsp = td[2]
            score = td[3].text.strip()
            time = td[4].text.strip()
            score_per_min = td[5].text.strip()

            # map name to score, timeplayed and score/min
            player_map[name] = calculate_efficacy(score, time, score_per_min)

    # sort the map
    sorted_map = OrderedDict(sorted(player_map.items(), key=lambda x: x[1], reverse=True))

    # update and clean the player map
    # updated_map = clean_map(player_map)
    updated_player_list = clean_map(sorted_map)

    # final list
    final_player_list = []

    # new logic to calculate efficacy increase/decrese
    for item in updated_player_list:
        # add a player if he does not exist
        if player_db.search(item['name']) == []:
            player_db.insert(item)
        else:
            
            # new efficacy
            new_eff = item['efficacy']
            # get the old efficacy
            old_eff = player_db.search(item['name'])[0]['efficacy']
            # difference
            change_eff = new_eff - old_eff
            # setting defult to constant
            change_value = 'constant'
            # print(f"Player: {item['name']} Old eff: {old_eff}  New eff: {new_eff}")
            # print(f"Increase/Decrese in Efficacy: {(new_eff - old_eff)}")
            if change_eff > 0:
                change_value = 'improved'
            elif change_eff < 0:
                change_value = 'degraded'
            else:
                change_value = 'constant'

        # update the db with new eff
        player_db.update(item['name'], new_eff)

        # add the change_value to final
        item['change'] = change_value
        item['diff'] = change_eff
        final_player_list.append(item)

    # flask it
    with app.app_context():
        rendered = render_template('index.html', \
            title = "Player Stats", \
            final_list = enumerate(final_player_list), \
            last_updated = current_datetime, \
            server_ip = conf.server_ip, \
            red_channel = conf.red_channel, \
            blue_channel = conf.blue_channel, \
            fy_aim_maps = conf.fy_aim_maps, \
            awp_maps = conf.awp_maps, \
            twoxtwo_maps = conf.twoxtwo_maps, \
            old_comp_maps = conf.old_comp_maps, \
            new_comp_maps = conf.new_comp_maps, \
            drop_box_link = conf.dropbox_link, \
                )
        # print it to stdout which will be piped later
        print(rendered)
