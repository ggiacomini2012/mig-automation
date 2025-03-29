import pyautogui
import subprocess
import time
import os

# Caminho da imagem no mesmo diretório do script
image_path = os.path.join(os.path.dirname(__file__), 'imagem.png')
print(image_path)

# Função para procurar a imagem
def detect_image():
    while True:
        # Adiciona um pequeno atraso para garantir que a tela esteja carregada
        time.sleep(2)
        
        print("Procurando imagem...")
        
        try:
            # Tenta localizar a imagem na tela
            position = pyautogui.locateOnScreen(image_path, confidence=0.8)  # Aumenta a sensibilidade da busca
            
            if position:
                print(f"Imagem encontrada em: {position}")
                # Executa o comando no terminal
                subprocess.run('echo Encontrei no terminal', shell=True)
                break  # Sai do loop quando a imagem for encontrada
            else:
                print("Imagem não encontrada.")
        
        except pyautogui.ImageNotFoundException:
            # Ignora a exceção e continua o loop
            print("Imagem não encontrada, continuando a busca.")
        
        time.sleep(1)  # Espera 1 segundo antes de verificar novamente

# Executa a função de detecção
detect_image()
