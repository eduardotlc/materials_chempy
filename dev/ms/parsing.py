#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 11:00:50 2023

@author: eduardotc
"""

import pandas as pd


file = str(input("ascii mass spec file path: "))
fparser = pd.read_csv(file, sep='\t', lineterminator='\n')
fparser2 = fparser.loc[1]
print(fparser)
