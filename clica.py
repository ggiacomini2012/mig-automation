import pyautogui
import time

def clicar_e_esperar(x, y, delay):
    pyautogui.click(x, y)
    time.sleep(delay)

def pressionar_e_esperar(tecla, delay):
    pyautogui.press(tecla)
    time.sleep(delay)

def pressionar_comb_e_esperar(teclas, delay):
    pyautogui.hotkey(*teclas)
    time.sleep(delay)

# Executar a sequência 5 vezes
for i in range(1):
    print(f"Executando a sequência {i+1}/5...")
    clicar_e_esperar(645, 687, 5)
    clicar_e_esperar(634, 332, 5)
    clicar_e_esperar(637, 394, 15)

    pressionar_comb_e_esperar(['ctrl', 'a'], 2)
    AQUI 


    # pressionar_e_esperar('enter', 10)
    # pressionar_comb_e_esperar(['ctrl', 'w'], 2)
    # clicar_e_esperar(616, 443, 18)
    # print(f"Sequência {i+1}/5 concluída.")
