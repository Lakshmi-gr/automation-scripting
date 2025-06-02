import logging

def get_logger(add_logger):
    logger = logging.getLogger(add_logger)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler("test_log.log")
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger