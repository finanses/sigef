"""Documentação para Automação do SIGEF"""

from pyautogui import PAUSE, press, write, hotkey, locateCenterOnScreen, click, doubleClick
from time import sleep

class CenterImageNotFoundError(Exception):
	"""docstring for CenterImageNotFoundError"""
	def __init__(self, path_image, message = 'Coordenadas centrais x e y da imagem não foram encontradas'):	
		self.message = message
		self.path_image = path_image
		super().__init__(self.message)

class AutoSigef(object):
	"""docstring for AutoSigef"""
	def __init__(self, browser: str):
		super(AutoSigef, self).__init__()
		self.PAUSE = 1
		self.browser = browser
		self.image = 'images/image.png'

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

	def __select_image_form__(self):

		try:

			x, y = locateCenterOnScreen(self.image)

			click(x = x, y = y)

		except:

			raise CenterImageNotFoundError(path_image = self.image)

if __name__ == '__main__':

	sigef = AutoSigef(browser = 'chrome')

	sigef.__choose_browser_and_login__()

	sigef.__select_image_form__()
