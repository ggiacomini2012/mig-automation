import pyautogui
import time

# Pressiona a tecla Windows
pyautogui.press('winleft')  # Ou 'winright', dependendo do seu teclado

# Espera 3 segundos
time.sleep(3)

# Digita 'bob'
pyautogui.write('bob')

# Espera 5 segundos
time.sleep(5)

# Aperta Enter
pyautogui.press('enter')
