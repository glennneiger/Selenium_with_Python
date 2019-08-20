import logging

logging.basicConfig(
    filename="C:/Users/Usuario/PycharmProjects/Selenium_with_Python/Useful_files/Selenium_logs/test2.log",
    format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is a debug message")
logger.info("This is a debug message")
logger.warning("This is a debug message")
logger.error("This is a debug message")
logger.critical("This is a debug message")
