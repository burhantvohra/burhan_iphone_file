# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 13:42:57 2021

@author: Burhan
"""

import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('bmh')
df=pd.read_csv("recipes_muffins_cupcakes.csv")
df
x=df['Flour']
y=df['Milk']
plt.xlabel("Flour", fontsize=18)
plt.ylabel("Milk", fontsize=12)
plt.scatter(x,y)