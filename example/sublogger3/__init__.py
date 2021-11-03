import wblog
print(f"sublogger3/__init__.py: {__name__}")

from . import subsublogger1
from . import subsublogger2

logger = wblog.getLogger()


def info(msg):
    logger.info(msg)

def warning(msg):
    logger.warning(msg)

def debug(msg):
    logger.debug(msg)
