import keyboard  # Para detectar atalhos de teclado
import pyperclip  # Para acessar o conteúdo do clipboard
import pyautogui  # Para simular a digitação
import time
import os
import sys
import daemon

def digitar_clipboard():
    """Lê o conteúdo do clipboard e digita no local atual do cursor, um por um."""
    try:
        texto = pyperclip.paste()  # Obtém o texto do clipboard
        if texto:
            for caractere in texto:  # Itera sobre cada caractere no texto
                if caractere.isdigit():  # Se o caractere for um número
                    pyautogui.press(caractere)  # Pressiona a tecla do número
                    print(f"Digitando número: {caractere}")
                else:  # Se o caractere for uma letra ou símbolo
                    pyautogui.write(caractere, interval=0.1)  # Digita o caractere com intervalo
                    print(f"Digitando caractere: {caractere}")
                time.sleep(0.1)  # Intervalo entre cada caractere
        else:
            print("Clipboard está vazio.")
    except Exception as e:
        print(f"Erro ao acessar o clipboard: {e}")

# Função para rodar o programa como um daemon
def rodar_como_daemon():
    with daemon.DaemonContext():
        # Define o atalho Ctrl + Alt + V para executar a função
        keyboard.add_hotkey('ctrl+alt+v', digitar_clipboard)
        print("O programa está rodando em segundo plano. Pressione Ctrl + Alt + V para digitar o conteúdo do clipboard.")
        print("Pressione Ctrl + M para sair.")
        
        # Mantém o programa rodando até Ctrl + M ser pressionado
        keyboard.wait('ctrl+m')  # Sai quando Ctrl + M é pressionado

# Chama a função para rodar o programa como um daemon
rodar_como_daemon()
