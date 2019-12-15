import logging

logger = logging.getLogger("调试信息")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
format_console = logging.Formatter("%(filename)s - %(levelname)s - %(lineno)s - %(message)s")

ch.setFormatter(format_console)

logger.addHandler(ch)