from re import I
from typing import *

# Clase de controlador de paginación bajo demanda
class PC():
    MARCO = 0+1
    BIT_VI = 1+1
    BIT_MODIFICADO = 2+1
    CONTADOR = 3+1
    def __init__(self, marcos_libres: List, num_paginas: int) -> None:
        self.marcos_libres = marcos_libres

        self.cont = 0
        # Inicializar tabla de paginas
        self.tabla_paginas: List[List[int]] = []

        # Inicializar tabla de marcos
        for i in range(num_paginas):
            self.tabla_paginas.append([i, -1, 0, 0, 0])
        

    def buscar_marco(self, direccion: int) -> int:
        return self.tabla_paginas[direccion][self.MARCO]

    def is_in_ram(self, pagina: int) -> bool:
        return self.tabla_paginas[pagina][self.BIT_VI] == 1

    def is_modified(self, pagina: int) -> bool:
        return self.tabla_paginas[pagina][self.BIT_MODIFICADO] == 1

    # busca pagina a reemplazar por LRU
    def buscar_reemplazo(self)-> int:
        less_recently_used = 0
        flag = False
        for page in range(len(self.tabla_paginas)):
            if self.is_in_ram(page):
                if flag:
                    if self.tabla_paginas[page][self.CONTADOR] < self.tabla_paginas[less_recently_used][self.CONTADOR]:
                        less_recently_used = page
                else:
                    less_recently_used = page
                    flag = True
        
        return less_recently_used   

    def next(self, pagina: int, escritura: bool = False) -> Tuple[int, Tuple[bool, bool]]:
        swap_in = False
        swap_out = False

        self.cont += 1
        self.tabla_paginas[pagina][self.CONTADOR] = self.cont
        if escritura:
            self.tabla_paginas[pagina][self.BIT_MODIFICADO] = 1
        if not self.is_in_ram(pagina):
            swap_in = True
            if len(self.marcos_libres) > 0:
                marco = self.marcos_libres.pop()
                self.tabla_paginas[pagina][self.MARCO] = marco
            else:
                reemplazo = self.buscar_reemplazo()
                if self.is_modified(reemplazo):
                    swap_out = True
                    self.tabla_paginas[reemplazo][self.BIT_MODIFICADO] = 0
                self.tabla_paginas[reemplazo][self.BIT_VI] = 0
                self.tabla_paginas[pagina][self.MARCO] = self.tabla_paginas[reemplazo][self.MARCO]
            self.tabla_paginas[pagina][self.BIT_VI] = 1
        
        return self.buscar_marco(pagina), (swap_in, swap_out)

    def direccion_fisica(self, direccion: int, tamMarco: int) -> int:
        pagina = direccion // tamMarco
        desplazamiento = direccion % tamMarco
        if self.is_in_ram(pagina):
            return self.buscar_marco(pagina) * tamMarco + desplazamiento
        else:
            return None

    @staticmethod
    def get_pagina(direccion: int, tamMarco: int) -> int:
        return direccion // tamMarco