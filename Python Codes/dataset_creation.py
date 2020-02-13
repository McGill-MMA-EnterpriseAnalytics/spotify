#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:49:44 2020

@author: luismiguel
"""

import pandas as pd

data = pd.read_csv('/Users/luismiguel/Downloads/US_Accidents_Dec19.csv')

df = data.sample(n=500000, random_state = 5)
list_topics = [3,4,5,6,7,8,9,10,11,13,14,15,16,17,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]
df = df.iloc[:,list_topics]

df.to_csv('/Users/luismiguel/Desktop/McGill MMA/Enterprise Analytics/accidents.csv')

df_prueba = pd.read_csv('/Users/luismiguel/Desktop/McGill MMA/Enterprise Analytics/accidents.csv')