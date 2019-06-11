# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 21:20:45 2019

@author: IEZhou
"""
from dota2_api import get_api_json


def get_match_id(url):
    match_id = []
    match_id_info = get_api_json(url)
    for matches in match_id_info['rows']:
        match_id.append(matches['match_id'])
    return match_id
