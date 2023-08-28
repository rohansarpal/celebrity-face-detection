# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 19:20:08 2023

@author: Rohan_Sarpal
"""




import splitfolders  # or import split_folders

input_folder = 'path of dataset'

# Split with a ratio.

splitfolders.ratio(input_folder, output="path of desired output", 
                   seed=42, ratio=(.7,.30), 
                 group_prefix=None) # default values


