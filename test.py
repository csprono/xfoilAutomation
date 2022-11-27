import csv
import subprocess
import numpy as np
import os
from funcs import *

#csv setup
header=['NACA', 'Alpha', 'CL', 'CD', 'CDp', 'CM', 'Top_Xtr', 'Bot_Xtr']
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

#define parameters
chord_length = 450 #in mm
chord_height = 50  #in mm
velocity = 15 #m/s
reynold = int(velocity * (chord_length*1E-3) / 1.5111E-5)
a_init, a_final, a_step = 0, 10, 1

try:
    os.remove('polar_file.txt')
    os.remove('input_file.in')
except:
    pass

#run xfoil
airfoil = '2101'
try:
    xfoil(airfoil, reynold, a_init, a_final, a_step)
    #appends data into array
    try:
        to_add = np.loadtxt('polar_file.txt', skiprows=12)
        rows = np.shape(to_add)

        if to_add.size != 0:
            if len(rows) == 1:
                naca = np.full((1), airfoil)
                
            else:
                naca = np.full((rows[0], 1), airfoil)
                
            to_add = np.hstack((naca, to_add))        
    except:
        print('polar_file.txt is empty')    
except subprocess.TimeoutExpired as e:
    print(str(e))