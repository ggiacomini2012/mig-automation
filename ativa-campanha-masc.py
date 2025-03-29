import keyboard  # Para detectar atalhos de teclado
import subprocess  # Para executar outros scripts Python
import pygetwindow as gw  # Para manipular a janela do terminal

def minimizar_janela_terminal():
    """Função para minimizar a janela do terminal."""
    janela_terminal = gw.getWindowsWithTitle("Command Prompt")  # Ou use o nome do terminal que está sendo usado
    if janela_terminal:
        janela_terminal[0].minimize()  # Minimiza a janela

def executar_script():
    """Função que executa um arquivo Python."""
    try:
        # Substitua o caminho pelo arquivo Python que deseja executar
        caminho_script = r"C:\Users\Cliente Network\Desktop\automation\campanha-masc.py"
        subprocess.Popen(["python", caminho_script, "20"])  # Executa o script
        print(f"Executando: {caminho_script}")
        
        # Minimiza a janela do terminal após iniciar o script
        minimizar_janela_terminal()

    except Exception as e:
        print(f"Erro ao tentar executar o script: {e}")

# Define o atalho Alt + B para executar o script
keyboard.add_hotkey('alt+b', executar_script)

print("O programa está rodando em segundo plano. Pressione Alt + B para executar o script.")
print("Pressione Ctrl + M para sair.")

# Mantém o programa rodando até Ctrl + M ser pressionado
keyboard.wait('ctrl+m')  # Sai quando Ctrl + M é pressionado
