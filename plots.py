# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 18:20:58 2021

@author: utpal-singh
"""
destination = input("Enter destination from this folder: \n")
depth = float(input("Enter max depth in metres, avoid negative values: \n"))

flags = input("Press f if you want last few lines to be plotted:    \n")

if flags == "f":
    num_files = int(input("Enter number of files from end to be plotted:  \n"))

names = ["x", "y", "z",  "P",  "T",  "S_hyd",  "S_aqu",  "S_gas",  "S_icd",  "X_inh",  "k_rg",  "k_rw",  "k_adj_F",  "perm_abs",  "porosity",  "P_cap"]
variable_plot = input('Please enter among the following: "x", "y", "z",  "P",  "T",  "S_hyd",  "S_aqu",  "S_gas",  "S_icd",  "X_inh",  "k_rg",  "k_rw",  "k_adj_F",  "perm_abs",  "porosity",  "P_cap":      ')

import pandas as pd
import os
import glob
from pathlib import Path
import numpy
import matplotlib.pyplot as plt

if not os.path.exists("./plots_" + destination + '_' + variable_plot):
    os.makedirs("./plots_" + destination + '_' + variable_plot)

files = glob.glob("./" + destination + "/*", recursive=True)
import re

def atof(text):
    try:
        retval = float(text)
    except ValueError:
        retval = text
    return retval

def natural_keys(text):
    return [ atof(c) for c in re.split(r'[+-]?([0-9]+(?:[.][0-9]*)?|[.][0-9]+)', text) ]

alist = files
alist.sort(key=natural_keys)

print("******************************Process Starting******************************************")

print("-------------------------Sorting the file names-----------------------------------------")
# initializing start Prefix
start_letter = "./" + destination + "/" + 'Plot_Data_Elem_'

# printing original list
print("****************************************************************************************")
# using list comprehension + startswith()
# Prefix Separation
final_list = [x for x in alist if x.startswith(start_letter)]

if flags == "f":
    final_list = final_list[(-1*num_files):]

print("-----------------------------Making final list------------------------------------------")

print("****************************************************************************************")

print("--------------------------Appending files-------------------------------------------------")
mylist = []
length = 0

#names = ["x", "y", "z",  "P",  "T",  "S_hyd",  "S_aqu",  "S_gas",  "S_icd",  "X_inh",  "k_rg",  "k_rw",  "k_adj_F",  "perm_abs",  "porosity",  "P_cap"]
#daf = pd.DataFrame(columns=names)
#for item in final_list:
#    df = pd.read_csv(item, sep = "  | ", names = names, skiprows=2, engine = "python")
#    length_df = len(df)
#    temp = df
#    temp = length
#    length_df = len(df)
#    #temp_iloc_0 = df.iloc[0]
#    #tem_iloc_n = df.iloc(length_df)
#    if length > temp:
#        leastlength = temp
#    df.loc[length_df] = df.loc[length_df-1]
#    df = df.shift(1)
#    df.iloc[0] = df.iloc[length_df]
#    df.drop(length_df, inplace=True)        
#    daf = daf.append(df)
#    #pd.concat([daf, df])

    

#daf.to_csv(output_filename+ ".csv")
#sorteddf = daf[daf['z']>=-1*depth]
#sorteddf.to_csv(output_filename+str(-1*depth)+".csv")

#print("---------------------Appending files done------------------------------------------------")

print("*************************************************************************************************")

#names = ["x", "y", "z",  "P",  "T",  "S_hyd",  "S_aqu",  "S_gas",  "S_icd",  "X_inh",  "k_rg",  "k_rw",  "k_adj_F",  "perm_abs",  "porosity",  "P_cap"]
#variable_plot = input('Please enter among the following: "x", "y", "z",  "P",  "T",  "S_hyd",  "S_aqu",  "S_gas",  "S_icd",  "X_inh",  "k_rg",  "k_rw",  "k_adj_F",  "perm_abs",  "porosity",  "P_cap":      ')
#print('"x", "y", "z",  "P",  "T",  "S_hyd",  "S_aqu",  "S_gas",  "S_icd",  "X_inh",  "k_rg",  "k_rw",  "k_adj_F",  "perm_abs",  "porosity",  "P_cap"')
#daf = pd.DataFrame(columns=names)
for item in final_list:
    if os.path.exists("plots_" + destination+'_'+variable_plot+"/"+item.strip().split("/")[2]+"_" + variable_plot + ".jpg"):
        continue
    df = pd.read_csv(item, sep = "  | ", names = names, skiprows=2, nrows=1500, engine = "python")
    length_df = len(df)
    temp = df
    temp = length
    length_df = len(df)
    #temp_iloc_0 = df.iloc[0]
    #tem_iloc_n = df.iloc(length_df)
    if length > temp:
        leastlength = temp
    df.loc[length_df] = df.loc[length_df-1]
    df = df.shift(1)
    df.iloc[0] = df.iloc[length_df]
    df.drop(length_df, inplace=True)
    sorteddf = df[df['z']>=-1*depth]
    plt.plot(sorteddf[variable_plot], sorteddf['z'])
    plt.title(variable_plot + " vs z " + str(item))
    plt.ylabel("z")
    plt.xlabel(variable_plot)
    plt.savefig("plots_" + destination+'_'+variable_plot+"/"+item.strip().split("/")[2]+"_" + variable_plot + ".jpg", dpi=300)
    plt.clf()
print("*****************************************************************************************************")
