import pandas as pd
import matplotlib.pyplot as plt

# DIRECTIORIES TO CSV FILES
traj_ref_dir = 'trajectory.csv'

# TODO ADD DIRECTORIES TO YOUR CSV FILES
pp_50_dir = ''
pp_75_dir = ''
pp_100_dir = ''

cem_50_dir = ''
cem_75_dir = ''
cem_100_dir = ''

# SET OF DATAFRAMES
df_ref = pd.read_csv(traj_ref_dir, sep='; ', engine='python')

df_pp_50 = pd.read_csv(pp_50_dir, sep=',')
df_pp_75 = pd.read_csv(pp_75_dir, sep=',')
df_pp_100 = pd.read_csv(pp_100_dir, sep=',')

df_cem_50 = pd.read_csv(cem_50_dir, sep=',')
df_cem_75 = pd.read_csv(cem_75_dir, sep=',')
df_cem_100 = pd.read_csv(cem_100_dir, sep=',')

# PLOTTING
figure, axis = plt.subplots(1, 3)
axis[0].plot(df_ref['x_m'], df_ref['y_m'], ls='-', color='green')
axis[0].plot(df_cem_50['x'], df_cem_50['y'], ls='--')
axis[0].plot(df_pp_50['x'], df_pp_50['y'], ls='--')
axis[0].set_title("Path of vehicle (50% speed)")
axis[0].grid(True)
axis[0].legend(['Refence path', 'CEM', 'PP'], loc='upper left')
axis[0].set_xlabel('x')
axis[0].set_ylabel('y')

axis[1].plot(df_ref['x_m'], df_ref['y_m'], ls='-', color='green')
axis[1].plot(df_cem_75['x'], df_cem_75['y'], ls='--')
axis[1].plot(df_pp_75['x'], df_pp_75['y'], ls='--')
axis[1].set_title("Path of vehicle (75% speed)")
axis[1].grid(True)
axis[1].legend(['Refence path', 'CEM', 'PP'], loc='upper left')
axis[1].set_xlabel('x')
axis[1].set_ylabel('y')

axis[2].plot(df_ref['x_m'], df_ref['y_m'], ls='-', color='green')
axis[2].plot(df_cem_100['x'], df_cem_100['y'], ls='--')
axis[2].plot(df_pp_100['x'], df_pp_100['y'], ls='--')
axis[2].set_title("Path of vehicle (100% speed)")
axis[2].grid(True)
axis[2].legend(['Refence path', 'CEM', 'PP'], loc='upper left')
axis[2].set_xlabel('x')
axis[2].set_ylabel('y')

plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1)
plt.show()