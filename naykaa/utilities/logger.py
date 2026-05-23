# import logging
# import os
#
#
# def get_logger():
#
#
#
#     if not os.path.exists("logs"):
#
#         os.makedirs("logs")
#
#     logger = logging.getLogger()
#
#     logger.setLevel(logging.INFO)
#
#     file_handler = logging.FileHandler(
#         "logs/automation.log"
#     )
#
#     formatter = logging.Formatter(
#         "%(asctime)s : %(levelname)s : %(message)s"
#     )
#
#     file_handler.setFormatter(formatter)
#
#     logger.addHandler(file_handler)
#
#     return logger
import logging
import os


os.makedirs("logs", exist_ok=True)


logging.basicConfig(
    filename="logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

logger = logging.getLogger()


def get_logger():
    return None