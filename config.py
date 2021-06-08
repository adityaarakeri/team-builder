import datetime

class Config:
    # server details
    server_ip='108.61.124.73:27035'
    red_channel='https://discord.gg/QZBmNKd3ry'
    blue_channel='https://discord.gg/kAg8Du5wd4'
    fy_aim_maps=[
        '$3000$_b1',
        '32_aztecworld',
        'aim_headshot',
        'aim_map',
        'aim_ak-colt',
        'aim_deagle',
        'Aim_map_usp',
        'fy_snow',
        'fy_snow3',
        'fy_snow_dino',
        'fy_snow_dew',
        'fy_dustworld2010',
        'fy_dustworld2_x',
        'fy_gravemake',
        'fy_hotspot',
        'fy_icevalley',
        'fy_aztec_mini',
        'fy_aztecworld'

    ]
    awp_maps=[
        'awp_india',
        'awp_india2',
        'awp_inferno',
        'awp_fightyard',
        'awp_greatwalls',
        'awp_highrated',
        'awp_white',
        'awp_city2',
        'awp_bycaster_dust',
        'awp_concrete',
        'css_vietnam',
    ]
    twoxtwo_maps=[
        'de_dust2_2x2',
        'css_mirage2x2_go',
        'de_inferno2x2',
        'de_nuke2x2',
    ]
    old_comp_maps=[
        'de_dust2',
        'de_inferno',
        'de_nuke',
        'de_train',
        'de_mirage',
        'de_tuscan',
        'de_hell',
        'de_cbble',
        'de_forze',
        'de_aztec',
    ]
    new_comp_maps=[
        'css_dust2se_go',
        'csg_nuke',
        'css_mirage_go',
        'de_cache',
        'css_overpass',
        'css_train_go',
        'go_vertigo_classic',
        'css_cbble',
    ]
    gametrack_url = f'https://www.gametracker.com/server_info/{server_ip}/top_players/?sort=1&order=DESC&searchipp=50'

    # list of players who join regularly
    # the names have to be unique
    # if any player chanages their name often it should be noted
    constant_list = [
        'neo', 
        'Secret105v', 
        'Pom Pom M4n.', 
        'Xhosa', 
        'NoFea[r]wOw', 
        'r0B[i]n wOw~', 
        'LeThAl', 
        'Blitz', 
        'Sparky', 
        'Point Blank', 
        'Adheera', 
        'Roman', 
        'eXCALIBUr', 
        'Hector', 
        'alamaleste', 
        '<<OptimusPrime>>', 
        'Glady', 
        'ZeR0_CoOL', 
        'BerLin', 
        'CSK', 
        'Ethan', 
        'Skull_Crusher',
        'DEE',
        'MaxSteel'
    ]

    # anomalies that cause due to a player having different names
    neo_anom = [
        'neo', 
        'neo ~', 
        'zxc', 
        'ñeø', 
        'zxc [DGL.mode]', 
        'brzrkr',
        'klu'
    ]

    secret_anom = [
        'Secret105v', 
        'Secret105v #NoSound'
    ]

    pom_anom = [
        'Pom Pom M4n.',
        'Johnny Sins!', 
        'Johnny sins', 
        'Viper'
    ]

    # misc
    current_datetime = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')

    dropbox_link = 'https://www.dropbox.com/sh/vvih47eaqcpd1fd/AABxQn5Du3idxTuqYKll4-VSa?dl=0'