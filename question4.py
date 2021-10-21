# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:08:55 2015

@author: philippos
"""

obligor = {
    "id": 1,
    "name": "Genericom",
    "incorporation date": '1915-05-07',
    "previous names": ["Genco", "General Corp", "Gen Brothers"],
    "statements": ''
}

portfolio = {
    "metadata": {
        "as of date": '2015-05-07',
    },
    "obligor1": {
        "id": 1,
        "name": "Genericom",
        "incorporation date": '1915-05-07',
    },
    "obligor2": {
        "id": 2,
        "name": "ExpoCo",
        "incorporation date": '1815-05-07',
    }
}

obligor1 = {
    "id": 1,
    "name": "Genericom",
    "incorporation date": '1915-05-07',
    "previous names": ["Genco", "General Corp", "Gen Brothers"],
    "statements": ''
}
obligor2 = {
    "id": 2,
    "name": "ExpoCo",
    "incorporation date": '1815-05-07',
    "previous names": [],
    "statements": 'Missing'
}

portfolio2 = [obligor1, obligor2]
# >> > portfolio2[1]['name']
# 'Genericom'
