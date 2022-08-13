import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from celluloid import Camera
import pandas as pd

df = pd.read_csv('nyra_2019_complete.csv')

df_aqu_newyears = df[(df['track_id'] == 'AQU') & (df['race_date'] == "2019-01-01")]
df_small = df_aqu_newyears[(df_aqu_newyears['race_number'] == 9)].sort_values(by=['trakus_index']).reset_index(drop=True)



camera = Camera(plt.figure())
for i in range(1,len(df_small['trakus_index'].unique())+1):
    df_i = df_small[df_small['trakus_index'] == i]
    plt.scatter(df_i['latitude'], df_i['longitude'], s=50)
    print(i)
    for j in df_i.index:
        #print(j)
        plt.annotate(df_i['program_number'][j], (df_i['latitude'][j], df_i['longitude'][j]))
    camera.snap()
anim = camera.animate(blit=True)
anim.save('scatter_all_hoses.gif')