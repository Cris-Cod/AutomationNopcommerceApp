import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fileHandler = logging.FileHandler('./Logs/logfile.log', mode='w')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.addHandler(fileHandler)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger