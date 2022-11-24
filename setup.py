def setup(airfoil, reynolds_number, a_init, a_final, a_step):
    with open('input_file.in', 'w') as file:
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
        file.write('quit\n')
