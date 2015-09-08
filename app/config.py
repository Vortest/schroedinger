import logging
import os

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
logger.setLevel(logging.ERROR)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BROWSER = "Firefox"