# -*- coding: utf-8 -*-
"""
Created on Mon May 27 20:15:38 2019

@author: 
"""

from dota2_api import get_api_json
from is_destroy_mid_tower_induce_win import is_destroy_mid_tower_induce_win
from is_first_blood_induce_win import is_first_blood_induce_win
from get_match_id import get_match_id

match_id = get_match_id("https://api.opendota.com/api/explorer?sql=SELECT%20match_id%0AFROM%20match_patch%20WHERE"
                        "%20patch%20%3E%3D%20'7.1'%0AORDER%20BY%20RANDOM()%0ALIMIT%20200")
a = 0  
c = 0
for ids in match_id:
    match_info = get_api_json("https://api.opendota.com/api/matches/"+str(ids))
    #b = is_destroy_mid_tower_induce_win(match_info)
    b = is_first_blood_induce_win(match_info)
    if b == None:
        c += 1
    elif b:
        a += 1
    else:
        pass

print(a,c)