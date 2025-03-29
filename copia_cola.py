import keyboard  # Para detectar atalhos de teclado
import pyperclip  # Para acessar o conteúdo do clipboard
import pyautogui  # Para simular a digitação
import time

def digitar_clipboard():
    """Lê o conteúdo do clipboard e digita no local atual do cursor, um por um."""
    time.sleep(0.3)
    try:
        texto = pyperclip.paste()  # Obtém o texto do clipboard
        if texto:
            for caractere in texto:  # Itera sobre cada caractere no texto
                if caractere.isdigit():  # Se o caractere for um número
                    pyautogui.press(caractere)  # Pressiona a tecla do número
                    print(f"Digitando número: {caractere}")
                else:  # Se o caractere for uma letra ou símbolo
                    pyautogui.press(caractere, interval=0.005)  # Digita o caractere com intervalo
                    print(f"Digitando caractere: {caractere}")
                time.sleep(0.005)  # Intervalo entre cada caractere
        else:
            print("Clipboard está vazio.")
    except Exception as e:
        print(f"Erro ao acessar o clipboard: {e}")

# Define o atalho Ctrl + Alt + V para executar a função
keyboard.add_hotkey('alt+v', digitar_clipboard)

print("O programa está rodando em segundo plano. Pressione Ctrl + Alt + V para digitar o conteúdo do clipboard.")
print("Pressione Ctrl + M para sair.")

# Mantém o programa rodando até Ctrl + M ser pressionado
keyboard.wait('ctrl+m')  # Sai quando Ctrl + M é pressionado
