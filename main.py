import subprocess
import numpy as np
import os
from setup import setup

polar_data = np.empty(7)

#remove old data output


#define parameters
chord_length = 450 #in mm
chord_height = 50  #in mm
velocity = 15 #m/s
reynold = int(velocity * chord_length / 1.5111E-5)
a_init, a_final, a_step = 0, 10, 1


for max_camber in np.arange(0, 4, 1): #0 to 9.5%
    for max_camber_pos in np.arange(0, 10, 2): #0 to 90%
        for thickness in np.arange(1, 40, 10): #1 to 40%
            #remove old input/intermediate output files
            try:
                os.remove('polar_file.txt')
                os.remove('input_file.in')
            except:
                pass
            
            #NACA code
            airfoil = f'{max_camber}{max_camber_pos}{thickness}'
            
            #prepares inputs to xfoil
            setup(airfoil, reynold, a_init, a_final, a_step)
            #runs xfoil based on inputs
            subprocess.call('xfoil.exe < input_file.in', shell=True)
            
            #appends data into array
            to_add = np.loadtxt('polar_file.txt', skiprows=12)
            """ rows = np.shape(to_add)[0]
            naca = np.full((rows, 1), airfoil)
            to_add = np.c_[to_add, naca] """
            polar_data = np.vstack((polar_data, to_add))
            
            os.system('cls')

#outputs results to csv
np.savetxt('output.csv', polar_data, fmt='%f', delimiter=',',  
    header='Alpha,CL,CD,CDp,CM,Top_Xtr,Bot_Xtr')
