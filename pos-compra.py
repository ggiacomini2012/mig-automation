import pyautogui
import time
from pytesseract import image_to_string
from PIL import Image
import keyboard
import re
import pygetwindow as gw  # Biblioteca para manipular janelas
import pyperclip  # Para acessar o texto da área de transferência
import sys
import tkinter as tk
from threading import Thread
import threading
import subprocess
import os
import random


# import spacy

# Carregar o modelo de língua portuguesa
# nlp = spacy.load("pt_core_news_sm")

# ------
# Variável global para controlar quando interromper
stop_execution = False
# Variável para controle do loop
executando = True

def substituir_texto_com_item(texto, item):
    mensagens_bia = [
        f"Ola!\nBia da Made...\nTudo bem??? 😊\nCurtiu {item}?\nAbraços! ✨",
        f"Oi Bia da made in guarda falando! 👋\nQue legal que comprou {item}!\nEspero que tenha gostado! 🤩\nAbraços!",
        f"Bia da made in guarda falando! 🎉\nQue bom que escolheu {item}!\nGostou? 🌟\nUm abraço!",
        f"Ola Bia da made in guarda falando! 💫\nMuito obrigada por comprar {item}!\nEsperamos que tenha gostado! 🎁\nAbraços!",
        f"Oi! 👋\nBia da Made...\nQue legal que curtiu {item}! 🎯\nUm abraco! ✨",
        f"Bia da made in guarda falando! 🤩\nMuito obrigada por escolher {item}!\nGostou? 🌟\nabraços!",
        f"Ola! 😊\nBia da Made...\nQue bom que gostou de {item}! 💫\nUm abraco! ✨",
        f"Oi Bia da made in guarda falando! 🌟\nQue legal que comprou {item}!\nEsperamos que tenha gostado! 🎁\nabraços!",
        f"Bia da made in guarda falando! 💫\nMuito obrigada por escolher {item}!\nGostou? 🌟\nUm abraco!",
        f"Ola Bia da made in guarda falando! 👋\nQue bom que curtiu {item}! 🎯\nEsperamos que tenha gostado! 🎁\nabraços! ✨"
    ]

    mensagens_gui = [
        f"Ola, tudo certinho?\nGui da MIG! 😃✨\nQueria saber, gostou d{item}?\nTudo de bom!!!\nAbracao... 🤩",
        f"Oi Gui aqui! 👋\nQue legal que comprou {item}!\nEspero que tenha gostado! 🤩\nTudo de bom!",
        f"Gui aqui! 🎉\nQue bom que escolheu {item}!\nGostou? 🌟\nUm abraco!",
        f"Ola Gui aqui! 💫\nMuito obrigado por comprar {item}!\nEsperamos que tenha gostado! 🎁\nTudo de bom!",
        f"Oi! 👋\nGui da Made aqui...\nQue legal que curtiu {item}! 🎯\nUm abraco! ✨",
        f"Gui aqui! 🤩\nMuito obrigado por escolher {item}!\nGostou? 🌟\nTudo de bom!",
        f"Ola! 😊\nGui da MIG...\nQue bom que gostou de {item}! 💫\nUm abraco! ✨",
        f"Oi Gui aqui! 🌟\nQue legal que comprou {item}!\nEsperamos que tenha gostado! 🎁\nTudo de bom!",
        f"Gui aqui! 💫\nMuito obrigado por escolher {item}!\nGostou? 🌟\nUm abraco!",
        f"Ola Gui aqui! 👋\nQue bom que curtiu {item}! 🎯\nEsperamos que tenha gostado! 🎁\nTudo de bom! ✨"
    ]

    if any(nome in texto for nome in ["Bianca Lima Pantano", "Bianca", "Lima", "Pantano"]):
        texto = random.choice(mensagens_bia)
    elif "da Made in Guarda." in texto:
        texto = random.choice(mensagens_gui)
    return texto

# Marca o início do código
inicio_execucao = time.time()


def monitorar_tecla_esc():
    global executando
    if threading.current_thread().name != "ESC Monitor":  
        return  # Garante que apenas a thread nomeada "ESC Monitor" executará esse código

    while executando:
        if keyboard.is_pressed('esc'):  # Verifica se a tecla ESC foi pressionada
            print("Tecla ESC pressionada. Encerrando execução.")
            executando = False
            os._exit(0)
            time.sleep(30)
            break
        time.sleep(0.1)  # Pequena pausa para evitar alto uso da CPU

# Criar e iniciar a única thread para monitorar a tecla ESC
thread_esc = threading.Thread(target=monitorar_tecla_esc, daemon=True, name="ESC Monitor")
thread_esc.start()

# Função para criar a janela do anúncio
def criar_anuncio():
    root = tk.Tk()
    root.title("Status")
    root.geometry("700x100")
    root.configure(bg="black")

    # Configurações para manter a janela sempre no topo
    root.attributes("-topmost", True)
    root.overrideredirect(True)  # Remove a barra de título

    # Mensagem
    label = tk.Label(root, text="Código em execução \n Aperte Esc repetidas vezes para sair", bg="black", fg="white", font=("Arial", 12, "bold"))
    label.pack(expand=True)

    # Mantém a janela aberta
    root.mainloop()


def criar_anuncio_final():
    root = tk.Tk()
    root.title("Status")
    root.geometry("700x100")
    root.configure(bg="black")

    # Configurações para manter a janela sempre no topo
    root.attributes("-topmost", True)
    root.overrideredirect(True)  # Remove a barra de título

    # Mensagem
    label = tk.Label(root, text="Código parando a execução \n Em alguns instantes o código encerrará", bg="red", fg="white", font=("Arial", 12, "bold"))
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
    pyautogui.hotkey(tecla)

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

def search_item(word):
    # Percorre a lista e retorna a palavra que contém o termo de busca
    for item in unique_items_with_article:
        if word.lower() in item.lower():
            return item
    return None  # Retorna None caso não encontre o item

def detectar_imagem(imagem):
    if not executando:
        return False
    try:
        localizacao = pyautogui.locateOnScreen(imagem, confidence=0.7)
        if localizacao:
            print(f"Imagem '{imagem}' encontrada.")
            # return True
            sys.exit("Execução interrompida: imagem encontrada.")
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


# Função para minimizar o terminal
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

unique_items = [
    "biquini",
    "blusa",
    "boardshort",
    "bolsa",
    "boné",
    "calça",
    "camisa",
    "caneca",
    "canga",
    "chapéu",
    "chinelo",
    "colete",
    "cooler",
    "cropped",
    "guarda-sol",
    "jaqueta",
    "kimono",
    "macacão",
    "maiô",
    "meia",
    "mochila",
    "pack",
    "regata",
    "saia",
    "sandália",
    "shoulder",
    "short",
    "t-shirt",
    "top",
    "vestido"
]

unique_items_with_article = [
    "o biquini",
    "a blusa",
    "o boardshort",
    "a bolsa",
    "o boné",
    "a calça",
    "a camisa",
    "a caneca",
    "a canga",
    "o chapéu",
    "o chinelo",
    "o colete",
    "o cooler",
    "o cropped",
    "o guarda-sol",
    "a jaqueta",
    "o kimono",
    "o macacão",
    "o maiô",
    "a meia",
    "a mochila",
    "o pack",
    "a regata",
    "a saia",
    "a sandália",
    "o shoulder",
    "o short",
    "a t-shirt",
    "o top",
    "o vestido"
]

# Função para esperar um tempo
def wait(ms):
    time.sleep(ms / 1000)

def pegar_primeira_palavra(frase):
    # Divide a frase em palavras com base nos espaços
    palavras = frase.split()
    # Retorna a primeira palavra, se existir
    return palavras[0] if palavras else None

# Função para corrigir o texto extraído
def corrigir_texto(texto):
    # Correções manuais específicas (substituições conhecidas)
    substituicoes = {
        "minimaza": "minimiza",
        "comsuno": "consumo",
        "ampliaa": "amplia",
        "comprass": "compras",
        "ultimass": "últimas",
    }

    # Substituir palavras conhecidas
    for palavra_errada, palavra_correta in substituicoes.items():
        texto = re.sub(rf'\b{palavra_errada}\b', palavra_correta, texto, flags=re.IGNORECASE)

    # Correções adicionais (pontuações ou letras extras)
    texto = re.sub(r"\s{2,}", " ", texto)  # Remove espaços duplos
    texto = texto.strip()  # Remove espaços extras nas extremidades

    return texto


# Função para minimizar o terminal
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

def find_first_item(text):
    # Transforma o texto em letras minúsculas para evitar problemas de comparação
    text = text.lower()
    # Percorre os itens na ordem e retorna o primeiro encontrado no texto
    for item in unique_items:
        if item in text:
            return search_item(item)
    return "as peças"

def pressionar_comb_e_esperar(teclas, delay):
    if not executando:
        return
    pyautogui.hotkey(*teclas)
    time.sleep(delay)


def scroll_to_exact_position():
    # Garante que a página vá para o topo primeiro
    pyautogui.scroll(10000)  # Rola bastante para cima

    time.sleep(1)  # Pequena pausa para evitar falhas

    # Agora, rola para a posição exata (número negativo para rolar para baixo)
    target_position = 400  # Ajuste conforme necessário
    pyautogui.scroll(-target_position)

minimizar_terminal()

# Função principal para execução do código
def executar_codigo():
    global executando
    numero_de_vezes_que_vai_repetir = int(sys.argv[1])
    for i in range(numero_de_vezes_que_vai_repetir):
        if not executando:  # Interrompe a execução imediatamente
            break
        invalido = detectar_imagem('./numero-url-invalido.png')


        if invalido:
            pressionar_comb_e_esperar(['ctrl', 'w'], 2)
            break
        else:
            print('tudo ok para começar')
        

        detectar_imagem('./numero-invalido.png')

        # Função principal
        if __name__ == "__main__":
            from threading import Thread

            # Minimiza o terminal antes de começar
            minimizar_terminal()
            wait(1000)

            # Inicia a thread para monitorar a combinação de teclas Shift + ESC
            thread_monitoramento = Thread(target=monitorar_tecla_esc, daemon=True)
            thread_monitoramento.start()

            try:
                # # Primeiro clique: Minimiza os dados de consumo
                # # pyautogui.click(1055, 456)
                # detectar_e_clicar('./dados-de-consumo.png', 1, ajuste_x=0, ajuste_y=0)
                # wait(2000)
                # print("Minimizou os dados de consumo")

                # # Segundo clique: Amplia as últimas compras
                # # pyautogui.click(1052, 558)
                # detectar_e_clicar('./ultimas-compras.png', 1, ajuste_x=0, ajuste_y=0)
                # wait(2000)
                # print("Ampliou as últimas compras")

                # # Terceiro clique: Seleciona a última compra
                # # pyautogui.click(1061, 602)
                # detectar_e_clicar('./ultimas-compras.png', 1, ajuste_x=0, ajuste_y=30)
                # wait(2000)
                # print("Selecionou a última compra")


                # move o mouse
                pyautogui.moveTo(634, 349)
                wait(500)

                pyautogui.scroll(-2000)

                pyautogui.click(1088, 526)
                wait(500)
                pyautogui.click(1085, 583)
                wait(500)
                # scroll_to_exact_position()
                pyautogui.scroll(-200)
                wait(500)

                # Da zoom na página
                def pressionar_ctrl_mais(parametro):
                    pyautogui.hotkey("ctrl", parametro)
                    print(f"Ctrl e {parametro}")

                pressionar_ctrl_mais("+")
                wait(300)
                pressionar_ctrl_mais("+")
                wait(300)
                # pressionar_ctrl_mais("+")
                # wait(200)
                # pressionar_ctrl_mais("+")
                # wait(200)

                # Scrolla um pouco para baixo

                # Tira print da área especificada
                left, top, right, bottom = 38, 346, 799, 629
                screenshot = pyautogui.screenshot(region=(left, top, right - left, bottom - top))
                screenshot.save("screenshot.png")
                print("Print tirado e salvo como 'screenshot.png'")

                # Extrai o texto da imagem
                texto_extraido = image_to_string(Image.open("screenshot.png"), lang="por")
                print("Texto extraído da imagem:")
                print(texto_extraido)

                # Corrige o texto extraído
                texto_corrigido = corrigir_texto(texto_extraido)
                print("Texto corrigido:")
                print(texto_corrigido)
                # print("Uma palavra só:")
                # print(pegar_primeira_palavra(texto_corrigido))
                print("Item encontrado:")
                print(find_first_item(texto_corrigido))
                item_comprado = find_first_item(texto_corrigido)

                # move o mouse
                pyautogui.moveTo(634, 349)
                wait(200)


                pressionar_ctrl_mais("-")
                wait(300)
                pressionar_ctrl_mais("-")
                wait(300)
                # pressionar_ctrl_mais("-")
                wait(4000)
                # pressionar_ctrl_mais("-")
                # wait(200)

                # pyautogui.click(657, 685)
                detectar_e_clicar('./whats-puro.png', 1, ajuste_x=0, ajuste_y=0)
                wait(2000)
                print("whats 1")

                # pyautogui.click(639, 501)
                detectar_e_clicar('./whats-puro.png', 1, ajuste_x=0, ajuste_y=0)
                wait(2000)
                print("whats 2")

                # pyautogui.click(622, 391)
                detectar_e_clicar('./whats-puro.png', 1, ajuste_x=0, ajuste_y=0)
                wait(10000)
                print("whats 3")

                # pyautogui
                pressionar_comb_e_esperar(['ctrl', 'a'], 2)
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(2)

                texto_selecionado = pyperclip.paste()
                print("texto_selecionado, item_comprado:")
                print(texto_selecionado, item_comprado)
                texto_final = substituir_texto_com_item(texto_selecionado, item_comprado)
                pyperclip.copy(texto_final)
                print("texto_final:")
                print(texto_final)
                pyautogui.hotkey('ctrl', 'v')

                wait(2000)
                pressionar_e_esperar('enter', 3)
                pressionar_comb_e_esperar(['ctrl', 'w'], 2)
                clicar_e_esperar(616, 443, 10)
                sleep_time = round(random.uniform(1, 4), 1)
                time.sleep(sleep_time)
                
                


            except Exception as e:
                print(f"Ocorreu um erro: {e}")

            finally:
                print("Encerrando o script.")        



        print(f"Sequência {i+1}/{numero_de_vezes_que_vai_repetir} concluída.")

# Cria threads para o monitoramento e o anúncio
thread_anuncio = Thread(target=criar_anuncio, daemon=True)
thread_anuncio.start()

thread_monitoramento = Thread(target=monitorar_tecla_esc, daemon=True)
thread_monitoramento.start()

# Executa o código principal
executar_codigo()

# Marca o término do código
fim_execucao = time.time()

# Calcula a duração
duracao_total = fim_execucao - inicio_execucao
horas = int(duracao_total // 3600)
minutos = int((duracao_total % 3600) // 60)
segundos = int(duracao_total % 60)

# Exibe o tempo de execução no formato desejado
print(f"Tempo total de execução: {horas:02}h{minutos:02}m{segundos:02}s")

# Finaliza o programa
print("Encerrando o programa.")

executando = False
