import math
import datetime
import requests
import urllib3
from bs4 import BeautifulSoup
from collections import OrderedDict
urllib3.disable_warnings()

from flask import Flask, render_template

# instantiate the app
app = Flask('app')

## Defaults
# set the current time
current_datetime = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')
# current gametracker url
URL = 'https://www.gametracker.com/server_info/108.61.124.73:27035/top_players/?sort=1&order=DESC&searchipp=50'



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
    neo = ['neo', 'neo ~', 'zxc', 'ñeø', 'zxc [DGL.mode]', 'ne0', '0_o', 'brzrkr']

    # secret
    secret = ['Secret105v', 'Secret105v #NoSound']

    # pom
    pom = ['Pom Pom M4n.', 'Drunken Monkey', 'Johnny Sins!', 'Johnny sins', 'Viper']

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
    constant_list = ['neo', 'Secret105v', 'Pom Pom M4n.', 'Xhosa', 'NoFea[r]wOw', 'r0B[i]n wOw~', 'LeThAl', 'Blitz', 
    'Sparky', 'Point Blank', 'Adheera', 'Roman', 'eXCALIBUr', 'Hector', 'alamaleste', '<<OptimusPrime>>', 
    'Glady', 'ZeR0_CoOL', 'BerLin', 'CSK', 'Ethan', 'Skull_Crusher']

    # clean up the list in a better way
    new_map = {}
    for player, efficacy in player_map.items():
        if player in constant_list:
            new_map[player] = efficacy

    # remove folks who are not joining
    # remove_list = ['Fluttershy', 'Tony', 'Hmmm', 'Master-User', 'Dinga', 'Leosa', 'Leaving in 10', 'HBD Adheera']
    # for item in remove_list:
    #     del updated_map[item]

    return new_map


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

    # update and clean the player map
    updated_map = clean_map(player_map)
    # sort it appropriatly
    sorted_map = OrderedDict(sorted(updated_map.items(), key=lambda x: x[1], reverse=True))

    # flask it
    with app.app_context():
        rendered = render_template('index.html', \
            title = "Player Stats", \
            player_map = enumerate(sorted_map.items()), \
            last_updated = current_datetime)
        # print it to stdout which will be piped later
        print(rendered)