import pandas as pd
import math as mt
import numpy as np
import matplotlib.pyplot as plt

def calc_dist(point1, point2):
    return mt.sqrt(mt.pow(point2[0]-point1[0], 2) + mt.pow(point2[1]-point1[1], 2))

def error_list(df_ref, df_gtr):
    tp_list_ref = [tuple(row) for index, row in df_ref.iterrows()]
    tp_list_gtr = [tuple(row) for index, row in df_gtr.iterrows()]
    err_list = []

    for pt1 in tp_list_ref:
        dst = np.inf
        for pt2 in tp_list_gtr:
            if (calc_dist(pt1, pt2) <= dst):
                dst = calc_dist(pt1, pt2)
        err_list.append(dst)
    
    return err_list

# DIRECTIORIES TO CSV FILES
traj_ref_dir = 'trajectory.csv'

# TODO ADD DIRECTORIES TO YOUR CSV FILES
pp_50_dir = ''
pp_75_dir = ''
pp_100_dir = ''

cem_50_dir = ''
cem_75_dir = ''
cem_100_dir = ''

# SET OF DATAFRAMES (ONLY x, y COLLUMNS REQUIRED)
df_ref = pd.read_csv(traj_ref_dir, sep='; ', engine='python')
df_ref = df_ref[['x_m', 'y_m']]

df_pp_50 = pd.read_csv(pp_50_dir, sep=',')
df_pp_75 = pd.read_csv(pp_75_dir, sep=',')
df_pp_100 = pd.read_csv(pp_100_dir, sep=',')

df_cem_50 = pd.read_csv(cem_50_dir, sep=',')
df_cem_75 = pd.read_csv(cem_75_dir, sep=',')
df_cem_100 = pd.read_csv(cem_100_dir, sep=',')

# LISTS OF ERRORS ON SET TRAJECTORY
err_pp_50 = error_list(df_ref=df_ref, df_gtr=df_pp_50)
err_pp_75 = error_list(df_ref=df_ref, df_gtr=df_pp_75)
err_pp_100 = error_list(df_ref=df_ref, df_gtr=df_pp_100)

err_cem_50 = error_list(df_ref=df_ref, df_gtr=df_cem_50)
err_cem_75 = error_list(df_ref=df_ref, df_gtr=df_cem_75)
err_cem_100 = error_list(df_ref=df_ref, df_gtr=df_cem_100)

# PLOTTING
figure, axis = plt.subplots(3, 1)
axis[0].plot(err_cem_50)
axis[0].plot(err_pp_50)
axis[0].set_title("Path error with 50% speed")
axis[0].grid(True)
axis[0].legend(['CEM', 'PP'], loc='upper left')
axis[0].set_xlim(0, 270)
axis[0].set_xlabel('Point on reference path')
axis[0].set_ylabel('Path error []')

axis[1].plot(err_cem_75)
axis[1].plot(err_pp_75)
axis[1].set_title("Path error with 75% speed")
axis[1].grid(True)
axis[1].legend(['CEM', 'PP'], loc='upper left')
axis[1].set_xlim(0, 270)
axis[1].set_xlabel('Point on reference path')
axis[1].set_ylabel('Path error []')

axis[2].plot(err_cem_100)
axis[2].plot(err_pp_100)
axis[2].set_title("Path error with 100% speed")
axis[2].grid(True)
axis[2].legend(['CEM', 'PP'], loc='upper left')
axis[2].set_xlim(0, 270)
axis[2].set_xlabel('Point on reference path')
axis[2].set_ylabel('Path error []')

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1)
plt.show()