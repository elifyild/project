# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:41:18 2022

@author: Elif
"""
import numpy as np
import pandas as pd
from scipy.stats import norm, kurtosis
import scipy
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#data_functions
##IMPORT EXCEL FILE
# file_name='birlestirilmis_betonarme_yapilar_dd-report_details.xlsx'
file_name='betonarme_yapilar_full.xlsx'
df=pd.read_excel(file_name, sheet_name = 'Sheet1')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete empty column

##DONATI SINIFI ANALIZI 
df_donati=df['Donati Sinifi']
# selecting rows based on condition 
df_S220 = df[df['Donati Sinifi'] == 'Nervürsüz (S220)'] 
df_S420 = df[df['Donati Sinifi'] == 'Nervürlü (S420)'] 
df_Karma = df[df['Donati Sinifi'] == 'Karma (S220 ve S420)'] 

donati_value_count=df_donati.value_counts() 
donati_value_perc=df_donati.value_counts(normalize=True) 
donati_names=list(donati_value_count.index.values) #Get row-index values of Pandas DataFrame as list

fig = plt.figure(figsize = (7, 7))
 
# creating the bar plot
graph = plt.bar(donati_names, donati_value_count, color ='lightblue',width = 0.4)

#reference
# https://www.geeksforgeeks.org/display-percentage-above-bar-chart-in-matplotlib/
# We can use get_width() method and get_height() method that returns 
# the width and height of each bar respectively in the bar graph.

# get_xy() method can be used to get the x and y coordinates 
# at the bottom leftmost point of each bar.

i = 0
for p in graph:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    plt.text(x+width/2,
             y+height*1.01,
             str(round(donati_value_perc[i],3)*100)+'%',
             ha='center',
             weight='bold')
    i+=1
    
plt.xlabel("Donatı Sınıfı")
plt.ylabel("Bina Sayısı")
plt.title("Donatı Sınıfı Dağılımı - Bina Sayısı: %i" % (len(df_donati)))
plt.show()