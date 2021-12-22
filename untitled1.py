# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 13:29:02 2021

@author: Burhan
"""

import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('bmh')
df=pd.read_csv("fashion-mnist_test.csv")
#all receipt
x=df['label']
y=df['pixel12']


plt.xlabel("label", fontsize=10)
plt.ylabel("pixel", fontsize=10)
plt.bar(x,y)
