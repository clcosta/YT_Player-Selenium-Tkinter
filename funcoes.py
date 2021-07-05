from tkinter.constants import TRUE
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AppYt:

    def __init__(self):
        """
        Inicia a classe:
        1. cria a cor do botão de "Play/Pause" por padrão é vermelho
        2. cria o texto do botão "Play/Pause" por padrão é 'pause'
        3. cria a referência status(Bool) para controlar como está o botão "Play/Pause" 
        4. cria a instancia do Webdriver | Caso o usuário não tenha instalado ela vai instalar o webdriver.
        """
        self.corplaypause = 'red'
        self.textopause = 'Pause'
        self._status = True
        self.__webdriver = ChromeDriverManager().install()

    def iniciar_videos(self, busca):
        """Responsável por Inicializar um unico vídeo.

        Args:
            busca ([String]): [Recebe a pesquisa referente a busca que será feita no Youtube]
        """
        
        ## Inicia o navegador controlado pelo código
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(self.__webdriver,options=options)
        self.driver.get("https://www.youtube.com/")
        
        # Aguarda a página carregar para evitar erros
        wait = WebDriverWait(self.driver, 20*60)
        element = wait.until(EC.element_to_be_clickable((By.ID, "search")))
        element.click()

        # Pesquisa a busca desejada pelo usuário
        self.driver.find_element_by_id("search").click()
        self.driver.find_element_by_id("search").send_keys(busca)
        self.driver.find_element_by_id("search-icon-legacy").click()

        # Aguarda os videos carregar para evitar erros
        while len(self.driver.find_elements_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/div/ytd-toggle-button-renderer/a/tp-yt-paper-button/yt-formatted-string')) < 1 :
            time.sleep(1)
        
        # Clica no primeiro vídeo referente a busca do usuário
        self.driver.find_element_by_id("title-wrapper").click()
        time.sleep(5)
        
        # Verifica se o vídeo teve Anúncios e pula se tiver
        ad = self.driver.find_elements_by_xpath('//*[@class="ytp-ad-text"]')
        if len(ad) != 0:
            time.sleep(2)
            element = self.driver.find_element_by_xpath("//button[@class='ytp-ad-skip-button ytp-button']")
            element.click()

    def PausePlay(self):
        """
        Pausa ou da Play na música atual
        e é responsavel por alterar a cor da classe
        que por sua vez é responsavel por alterar o a cor
        do botãos
        """
        if self._status == True:
            self.corplaypause = 'green'
            self.textopause = 'Play'
            self._status = False
            self.driver.find_element_by_css_selector('button.ytp-play-button').click()
        elif self._status == False:
            self.corplaypause = 'red'
            self.textopause = 'Pause'
            self._status = True
            self.driver.find_element_by_css_selector('button.ytp-play-button').click()

    def Proxima(self):
        """
        Pula para a proxima música
        """
        self.driver.find_element_by_css_selector('a.ytp-next-button').click()
        time.sleep(5)
        
        # Verifica se o vídeo teve Anúncios e pula se tiver
        ad = self.driver.find_elements_by_xpath('//*[@class="ytp-ad-text"]')
        if len(ad) != 0:
            time.sleep(3)
            element = self.driver.find_element_by_xpath("//button[@class='ytp-ad-skip-button ytp-button']")
            element.click()


    def __pegar_tempo(texto):
        """Transforma um texto em segundos!

        Args:
            texto ([String]): [Recebe uma String em formato de tempo -> 1:30m]

        Returns:
            tempo ([Int]): [Retorna um número inteiro correspondente ao tempo do texto em SEGUNDOS -> 1:30m = 90 segundos]
        """
        texto = texto.split(":")
        if len(texto) == 3:
            texto[0] = int(texto[0])
            texto[0] = texto[0]*60*60
            texto[1] = int(texto[1])
            texto[1] = texto[1]*60
            texto[2] = int(texto[2])
            tempo = texto[0] + texto[1] + texto[2]
            return tempo
        elif len(texto) == 2 and texto[0] != '0':
            texto[0] = int(texto[0])
            texto[0] = texto[0]*60
            texto[1] = int(texto[1])
            tempo = texto[0] + texto[1]
            return tempo
        elif len(texto) == 2 and texto[0] == '0':
            tempo = int(texto[1])
            return tempo

    def iniciar_vario_videos(self, busca):
        """Responsável por iniciar varios vídeos.

        Args:
            busca ([List]): [Recebe uma lista de pesquisas quer será feita, o tempo do vídeo acabar é o determinante para começar a proxima busca.]
        """
        ## Inicia o navegador controlado pelo código
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(self.__webdriver,options=options)
        
        # Percorre a minha lista de Buscas
        for item in busca:
            self.driver.get("https://www.youtube.com/")

            # Espera a página carregar, faz a busca digitada pelo usuário
            wait = WebDriverWait(self.driver, 20*60)
            element = wait.until(EC.element_to_be_clickable((By.ID, "search")))
            element.click()
            self.driver.find_element_by_id("search").send_keys(item)
            self.driver.find_element_by_id("search-icon-legacy").click()

            # Espera os vídeos carregar
            while len(self.driver.find_elements_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/div/ytd-toggle-button-renderer/a/tp-yt-paper-button/yt-formatted-string')) < 1 :
                time.sleep(1)

            # Clica no primeiro vídeo referente a busca do usuário
            self.driver.find_element_by_id("title-wrapper").click()
            time.sleep(5)
            
            # Verifica se o vídeo teve Anúncios e pula se tiver
            ad = self.driver.find_elements_by_xpath('//*[@class="ytp-ad-text"]')
            if len(ad) != 0:
                time.sleep(2)
                element = self.driver.find_element_by_xpath("//button[@class='ytp-ad-skip-button ytp-button']")
                element.click()

            # Utiliza o tempo do vídeo como referência para ir para a proxima busca.
            time.sleep(10)
            texto_tempo = self.driver.find_element_by_xpath('//span[@class="ytp-time-duration"]').get_attribute('innerHTML')
            tempo = int(AppYt.__pegar_tempo(texto_tempo))
            print(tempo)
            time.sleep(tempo-10)
        self.driver.quit()