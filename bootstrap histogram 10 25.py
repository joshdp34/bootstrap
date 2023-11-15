"""

@author: Joshua_Patrick
"""


import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import os

os.chdir("C:\\Users\\Joshua_Patrick\\Box\\2023 08 STA 2450")
dat = pd.read_csv("2017_Fuel_Economy_Data.csv")

dat = dat["Combined Mileage (mpg)"]
n = len(dat)
n_boot = 10_000                            
stat = "mean"

boot_stat = []
for i in range(n_boot):
    boot_sample = dat.sample(n, replace = True)
    
    if stat == "median":
        boot_stat.append(float(boot_sample.median()))
    elif stat == "mean":
        boot_stat.append(float(boot_sample.mean()))
    elif stat == "std dev":
        boot_stat.append(float(boot_sample.std()))
    else:
        raise TypeError("Wrong statistic name")
boot_df = pd.DataFrame({'x': boot_stat})

(
 ggplot(boot_df, aes(x = "x"))+
 geom_histogram()
 )

