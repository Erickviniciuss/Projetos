import pyautogui as pyg
from time import sleep
import pygetwindow as gw
#pyautogui.click() -> Clicar
#pyautogui.press() -> Pressionar uma tecla
#pyautogui.write() -> escrever
#pyautogui.PAUSE = -> Pausa entre códigos
#pyautogui.hotkey() -> Atalho
#pyautogui.position() -> Descobrir posição do mause
#pyautogui.scroll() -> Rola a pagina para cima
list1 = ['c','h','r','o','m','e']
pyg.press("win")
sleep(1)
for c in list1:
    pyg.write(c)
    sleep(0.2)
pyg.press('enter')
sleep(1)
windows = gw.getWindowsWithTitle('Chrome')[0]
if windows.isMaximized:
    print()
else:
    pyg.hotkey('win', 'Up')
sleep(2)
pyg.click(x=626, y=490)
sleep(5)
pyg.click(x=603, y=106)
sleep(10)
pyg.click(x=897, y=515)
sleep(10)
pyg.click(x=358, y=282)