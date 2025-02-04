from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
import threading
import time

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
    wait = WebDriverWait(driver, 10)  # Timeout de 10 segundos

    return driver, wait

# Função para abrir link e tentar pular anúncio
def abrir_link():
    url = entrada.get().strip()
    if url:
        thread = threading.Thread(target=processar_link, args=(url,))
        thread.start()

# Função separada para evitar travamento da interface
def processar_link(url):
    driver.get(url)
    time.sleep(3)  # Tempo para a página carregar

    while True:
        try:
            # Espera até 5 segundos para encontrar o botão "Pular"
            pular_video = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Pular']")))
            pular_video.click()
            print("Anúncio pulado!")
            break  # Sai do loop após pular o anúncio
        except:
            print("Nenhum botão de pular anúncio encontrado. Tentando novamente...")
            time.sleep(2)

# Criando a interface gráfica
janela = tk.Tk()
janela.title("Abrir Link de Vídeo")
janela.geometry("400x150")

# Widgets da interface
label = tk.Label(janela, text="Cole o link do vídeo:")
label.pack(pady=10)

entrada = tk.Entry(janela, width=50)
entrada.pack(pady=5)

botao = tk.Button(janela, text="Abrir", command=abrir_link)
botao.pack(pady=10)

# Inicializa o WebDriver
driver, wait = iniciar_driver()

# Mantém a interface gráfica rodando
janela.mainloop()

# Fecha o navegador ao encerrar a interface
driver.quit()
