import pyautogui
import pyperclip  # Para acessar o texto da área de transferência
import time
import keyboard  # Para capturar a tecla ESC

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

# Executar a sequência com verificação da tecla ESC
for i in range(20):
    if keyboard.is_pressed('esc'):  # Verifica se a tecla ESC foi pressionada
        print("Tecla ESC pressionada. Encerrando execução.")
        break

    detectar_imagem('./numero-invalido.png')
    detectar_e_clicar('./numero-invalido.png', 18, ajuste_x=0, ajuste_y=0)
    print(f"Executando a sequência {i+1}/20...")
    clicar_e_esperar(645, 687, 5)
    clicar_e_esperar(634, 332, 5)
    clicar_e_esperar(637, 394, 19)

    invalido = detectar_imagem('./numero-invalido.png')
    time.sleep(4)

    if invalido:
        pressionar_comb_e_esperar(['ctrl', 'w'], 2)
        break
    else:
        pressionar_comb_e_esperar(['ctrl', 'a'], 2)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)

        texto_selecionado = pyperclip.paste()
        texto_modificado = substituir_texto(texto_selecionado)

        pyperclip.copy(texto_modificado)
        pyautogui.hotkey('ctrl', 'v')

        pressionar_e_esperar('enter', 10)
        pressionar_comb_e_esperar(['ctrl', 'w'], 2)
        clicar_e_esperar(616, 443, 18)

    print(f"Sequência {i+1}/20 concluída.")
