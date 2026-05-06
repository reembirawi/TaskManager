import logging


def setup_logger():
    logging.basicConfig(
        filename='app.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
