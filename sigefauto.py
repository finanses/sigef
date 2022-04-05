"""Documentação para Automação do SIGEF"""

from pyautogui import PAUSE, press, write, hotkey, locateCenterOnScreen, click, doubleClick
from time import sleep
from credentials import USER, PASSWORD

class CenterImageNotFoundError(Exception):
	"""docstring for CenterImageNotFoundError"""
	def __init__(self, message = 'Coordenadas centrais x e y da imagem não foram encontradas'):	
		self.message = message
		super().__init__(self.message)

class AutoSigef(object):
	"""docstring for AutoSigef"""
	def __init__(self, browser: str, user: str, password: str):
		super(AutoSigef, self).__init__()
		self.PAUSE = 1
		self.browser = browser
		self.image = 'images/image.png'
		self.user = user
		self.password = password

	def __select_image_form__(self):

		try:

			x, y = locateCenterOnScreen(self.image) ## recortar a imagem a partir de um screenshot da tela inteira

			click(x = x, y = y)

		except:

			raise CenterImageNotFoundError()

	def __choose_browser_and_login__(self):

		browsers = {
			'chrome': 'google chrome',
			'firefox': 'firefox',
			'edge': 'microsoft edge',
			'explorer': 'internet explorer'
		}

		press('win')

		write(browsers.get(self.browser))

		press('enter')

		sleep(3) ## desacelerar o processo de escrita em 3 segundos

		write('http://sigef.seplan.ma.gov.br/')

		press('enter')

		sleep(5) ## desacelerar o processo de busca de imagem em 5 segundos

		self.__select_image_form__()

if __name__ == '__main__':

	sigef = AutoSigef(browser = 'chrome', user = USER, password = PASSWORD)

	sigef.__choose_browser_and_login__()
