import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
logger.setLevel(logging.ERROR)
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

BROWSER = "Firefox"