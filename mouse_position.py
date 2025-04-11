# -*- coding: utf-8 -*-

import time
from pynput.mouse import Controller

def mostrar_posicao_mouse():
    mouse = Controller()
    
    while True:
        # Captura a posição do mouse
        posicao = mouse.position
        
        # Exibe a posição no terminal
        print(f"pyautogui.click{posicao}")
        
        # Atraso de 500ms
        time.sleep(0.5)

if __name__ == "__main__":
    mostrar_posicao_mouse()
