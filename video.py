from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import tkinter as tk
import threading
import time
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as condicao
# Inicializa o WebDriver
def iniciar_driver():
    chrome_options = Options()
    
    caminho_download = r'E:\Storage\Desktop'  # Corrigir o caminho de download
    
    # Opções do Chrome
    argumentos = ['--lang=pt-BR', '--window-size=1366,768', '--incognito']
    for argumento in argumentos:
        chrome_options.add_argument(argumento)

    # Configurações do Chrome
    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': caminho_download,
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    # Inicializando o WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 9999999999999999999999999999999999999,poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,ElementNotSelectableException])  # Timeout de 10 segundos

    return driver, wait
def abrir_link():
    link = campo.get().strip()
    if link:
        topico = threading.Thread(topico=processar_link, args=(link,))
        topico.start()

def processar_link(link):
    driver.get(link)
    time.sleep(3)
    while True:
        # try = tentar algo
        try:
            pular_video = wait.until(condicao.visibility_of_element_located((By.XPATH,"//div[text()='Pular']")))
            pular_video.click()
            break
        except:
            time.sleep(1) # caso o botao no seja encontrado, vai esperar 1 segundo e tentar dnv



# janela de interface.
janela = tk.Tk()
janela.title('Abrir link')
janela.geometry('500x500')
# interações dentro da janela.
label= tk.Label(janela, width=50)
label.pack(pady=5)

campo = tk.Entry(janela, width=40)
campo.pack(pady=10)

botao= tk.Button(janela, text='Abrir')
botao.pack(padx=10, pady=5)
driver , wait = iniciar_driver()
janela.mainloop()# mantém a janela de interação com o usuario aberta
driver.quit()
