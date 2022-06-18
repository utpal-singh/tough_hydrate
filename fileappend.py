# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 18:20:58 2021

@author: utpal-singh
"""

import pandas as utpal
import os
import glob
from pathlib import Path
import numpy
destination = input("Enter destination from this folder: \n")
depth = float(input("Enter max depth in metres, avoid negative values: \n"))
output_filename = input("Enter output filename, dont include xlsx: \n")

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


mylist = []
length = 0

names = ["x", "y", "z",  "P",  "T",  "S_hyd",  "S_aqu",  "S_gas",  "S_icd",  "X_inh",  "k_rg",  "k_rw",  "k_adj_F",  "perm_abs",  "porosity",  "P_cap"]
daf = utpal.DataFrame(columns=names)
for item in files:
    df = utpal.read_csv(item, sep = "  | ", names = names, skiprows=2)
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
    

daf.to_excel(output_filename+ ".xlsx")
sorteddf = daf[daf['z']>=-1*depth]
sorteddf.to_excel(output_filename+str(-1*depth)+".xlsx")
