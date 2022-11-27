import subprocess

def setup(airfoil, reynolds_number, a_init, a_final, a_step):
    with open('xfoil.in', 'w') as file:
        file.write(f'NACA {airfoil}\n')
        file.write('PANE\n')
        
        #operation commands for xfoil
        file.write('OPER\n')
        file.write(f'VISC {reynolds_number}\n')
        file.write('PACC\n')
        file.write('polar_file.txt\n\n')
        file.write('ITER 100\n')
        file.write(f'ASeq {a_init} {a_final} {a_step}\n')
    
        #close
        file.write("\n")
        file.write('quit\n')

def xfoil(airfoil, reynolds_number, a_init, a_final, a_step):
    setup(airfoil, reynolds_number, a_init, a_final, a_step)
    
    try:
        p = subprocess.run(f'xfoil.exe < xfoil.in > NACA{airfoil}.out', 
            shell=True, timeout=20)
    except subprocess.TimeoutExpired:
        raise subprocess.TimeoutExpired('xfoil.exe', 20)
    

def get_airfoil(max_camber, max_camber_pos, thickness):
    max_camber = str(max_camber)
    max_camber_pos = str(max_camber_pos)  
    return f'{max_camber[0]}{max_camber_pos[0]}{thickness:02d}'




