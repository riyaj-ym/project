import logging


class LogGen:
    @staticmethod
    def logGen():
        logging.basicConfig(filename="./logs/automationLog.log",
                            format="%(asctime)s, %(levelname)s, %(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p",
                            force=True,
                            filemode='w')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
