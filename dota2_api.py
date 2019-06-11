# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:53:45 2019

@author: IEZhou
"""
import requests


def get_api_json(url):
    try:
        r = requests.get(url, timeout=3)
        r_json = r.json()
        return r_json
    except:
        return get_api_json(url)


if __name__ == '__main__':
    pass
