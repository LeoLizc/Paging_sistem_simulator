import math
import pygame, sys
import time
from logic.PC import PC
#from pyparsing import col
from components import Button, ColumnTable, RowTable
import tkinter, tkinter.filedialog as filedialog
import os

pygame.init()

ancho=850
alto=720
SCREEN = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

tam_marco=4
tam_so=32
tam_proc=30
num_marcos=10
marco_actual=0

marcos_libres = []
marcos_ocupados = [] 
lista_intrucciones = []

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    global tam_marco
    global tam_so
    global tam_proc
    global num_marcos

    pos_vertical=200
    espaciado=85
    distancia=30
    tam_letra_titulos=20

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(40).render("Parámetros", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(ancho/2, 120))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        #TAMAÑO DE MARCO
        tamMarco_TEXT = get_font(tam_letra_titulos).render(str("Tamaño de marco"), True, "White")
        tamMarco_RECT = tamMarco_TEXT.get_rect(center=(ancho/2, pos_vertical))
        SCREEN.blit(tamMarco_TEXT, tamMarco_RECT)
        tamMarco_NUM = get_font(40).render(str(tam_marco), True, "White")
        tamMarco_RECT = tamMarco_NUM.get_rect(center=(ancho/2, pos_vertical+distancia))
        SCREEN.blit(tamMarco_NUM, tamMarco_RECT)
        tamMarco_AUMENTAR = Button(image=None, pos=(ancho/2+90, pos_vertical+distancia), 
                            text_input="(+)", font=get_font(30), base_color="White", hovering_color="Green")
        tamMarco_AUMENTAR.changeColor(PLAY_MOUSE_POS)
        tamMarco_AUMENTAR.update(SCREEN)
        tamMarco_DISMINUIR = Button(image=None, pos=(ancho/2-90, pos_vertical+distancia), 
                            text_input="(-)", font=get_font(30), base_color="White", hovering_color="Green")
        tamMarco_DISMINUIR.changeColor(PLAY_MOUSE_POS)
        tamMarco_DISMINUIR.update(SCREEN)


        #TAMAÑO DE SO
        tamSO_TEXT = get_font(tam_letra_titulos).render(str("Tamaño del sistema operativo"), True, "White")
        tamSO_RECT = tamSO_TEXT.get_rect(center=(ancho/2, pos_vertical+espaciado))
        SCREEN.blit(tamSO_TEXT, tamSO_RECT)
        tamSO_NUM = get_font(40).render(str(tam_so), True, "White")
        tamSO_RECT = tamSO_NUM.get_rect(center=(ancho/2, pos_vertical+espaciado+distancia))
        SCREEN.blit(tamSO_NUM, tamSO_RECT)
        tamSO_AUMENTAR = Button(image=None, pos=(ancho/2+90, pos_vertical+espaciado+distancia), 
                            text_input="(+)", font=get_font(30), base_color="White", hovering_color="Green")
        tamSO_AUMENTAR.changeColor(PLAY_MOUSE_POS)
        tamSO_AUMENTAR.update(SCREEN)
        tamSO_DISMINUIR = Button(image=None, pos=(ancho/2-90, pos_vertical+espaciado+distancia), 
                            text_input="(-)", font=get_font(30), base_color="White", hovering_color="Green")
        tamSO_DISMINUIR.changeColor(PLAY_MOUSE_POS)
        tamSO_DISMINUIR.update(SCREEN)
        tam_so_aumentar_10 = Button(image=None, pos=(ancho/2+85*2, pos_vertical+espaciado+distancia), 
                            text_input="(++)", font=get_font(30), base_color="White", hovering_color="Green")
        tam_so_aumentar_10.changeColor(PLAY_MOUSE_POS)
        tam_so_aumentar_10.update(SCREEN)
        tam_so_disminuir_10 = Button(image=None, pos=(ancho/2-85*2, pos_vertical+espaciado+distancia), 
                            text_input="(--)", font=get_font(30), base_color="White", hovering_color="Green")
        tam_so_disminuir_10.changeColor(PLAY_MOUSE_POS)
        tam_so_disminuir_10.update(SCREEN)


        #TAMAÑO DE PROCESO
        tamProc_TEXT = get_font(tam_letra_titulos).render(str("Tamaño del proceso"), True, "White")
        tamProc_RECT = tamProc_TEXT.get_rect(center=(ancho/2, pos_vertical+espaciado*2))
        SCREEN.blit(tamProc_TEXT, tamProc_RECT)
        tamProc_NUM = get_font(40).render(str(tam_proc), True, "White")
        tamProc_RECT = tamProc_NUM.get_rect(center=(ancho/2, pos_vertical+espaciado*2+distancia))
        SCREEN.blit(tamProc_NUM, tamProc_RECT)
        tamProc_AUMENTAR = Button(image=None, pos=(ancho/2+90, pos_vertical+espaciado*2+distancia), 
                            text_input="(+)", font=get_font(30), base_color="White", hovering_color="Green")
        tamProc_AUMENTAR.changeColor(PLAY_MOUSE_POS)
        tamProc_AUMENTAR.update(SCREEN)
        tamProc_DISMINUIR = Button(image=None, pos=(ancho/2-90, pos_vertical+espaciado*2+distancia), 
                            text_input="(-)", font=get_font(30), base_color="White", hovering_color="Green")
        tamProc_DISMINUIR.changeColor(PLAY_MOUSE_POS)
        tamProc_DISMINUIR.update(SCREEN)
        tam_proc_aumentar_10 = Button(image=None, pos=(ancho/2+85*2, pos_vertical+espaciado*2+distancia), 
                            text_input="(++)", font=get_font(30), base_color="White", hovering_color="Green")
        tam_proc_aumentar_10.changeColor(PLAY_MOUSE_POS)
        tam_proc_aumentar_10.update(SCREEN)
        tam_proc_disminuir_10 = Button(image=None, pos=(ancho/2-85*2, pos_vertical+espaciado*2+distancia), 
                            text_input="(--)", font=get_font(30), base_color="White", hovering_color="Green")
        tam_proc_disminuir_10.changeColor(PLAY_MOUSE_POS)
        tam_proc_disminuir_10.update(SCREEN)

        #NÚMERO DE MARCOS
        numMarcos_TEXT = get_font(tam_letra_titulos).render(str("Número de marcos"), True, "White")
        numMarcos_RECT = numMarcos_TEXT.get_rect(center=(ancho/2, pos_vertical+espaciado*3))
        SCREEN.blit(numMarcos_TEXT, numMarcos_RECT)
        numMarcos_NUM = get_font(40).render(str(num_marcos), True, "White")
        numMarcos_RECT = numMarcos_NUM.get_rect(center=(ancho/2, pos_vertical+espaciado*3+distancia))
        SCREEN.blit(numMarcos_NUM, numMarcos_RECT)
        numMarcos_AUMENTAR = Button(image=None, pos=(ancho/2+90, pos_vertical+espaciado*3+distancia), 
                            text_input="(+)", font=get_font(30), base_color="White", hovering_color="Green")
        numMarcos_AUMENTAR.changeColor(PLAY_MOUSE_POS)
        numMarcos_AUMENTAR.update(SCREEN)
        numMarcos_DISMINUIR = Button(image=None, pos=(ancho/2-90, pos_vertical+espaciado*3+distancia), 
                            text_input="(-)", font=get_font(30), base_color="White", hovering_color="Green")
        numMarcos_DISMINUIR.changeColor(PLAY_MOUSE_POS)
        numMarcos_DISMINUIR.update(SCREEN)


    
        PLAY_BACK = Button(image=None, pos=(ancho/2, 600+20), 
                            text_input="Volver", font=get_font(40), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        PLAY_SIGUIENTE = Button(image=None, pos=(ancho/2, 550+20), 
                            text_input="Siguiente", font=get_font(40), base_color="White", hovering_color="Green")
        PLAY_SIGUIENTE.changeColor(PLAY_MOUSE_POS)
        PLAY_SIGUIENTE.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_SIGUIENTE.checkForInput(PLAY_MOUSE_POS):
                    menu_marcos_libres()
                #Marco
                if tamMarco_AUMENTAR.checkForInput(PLAY_MOUSE_POS):
                    tam_marco=tam_marco*2
                    
                if tamMarco_DISMINUIR.checkForInput(PLAY_MOUSE_POS):
                    if(tam_marco>2):
                        tam_marco=tam_marco//2
                        if tam_so/tam_marco+1 > num_marcos:
                            num_marcos = tam_so//tam_marco+1
                #SO
                if tamSO_AUMENTAR.checkForInput(PLAY_MOUSE_POS):
                    tam_so=tam_so+1
                    
                    if tam_so/tam_marco+1 > num_marcos:
                        num_marcos = num_marcos + 1 
                    
                if tamSO_DISMINUIR.checkForInput(PLAY_MOUSE_POS):
                    if tam_so != 1:
                        tam_so=tam_so-1
                if tam_so_aumentar_10.checkForInput(PLAY_MOUSE_POS):
                    tam_so=tam_so+10
                    
                    if tam_so/tam_marco+1 > num_marcos:
                        num_marcos = num_marcos + 1
                    
                if tam_so_disminuir_10.checkForInput(PLAY_MOUSE_POS):
                    if tam_so > 10:
                        tam_so=tam_so-10
                    elif tam_so > 1:
                        tam_so=1

                        
                    
                #Proceso
                if tamProc_AUMENTAR.checkForInput(PLAY_MOUSE_POS):
                    tam_proc=tam_proc+1
                    
                    if tam_so/tam_marco+1 > num_marcos:
                        num_marcos = tam_so/tam_marco+1

                if tamProc_DISMINUIR.checkForInput(PLAY_MOUSE_POS):
                    if tam_proc>1:
                        tam_proc=tam_proc-1
                        if tam_so/tam_marco+1 > num_marcos:
                            num_marcos = tam_so/tam_marco+1
                
                if tam_proc_aumentar_10.checkForInput(PLAY_MOUSE_POS):
                    tam_proc=tam_proc+10
                    
                    if tam_so/tam_marco+1 > num_marcos:
                        num_marcos = tam_so/tam_marco+1

                if tam_proc_disminuir_10.checkForInput(PLAY_MOUSE_POS):
                    if tam_proc>10:
                        tam_proc=tam_proc-10
                        if tam_so/tam_marco+1 > num_marcos:
                            num_marcos = tam_so/tam_marco+1
                    elif tam_proc > 1:
                        tam_proc=1
            
                    
                #numMarcos
                if numMarcos_AUMENTAR.checkForInput(PLAY_MOUSE_POS):
                    num_marcos=num_marcos+1
                    
                if numMarcos_DISMINUIR.checkForInput(PLAY_MOUSE_POS):
                    if num_marcos>2:
                        if tam_so/tam_marco+1 < num_marcos:
                            num_marcos=num_marcos-1
                        
        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def menu_marcos_libres():
    global tam_marco
    global tam_so
    global tam_proc
    global num_marcos
    global marco_actual
    
    #Se calcula cuántos marcos ocupará el SO
    marcos_so = math.ceil(tam_so/tam_marco)
    global marcos_libres
    global marcos_ocupados

    marcos_libres.sort()
    marcos_ocupados.sort()
            
    for i in range(num_marcos):
        if marcos_libres.count(i)==0 and marcos_ocupados.count(i)==0:
            if i<num_marcos-marcos_so:
                    marcos_libres.append(i)
            else:
                marcos_ocupados.append(i)
        
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(40).render("Seleccionar marcos libres", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(ancho/2, 120))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        #Número
        marco_NUM = get_font(70).render(str(marco_actual), True, "White")
        marco_RECT = marco_NUM.get_rect(center=(ancho/2, alto/2-50))
        SCREEN.blit(marco_NUM, marco_RECT)

        #Flecha der
        flechaDer = Button(image=None, pos=(ancho/2+50, alto/2-50), 
                            text_input="+", font=get_font(40), base_color="White", hovering_color="Green")
        flechaDer.changeColor(MOUSE_POS)
        flechaDer.update(SCREEN)
        #Flecha der
        flechaIzq = Button(image=None, pos=(ancho/2-60, alto/2-50), 
                            text_input="-", font=get_font(40), base_color="White", hovering_color="Green")
        flechaIzq.changeColor(MOUSE_POS)
        flechaIzq.update(SCREEN)

        #Botón de libre/ocupado
        if marcos_libres.count(marco_actual)>0:
            buttonAdd = Button(image=None, pos=(ancho/2, alto/2+10), 
                                text_input="Marcar como ocupado", font=get_font(29), base_color="White", hovering_color="Green")
        else:
            buttonAdd = Button(image=None, pos=(ancho/2, alto/2+10), 
                                text_input="Marcar como libre", font=get_font(29), base_color="White", hovering_color="Green")

        buttonAdd.changeColor(MOUSE_POS)
        buttonAdd.update(SCREEN)
        
        #Texto lista de ocupados
        marcosOcupados_TEXT = get_font(30).render("Ocupados:", True, "White")
        marcosOcupados_RECT = marcosOcupados_TEXT.get_rect().midleft = (80, 480)
        SCREEN.blit(marcosOcupados_TEXT, marcosOcupados_RECT)
        
        marcosOcupados_LIST = get_font(25).render(str(marcos_ocupados), True, "White")
        marcosOcupados_RECT = marcosOcupados_LIST.get_rect().midleft = (300, 484)
        SCREEN.blit(marcosOcupados_LIST, marcosOcupados_RECT)

        #Texto lista de libres
        marcosLibres_TEXT = get_font(30).render("Libres:", True, "White")
        marcosLibres_RECT = marcosLibres_TEXT.get_rect().midleft = (80, 442)
        SCREEN.blit(marcosLibres_TEXT, marcosLibres_RECT)

        marcosLibres_LIST = get_font(25).render(str(marcos_libres), True, "White")
        marcosLibres_RECT = marcosLibres_LIST.get_rect().midleft = (300, 445)
        SCREEN.blit(marcosLibres_LIST, marcosLibres_RECT)
        





        BACK = Button(image=None, pos=(ancho/2, 600+20), 
                            text_input="Volver", font=get_font(40), base_color="White", hovering_color="Green")
        BACK.changeColor(MOUSE_POS)
        BACK.update(SCREEN)

        SIGUIENTE = Button(image=None, pos=(ancho/2, 550+20), 
                            text_input="Siguiente", font=get_font(40), base_color="White", hovering_color="Green")
        SIGUIENTE.changeColor(MOUSE_POS)
        SIGUIENTE.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(MOUSE_POS):
                    main_menu()
                if SIGUIENTE.checkForInput(MOUSE_POS):
                    filename = prompt_file()
                    print(filename)
                    inst = []
                    if filename:
                        inst = read(filename)
                        simulator_screen(inst) 
                #Flecha derecha
                if flechaDer.checkForInput(MOUSE_POS):
                    if marco_actual<num_marcos-marcos_so-1:
                        marco_actual=marco_actual+1
                #Flecha izquierda
                if flechaIzq.checkForInput(MOUSE_POS):
                    if marco_actual>0:
                        marco_actual=marco_actual-1
                #Libre/Ocupado
                if buttonAdd.checkForInput(MOUSE_POS):
                    if marcos_libres.count(marco_actual)==0:
                        marcos_libres.append(marco_actual)
                        marcos_ocupados.remove(marco_actual)
                        marcos_libres.sort()
                        marcos_ocupados.sort()
                    else:
                        marcos_ocupados.append(marco_actual)
                        marcos_libres.remove(marco_actual)

        pygame.display.update()     

def prompt_file():
    """Create a Tk file dialog and cleanup when finished"""
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = filedialog.askopenfilename(parent=top, initialdir="./",)
    top.destroy()
    return file_name

def prompt_save_file():
    """Create a Tk file dialog and cleanup when finished"""
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = filedialog.asksaveasfilename(parent=top, initialdir="./",)
    top.destroy()
    if not file_name:
        return './bitácora.txt'
    return file_name

def read(file_name: str):
    with open(file_name, 'r') as file:
        # file.read(1)
        adresses = [int(x) for x in file.readline().strip().split(',')]
        types = file.readline().strip().split(',')
        if len(adresses) != len(types):
            return []

        return list(zip(adresses, types))

def main_menu():

    global tam_marco, tam_so, tam_proc, num_marcos,marco_actual, marcos_libres, marcos_ocupados

    tam_marco=16
    tam_so=32
    tam_proc=30
    num_marcos=10
    marco_actual=0
    marcos_libres = []
    marcos_ocupados = []

    posVertical=40

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("Frame", True, "#b68f40")
        MENU_TEXT2 = get_font(60).render("Simulator", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(ancho/2, 80))
        MENU_RECT2 = MENU_TEXT2.get_rect(center=(ancho/2, 150))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(ancho/2, 300+posVertical), 
                            text_input="Empezar", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(ancho/2, 450+posVertical), 
                            text_input="Salir", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(MENU_TEXT2, MENU_RECT2)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def simulator_screen(instrucciones: list):

    # init (start)
    file = open(prompt_save_file(), "w")
    SCREEN.fill("red")
    # print(marcos_libres)
    table = ColumnTable(pos = (5, ancho/2), numCol=len(instrucciones), headers=instrucciones, color="white")
    table.render(SCREEN)
    
    table.in_drag = False
    velocity: float = 1.0 #seconds per update
    num_paginas = int(tam_proc) // int(tam_marco) + int(int(tam_proc) % int(tam_marco) > 0)
    instruccion = 0
    
    pc = PC(marcos_libres=marcos_libres, num_paginas=num_paginas)

    page_table = RowTable(pos = (45.5, 60), numRow=num_paginas, color="white", render_size=(None, 35*5), headers=['Pag', 'Mar', 'V/I', 'Mod', 'Cont'], header_color=(32,3,53))
    page_table.rows[1:] = pc.tabla_paginas
    page_table.render(SCREEN)
    page_table.in_drag = False

    last_time = time.time()

    increment_velocity = Button(image=None, pos=(ancho-30, alto/2), 
                            text_input="+", font=get_font(40), base_color="White", hovering_color="Green")
    decrement_velocity = Button(image=None, pos=(30, alto/2), 
                            text_input="-", font=get_font(40), base_color="White", hovering_color="Green")

    fallos = 0
    reemplazos = -len(marcos_libres)

    ram = RowTable(pos = (720.5, 60), numCol= 2, color = "white", render_size=(None, 35*5), headers=['Marc', 'Pag'], numRow=len(marcos_libres), header_color=(57,4,94))

    ram.rows[1:] = [[x, '-'] for x in marcos_libres]
    ram.render(SCREEN)
    ram.in_drag = False
    
    disco = RowTable(pos = (446.5, 60), numCol=1, color = "white", render_size=(None, 35*5), headers=['Pag'], numRow=num_paginas, header_color=(57,4,94))

    disco.colSize = 90
    disco.size = (90, disco.rowSize*len(disco.rows))
    disco.rows[1:] = [[x] for x in range(num_paginas)]
    disco.in_drag = False

    swap_in = swap_out = False
    while True:
        # MOUSE_POS = pygame.mouse.get_pos()


        # OPTIONS_TEXT = get_font(40).render("This is the SIMULATOR screen.", True, "Black")
        # OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(ancho/2, 260))
        # SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # OPTIONS_BACK = Button(image=None, pos=(ancho/2, 460), 
        #                     text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        # OPTIONS_BACK.changeColor(MOUSE_POS)
        # OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if table.checkForInput(event.pos) and not table.in_drag:
                    last_mouse_pos = event.pos
                    table.in_drag = True
                elif increment_velocity.checkForInput(event.pos):
                    velocity -= 0.1
                elif decrement_velocity.checkForInput(event.pos):
                    velocity += 0.1
                elif page_table.checkForInput(event.pos) and not page_table.in_drag:
                    last_mouse_pos = event.pos
                    page_table.in_drag = True
                elif ram.checkForInput(event.pos) and not ram.in_drag:
                    last_mouse_pos = event.pos
                    ram.in_drag = True
                elif disco.checkForInput(event.pos) and not disco.in_drag:
                    last_mouse_pos = event.pos
                    disco.in_drag = True
                    # print('velocity: ', velocity)
            elif event.type == pygame.MOUSEBUTTONUP:
                table.in_drag = False
                page_table.in_drag = False
                ram.in_drag = False
                disco.in_drag = False
            elif event.type == pygame.MOUSEMOTION:
                increment_velocity.changeColor(pygame.mouse.get_pos())
                decrement_velocity.changeColor(pygame.mouse.get_pos())
                if table.in_drag:
                    table.drag((event.pos[0]-last_mouse_pos[0], 0) ,(ancho, alto))
                    last_mouse_pos = event.pos
                elif page_table.in_drag:
                    # print('f')
                    page_table.drag((0, event.pos[1]-last_mouse_pos[1]))
                    
                    # page_table.absolute_pos = (page_table.absolute_pos[0]+ (event.pos[0]-last_mouse_pos[0]), page_table.absolute_pos[1] + event.pos[1]-last_mouse_pos[1])
                    # page_table.x, page_table.y = (page_table.x+ (event.pos[0]-last_mouse_pos[0]), page_table.y + event.pos[1]-last_mouse_pos[1])

                    # print(page_table.absolute_pos)

                    last_mouse_pos = event.pos
                elif ram.in_drag:
                    ram.drag((0, event.pos[1]-last_mouse_pos[1]))

                    # ram.absolute_pos = (ram.absolute_pos[0]+ (event.pos[0]-last_mouse_pos[0]), ram.absolute_pos[1] + event.pos[1]-last_mouse_pos[1])
                    # ram.x, ram.y = (ram.x+ (event.pos[0]-last_mouse_pos[0]), ram.y + event.pos[1]-last_mouse_pos[1])

                    # print(ram.absolute_pos)

                    last_mouse_pos = event.pos
                elif disco.in_drag:
                    disco.drag((0, event.pos[1]-last_mouse_pos[1]))

                    # disco.absolute_pos = (disco.absolute_pos[0]+ (event.pos[0]-last_mouse_pos[0]), disco.absolute_pos[1] + event.pos[1]-last_mouse_pos[1])
                    # disco.x, disco.y = (disco.x+ (event.pos[0]-last_mouse_pos[0]), disco.y + event.pos[1]-last_mouse_pos[1])

                    # print(disco.absolute_pos)

                    last_mouse_pos = event.pos
                # print('drag')
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if OPTIONS_BACK.checkForInput(MOUSE_POS):
            #         main_menu()

        # UPDATES
        
        #file.write("Primera línea" + os.linesep)
        current_time = time.time()
        if current_time - last_time >= velocity:
            # print(current_time)
            if instruccion < len(instrucciones):
                pagina = PC.get_pagina(instrucciones[instruccion][0], int(tam_marco))
                marco, (swap_in, swap_out) = pc.next(pagina, True if instrucciones[instruccion][1]=='E' else False)
                table.set_columna(instruccion, [pagina, marco, pc.direccion_fisica(instrucciones[instruccion][0], int(tam_marco)) ,'X' if swap_in else '', 'X' if swap_out else ''])

                if swap_in:
                    fallos += 1
                    for i in range(len(ram.rows)):
                        if ram.rows[i][0] == marco:
                            ram.rows[i][1] = str(pagina)
                            break
                    reemplazos += 1
                
                file.write("En el milisegundo " + str(instruccion + 1) + " la dirección lógica " + str(instrucciones[instruccion][0]) + " ingresó en la página " + str(pagina) + ", marco #" + str(marco) + ". Además, su dirección física correspondiente es " + str(pc.direccion_fisica(instrucciones[instruccion][0], int(tam_marco))) + ((" y hubo swap in" + (" y swap out " if swap_out else '') ) if swap_in else '') + '\n')

                instruccion += 1
            last_time = current_time

        # RENDERS
        SCREEN.blit(BG, (0, 0))
        table.render(SCREEN)
        page_table.render(SCREEN)
        increment_velocity.update(SCREEN)
        decrement_velocity.update(SCREEN)
        ram.render(SCREEN)
        disco.render(SCREEN)

        # dibujar nombres de tablas
        OPTIONS_TEXT = get_font(20).render("Tabla de páginas", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(159, 45))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_TEXT = get_font(20).render("Disco", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(492, 45))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_TEXT = get_font(20).render("Ram", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(765, 45))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # escribir fallos y reemplazos
        OPTIONS_TEXT = get_font(20).render("Fallos: " + str(fallos), True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(159 -48, 300))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_TEXT = get_font(20).render("Reemplazos: " + str(max(0,reemplazos)), True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(492 -48, 300))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Se escribe si hubo swap in o swap out
        if swap_in:
            if swap_out:
                OPTIONS_TEXT = get_font(45).render("SWAP IN and SWAP OUT", True, "white")
                OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(ancho/2, alto/2))
                SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

                OPTIONS_TEXT = pygame.font.SysFont('arial', 60).render("<<  >>", True, "white")
                OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(627, 60+175/2))
                SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
            else:
                OPTIONS_TEXT = get_font(45).render("SWAP IN", True, "white")
                OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(ancho/2, alto/2))
                SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

                OPTIONS_TEXT = pygame.font.SysFont('arial', 60).render(">>", True, "white")
                OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(630, 60+175/2))
                SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        pygame.display.update()

#instruction_screen()
main_menu()
#menuMarcosLibres(16,32,16,8)