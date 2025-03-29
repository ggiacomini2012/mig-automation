import pyautogui
import pyperclip  # Para acessar o texto da área de transferência
import time
import keyboard  # Para capturar a tecla ESC
import sys
import tkinter as tk
from threading import Thread
import os
import pygetwindow as gw 

# Variável para controlar o estado de execução
executando = True
def minimizar_terminal():
    try:
        janela = gw.getWindowsWithTitle("cmd")  # Título padrão do terminal no Windows
        if janela:
            janela[0].minimize()
            print("Terminal minimizado.")
        else:
            print("Não foi possível encontrar o terminal para minimizar.")
    except Exception as e:
        print(f"Erro ao tentar minimizar o terminal: {e}")

minimizar_terminal()

# Função para monitorar a tecla ESC
def monitorar_tecla_esc():
    global executando
    while executando:  # Verifica constantemente se a tecla ESC foi pressionada
        if keyboard.is_pressed('esc'):
            print("Tecla ESC pressionada. Encerrando execução.")
            executando = False
            os._exit(0)
            time.sleep(30)
            break
        time.sleep(0.1)  # Evita uso excessivo de CPU

# Função para criar a janela do anúncio
def criar_anuncio():
    root = tk.Tk()
    root.title("Status")
    root.geometry("200x100")
    root.configure(bg="black")

    # Configurações para manter a janela sempre no topo
    root.attributes("-topmost", True)
    root.overrideredirect(True)  # Remove a barra de título

    # Mensagem
    label = tk.Label(root, text="Código em execução \n Aperte Esc para sair", bg="black", fg="white", font=("Arial", 12, "bold"))
    label.pack(expand=True)

    # Mantém a janela aberta
    root.mainloop()


def clicar_e_esperar(x, y, delay):
    if not executando:
        return
    pyautogui.click(x, y)
    time.sleep(delay)

def pressionar_e_esperar(tecla, delay):
    if not executando:
        return
    pyautogui.press(tecla)
    time.sleep(delay)

def pressionar_comb_e_esperar(teclas, delay):
    if not executando:
        return
    pyautogui.hotkey(*teclas)
    time.sleep(delay)

def detectar_e_clicar(imagem, delay, ajuste_x=0, ajuste_y=0):
    if not executando:
        return False
    try:
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
    except pyautogui.ImageNotFoundException:
        print(f"Imagem '{imagem}' não encontrada na tela.")
        return False
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return False

def detectar_imagem(imagem):
    if not executando:
        return False
    try:
        localizacao = pyautogui.locateOnScreen(imagem, confidence=0.8)
        if localizacao:
            print(f"Imagem '{imagem}' encontrada.")
            return True
        else:
            print(f"Imagem '{imagem}' não encontrada na tela.")
            return False
    except pyautogui.ImageNotFoundException:
        print(f"Imagem '{imagem}' não encontrada na tela.")
        return False
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return False

def substituir_texto(texto):
    if "Bianca Lima Pantano" in texto:
        texto = texto.replace("Bianca Lima Pantano", "Bia")
    elif "da Made in Guarda." in texto:
        linhas = texto.splitlines()
        for i, linha in enumerate(linhas):
            if "da Made in Guarda." in linha:
                linhas[i] = "Gui da Made in Guarda."
        texto = "\n".join(linhas)
    return texto

# Função principal para execução do código
def executar_codigo():
    global executando
    # Executar a sequência enquanto o programa está ativo
    numero_de_vezes_que_vai_repetir = int(sys.argv[1])
    for i in range(numero_de_vezes_que_vai_repetir):
        if not executando:  # Interrompe a execução imediatamente
            break

        detectar_imagem('./numero-invalido.png')
        detectar_e_clicar('./numero-invalido.png', 18, ajuste_x=0, ajuste_y=0)
        print(f"Executando a sequência {i+1}/20...")
        # clicar_e_esperar(645, 687, 3)
        # clicar_e_esperar(634, 332, 5)
        # detectar_e_clicar('./whats-puro.png', 5, ajuste_x=0, ajuste_y=0)
        detectar_e_clicar('./whats-puro.png', 4, ajuste_x=0, ajuste_y=0)
        # detectar_e_clicar('./whats-puro.png', 1, ajuste_x=0, ajuste_y=25)
        pyautogui.click(580, 560)
        time.sleep(4)
        
        detectar_e_clicar('./whats-puro.png', 16, ajuste_x=0, ajuste_y=0)


        invalido = detectar_imagem('./numero-invalido.png')
        invalido2 = detectar_imagem('./numero-invalido2.png')
        # time.sleep(6)

        if invalido or invalido2:
            pressionar_comb_e_esperar(['ctrl', 'w'], 2)
            break
        else:
            # pressionar_comb_e_esperar(['ctrl', 'a'], 2)
            # time.sleep(1)
            # mensagem_sale = "SALE MIG | 50% OFF ~ a promo mais esperada do verão! 🎉\n\nAgora sem desculpa para não levar pra casa aquelas peças que você precisa há tempos 😉\n\nEstamos te esperando aqui na Loja Balneário Camboriú, corre que a ação é por tempo limitado. 🤩"


            # pyperclip.copy(mensagem_sale)
            # pyautogui.hotkey('ctrl', 'v')
            # time.sleep(1)
        # clicar_e_esperar(470, 720, 3)
        # clicar_e_esperar(541, 442, 3)
        # pyautogui.write("9af341a13ba90e7d7d21f1b91225d003") 

            # adiciona foto
            clicar_e_esperar(470, 720, 1)
            clicar_e_esperar(541, 397, 1)
            pyautogui.write("69a3426a53a4f80856738f6cc8a3a673")
            pressionar_e_esperar('enter', 5)
            pressionar_e_esperar('enter', 5)
            pyautogui.hotkey('ctrl', 'f')
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.write('gui')
            pyautogui.hotkey('tab')
            pyautogui.press('enter')            
            pressionar_comb_e_esperar(['ctrl', 'w'], 2)
            clicar_e_esperar(616, 443, 13)

        print(f"Sequência {i+1}/20 concluída.")

# Cria threads para o monitoramento e o anúncio
thread_anuncio = Thread(target=criar_anuncio, daemon=True)
thread_anuncio.start()

thread_monitoramento = Thread(target=monitorar_tecla_esc, daemon=True)
thread_monitoramento.start()

# Executa o código principal
executar_codigo()

# Finaliza o programa
executando = False
print("Encerrando o programa.")
