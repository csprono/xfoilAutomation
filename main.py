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


for max_camber in np.arange(0, 5, 1): #0 to 9.5%
    for max_camber_pos in np.arange(0, 50, 10): #0 to 90%
        for thickness in np.arange(1, 40, 10): #1 to 40%
            #remove old input/intermediate output files
            try:
                os.remove('polar_file.txt')
                os.remove('xfoil.in')
            except:
                pass
            
            #run xfoil
            airfoil = get_airfoil(max_camber, max_camber_pos, thickness)
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

                    #writes xfoil output to csv
                    with open('output.csv', 'a') as f:
                        #writer = csv.writer(f)
                        #writer.writerows(to_add)
                        np.savetxt(f, to_add, fmt = '%s', delimiter=',')
                except:
                    print('polar_file.txt is empty')    
                    continue
            except subprocess.TimeoutExpired as e:
                print(str(e))        
                continue