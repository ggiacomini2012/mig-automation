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

def detectar_e_clicar(imagem, delay, ajuste_x=0, ajuste_y=0):
    localizacao = pyautogui.locateOnScreen(imagem, confidence=0.8)
    if localizacao:
        centro = pyautogui.center(localizacao)
        print(centro)
        ajustado_x = centro.x + ajuste_x
        ajustado_y = centro.y + ajuste_y
        print(ajustado_x, ajustado_y)
        pyautogui.click(ajustado_x, ajustado_y)
        time.sleep(delay)
    else:
        print(f"Imagem '{imagem}' não encontrada na tela.")

# Executar a sequência várias vezes
for i in range(1):
    print(f"Executando a sequência {i+1}/20...")
    
    inicio = time.time()  # Marca o início da iteração
    
    clicar_e_esperar(645, 687, 5)
    detectar_e_clicar('./whats.png', 5, ajuste_x=0, ajuste_y=15)  # Substitua 'imagem1.png' pelo caminho da sua imagem
    clicar_e_esperar(637, 394, 17)

    clicar_e_esperar(478, 724, 3)

    clicar_e_esperar(530, 432, 5)
    clicar_e_esperar(276, 232, 3)
    pressionar_e_esperar('enter', 8)
    pressionar_e_esperar('enter', 13)

    pressionar_comb_e_esperar(['ctrl', 'w'], 2)
    clicar_e_esperar(616, 443, 18)
    
    fim = time.time()  # Marca o fim da iteração
    duracao = fim - inicio  # Calcula o tempo decorrido
    
    print(f"Sequência {i+1}/20 concluída em {duracao:.2f} segundos.")

