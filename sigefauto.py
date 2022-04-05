"""Documentação para Automação do SIGEF"""

from pyautogui import PAUSE, press, write, hotkey, locateOnScreen, click, doubleClick
from time import sleep

class AutoSigef(object):
	"""docstring for AutoSigef"""
	def __init__(self, browser: str):
		super(AutoSigef, self).__init__()
		self.PAUSE = 1
		self.browser = browser
		
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

if __name__ == '__main__':

	sigef = AutoSigef(browser = 'chrome')

	sigef.__choose_browser_and_login__()
