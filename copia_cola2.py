import pyperclip
import pyautogui
import time

def digitar_clipboard():
    """Obtém o conteúdo do clipboard e digita no local atual do cursor."""
    time.sleep(0.3)  # Pequeno atraso para evitar conflitos
    try:
        texto = pyperclip.paste()  # Obtém o conteúdo do clipboard
        if texto:
            # pyautogui.hotkey("alt", "tab")  # Alterna rapidamente entre janelas
            time.sleep(0.1)  # Pequeno delay para evitar falhas
            pyautogui.write(texto, interval=0.01)  # Digita normalmente
        else:
            print("Clipboard está vazio.")
    except Exception as e:
        print(f"Erro ao acessar o clipboard: {e}")

if __name__ == "__main__":
    digitar_clipboard()
