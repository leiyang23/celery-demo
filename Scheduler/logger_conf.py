import logging

logger = logging.getLogger("调试信息")
logger.setLevel(logging.ERROR)

ch = logging.StreamHandler()
format_console = logging.Formatter("%(filename)s - %(levelname)s - %(lineno)s - %(message)s")

ch.setFormatter(format_console)

logger.addHandler(ch)