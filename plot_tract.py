#!/usr/bin/env python3

#Script plots 2 groups of time series

import os
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

in_dir = '/media/mcuser/Partition1/ADRC/ADRC_dMRI_output/Brainstem_05-29-20'
in_file1 = in_dir + '/' + 'LC2TECL_FA_y_compGRP.txt'
in_file2 = in_dir + '/' + 'LC2TECR_FA_y_compGRP.txt'
out_file = in_dir + '/' + 'LC2TEC_FA_y.png'
title_str = 'LC2TEC FA y'
grp_labels = ['Left', 'Right']

data1 = pd.read_csv(in_file1, sep='\t')
data2 = pd.read_csv(in_file2, sep='\t')

# Create a seperate dataframe for holding the calculated values
plot_data1 = pd.DataFrame(columns = ['Corr', 'mean', 'sd', 'se'])
plot_data1['Corr'] = data1['Corr']
plot_data1['mean'] = data1.mean(axis=1)
plot_data1['sd'] = data1.std(axis=1)
plot_data1['se'] = data1.std(axis=1)/(data1.count(axis=1)**(1/2))

plot_data2 = pd.DataFrame(columns = ['Corr', 'mean', 'sd', 'se'])
plot_data2['Corr'] = data2['Corr']
plot_data2['mean'] = data2.mean(axis=1)
plot_data2['sd'] = data2.std(axis=1)
plot_data2['se'] = data2.std(axis=1)/(data2.count(axis=1)**(1/2))
print(plot_data2.head())

#Plot the average timeseries
grp1, = plt.plot(plot_data1['Corr'], plot_data1['mean'], )
#Plot error bars
plt.fill_between(plot_data1['Corr'],
                plot_data1['mean']-plot_data1['se'],
                plot_data1['mean']+plot_data1['se'],
                alpha=0.2, linewidth=0)

grp2, = plt.plot(plot_data2['Corr'], plot_data2['mean'])
plt.fill_between(plot_data2['Corr'],
                plot_data2['mean']-plot_data2['se'], 
                plot_data2['mean']+plot_data2['se'],
                alpha=0.2, linewidth=0)

plt.legend([grp1, grp2], grp_labels)
plt.xlabel('MNI Coordinates')
plt.title(title_str)
#plt.show()
plt.savefig(out_file)
