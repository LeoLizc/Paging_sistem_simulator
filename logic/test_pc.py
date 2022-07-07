from PC import PC
import numpy as np

secuencia: list = [21, 26, 25, 6, 5, 29, 4, 5, 17, 16, 24, 25, 4, 7, 21, 1, 14, 15, 21, 22]
escritura: list = [False, False, True, True, False, False, False, True, True, True, True, False, True, False, True, True, False, False, True, True]

direcciones = zip(secuencia, escritura)
tam_marco = 4
tam_proceso = max(secuencia)+1
num_paginas = tam_proceso // tam_marco + (tam_proceso % tam_marco > 0)
marcos_libres = [3, 5, 8]

# instanciando listas de salidas
out_swap_in = []
out_swap_out = []
out_num_pag = []
out_num_marc = []
out_dir_fis = []

pc: PC = PC(marcos_libres, num_paginas)

for direccion, escrito in direcciones:
    pagina = PC.get_pagina(direccion, tam_marco)
    marco, (swap_in, swap_out) = pc.next(pagina, escrito)
    
    out_swap_in.append(swap_in)
    out_swap_out.append(swap_out)
    out_num_pag.append(pagina)
    out_num_marc.append(marco)
    out_dir_fis.append(pc.direccion_fisica(direccion, tam_marco))

print('num_pag:',out_num_pag)
print('num_marc:', out_num_marc)
print('dir_fis:',out_dir_fis)
print('swap_in', out_swap_in)
print('swap_out', out_swap_out)
