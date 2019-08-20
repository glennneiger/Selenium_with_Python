import logging

logging.basicConfig(
    filename="C:/Users/Usuario/PycharmProjects/Selenium_with_Python/Useful_files/Selenium_logs/test.log",
    format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

logging.debug("This is a debug message")
logging.info("This is a debug message")
logging.warning("This is a debug message")
logging.error("This is a debug message")
logging.critical("This is a debug message")
