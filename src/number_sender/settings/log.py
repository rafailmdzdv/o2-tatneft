import logging
import pathlib


LOGFILE_PATH = pathlib.Path(__file__).resolve().parent.parent


def get_logger() -> logging.Logger:
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] - [%(name)s] -- %(message)s'
    )
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(f'{LOGFILE_PATH}/log.log')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


logger = get_logger()
