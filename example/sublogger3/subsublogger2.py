import wblog
print(f"sublogger3/subsublogger2.py: {__name__}")

logger = wblog.getLogger()


def info(msg):
    logger.info(msg)

def warning(msg):
    logger.warning(msg)

def debug(msg):
    logger.debug(msg)
