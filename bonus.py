import pyautogui
import pyperclip  # Para acessar o texto da área de transferência
import time
import keyboard  # Para capturar a tecla ESC
import sys
import tkinter as tk
from threading import Thread
import os
import pygetwindow as gw
import re
from urllib.parse import urlparse, parse_qs, urlencode
import random

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução de {func.__name__}: {fim - inicio:.6f} segundos")
        return resultado
    return wrapper

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

def convert_whatsapp_link(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    if 'phone' in query_params:
        phone_number = query_params['phone'][0]
        text = query_params.get('text', [''])[0]  # Pega o texto, se existir
        
        # # Remove o código do país (55 para Brasil)
        # if phone_number.startswith("55") and len(phone_number) > 10:
        #     phone_number = phone_number[2:]  # Remove os dois primeiros dígitos
        
        # Recria a URL com o text
        encoded_text = urlencode({'text': text}) if text else ""
        if text == "":
            # para a execução do codigo inteiro
            os._exit(0)
        return f"https://wa.me/{phone_number}"
        # return f"https://wa.me/{phone_number}?{encoded_text}" if text else f"https://wa.me/{phone_number}"


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
        localizacao = pyautogui.locateOnScreen(imagem, confidence=0.7)
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
@medir_tempo
def executar_codigo():
    time.sleep(1)
    global executando
    # Executar a sequência enquanto o programa está ativo
    numero_de_vezes_que_vai_repetir = int(sys.argv[1])
    for i in range(numero_de_vezes_que_vai_repetir):
        if not executando:  # Interrompe a execução imediatamente
            break

        # detectar_imagem('./numero-invalido.png')
        # detectar_e_clicar('./numero-invalido.png', 18, ajuste_x=0, ajuste_y=0)
        print(f"Executando a sequência {i+1}/20...")

        detectar_e_clicar('./whats-puro.png', 1.5, ajuste_x=0, ajuste_y=0)
        detectar_e_clicar('./enviar-mens.jpg', 1.5, ajuste_x=0, ajuste_y=0)
        
        pyautogui.click(627, 326)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        mensagem = pyperclip.paste()
        time.sleep(0.2)
        detectar_e_clicar('./enviar-whats.jpg', 0.2, ajuste_x=0, ajuste_y=0)
        # return
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        texto_selecionado_url = pyperclip.paste()
        texto_modificado_url = convert_whatsapp_link(texto_selecionado_url)
        pyperclip.copy(texto_modificado_url)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)
        pyautogui.hotkey('enter')
        time.sleep(3)

        invalido = detectar_imagem('./numero-invalido.png')
        # time.sleep(6)

        if invalido:
            pressionar_comb_e_esperar(['ctrl', 'w'], 2)
            break
        else:
            # pressionar_comb_e_esperar(['ctrl', 'a'], 2)
            # pyautogui.hotkey('ctrl', 'c')
            # time.sleep(1)

            # texto_selecionado = pyperclip.paste()
            texto_modificado = substituir_texto(mensagem)

            # verifica se o numero é valido
            # Definição de variáveis para simular a detecção de imagens inválidas
            invalido2 = detectar_imagem('./numero-invalido.png')
            invalido3 = detectar_imagem('./invalido.jpg')

            # Verifica se pelo menos uma das imagens foi detectada
            if invalido2 or invalido3:
                print("Imagem inválida detectada!")
                executando = False
                os._exit(0)
                break

            pyperclip.copy(texto_modificado)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.2)

            pressionar_e_esperar('enter', 1)
            
            pyautogui.hotkey('ctrl', 'f')
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.write('gui')
            pyautogui.hotkey('tab')
            pyautogui.press('enter')
            time.sleep(0.2)
            pyautogui.hotkey('alt', 'tab')
            time.sleep(0.2)
            pyautogui.hotkey('ctrl', 'w')
            # pressionar_comb_e_esperar(['ctrl', 'w'], 1)
            clicar_e_esperar(616, 443, 6)
            clicar_e_esperar(616, 461, 4)

            sleep_time = round(random.uniform(1, 4), 1)
            time.sleep(sleep_time)

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
