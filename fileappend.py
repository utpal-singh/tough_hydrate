# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 18:20:58 2021

@author: utpal-singh
"""

import pandas as pd
import os
import glob
from pathlib import Path
import numpy
destination = input("Enter destination from this folder: \n")
depth = float(input("Enter max depth in metres, avoid negative values: \n"))
output_filename = input("Enter output filename, dont include xlsx: \n")

#requires pip install openpyxl

current_working_dir = os.getcwd()
destination_working_dir = os.path.join(current_working_dir, destination)
#files = glob.glob("./" + destination + "/*", recursive=True)
files = glob.glob(destination_working_dir + "/*", recursive=True)

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

print("******************alist end*****************************")

alist.sort(key=natural_keys)

#start_letter = "./" + destination + "/" + 'Plot_Data_Elem_'
start_letter = os.path.join(destination_working_dir, "Plot_Data_Elem_")

print("******alist sorted and started-letter************************")
# printing original list
print("****************************************************************************************")
# using list comprehension + startswith()
# Prefix Separation
final_list = [x for x in alist if x.startswith(start_letter)]


mylist = []
length = 0

print("******************loop begin**************************")
names = ["x", "y", "z",  "P",  "T",  "S_hyd",  "S_aqu",  "S_gas",  "S_icd",  "X_inh",  "k_rg",  "k_rw",  "k_adj_F",  "perm_abs",  "porosity",  "P_cap"]
daf = pd.DataFrame(columns=names)
for item in final_list:
    df = pd.read_csv(item, sep = "  | ", names = names, skiprows=2, nrows=1501)
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
    daf = daf.append(df)
    
print("******************loop end******************")
daf.to_csv(output_filename+destination+ ".csv")
sorteddf = daf[daf['z']>=-1*depth]
sorteddf.to_csv(output_filename+destination+str(-1*depth)+".csv")
