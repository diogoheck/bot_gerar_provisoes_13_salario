import pyautogui
from time import sleep
from funcao_locate.localizar_elemento import localizar_elemento_tela


def acessar_modulo_folha():
    sleep(5)
   # clicar no unico contabil para abrir opcoes
    pyautogui.click(1174, 58, duration=1)
    sleep(2)
    # mover ate opcao unico folha
    pyautogui.move(0, 38, duration=1)
    sleep(2)
    # clicar unico folha para mudar o modulo
    pyautogui.click()
    sleep(10)
