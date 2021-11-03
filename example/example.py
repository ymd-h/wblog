# Example script for explaining wblog logging
#
# In order to explain nested logging behavior, we call these logging functions
# at top level script, however, it is not designed use case.
# Each logger is designed to call inside their module.
#
# Package / Module Structure:
#   + -- example.py
#   + -- sublogger1.py
#   + -- sublogger2.py
#   + -- sublogger3/
#        + -- __init__.py
#        + -- subsublogger1.py
#        + -- subsublogger2.py
#
# Notes:
#   We intentionally use print function to distinguish from logging functions.
#
# Predefined logging levels:
#   |name    |int|
#   |--------|---|
#   |CRITICAL| 50|
#   |ERROR   | 40|
#   |WARNING | 30|
#   |INFO    | 20|
#   |DEBUG   | 10|
#   |NOTSET  |  0|


import logging

import wblog
print(f"example.py: {__name__}")

import sublogger1
import sublogger2
import sublogger3

print("")

logger = wblog.getLogger()

print("1. Default Config: No logs are shown because of no handlers.")
# Global default config
# - Root logger has logging.WARNING level.
# - Root logger has no handlers.
# - Package top level logger has NullHandler.

logger.debug("logger.debug")
logger.info("logger.info")
logger.warning("logger.warning")

sublogger1.debug("sublogger1.debug")
sublogger1.info("sublogger1.info")
sublogger1.warning("sublogger1.warning")

sublogger2.debug("sublogger2.debug")
sublogger2.info("sublogger2.info")
sublogger2.warning("sublogger2.warning")

sublogger3.debug("sublogger3.debug")
sublogger3.info("sublogger3.info")
sublogger3.warning("sublogger3.warning")

sublogger3.subsublogger1.debug("sublogger3.subsublogger1.debug")
sublogger3.subsublogger1.info("sublogger3.subsublogger1.info")
sublogger3.subsublogger1.warning("sublogger3.subsublogger1.warning")

sublogger3.subsublogger2.debug("sublogger3.subsublogger2.debug")
sublogger3.subsublogger2.info("sublogger3.subsublogger2.info")
sublogger3.subsublogger2.warning("sublogger3.subsublogger2.warning")


print("")

print("2. logging.basicConfig(): All logs above warning are shown")
logging.basicConfig()
# - Root logger has logging.WARNING level.
# - Root logger has StreamHandler to console standard error.
# - Package top level logger has NullHandler.
# - All logs are delegated to root logger.

logger.debug("logger.debug")
logger.info("logger.info")
logger.warning("logger.warning")

sublogger1.debug("sublogger1.debug")
sublogger1.info("sublogger1.info")
sublogger1.warning("sublogger1.warning")

sublogger2.debug("sublogger2.debug")
sublogger2.info("sublogger2.info")
sublogger2.warning("sublogger2.warning")

sublogger3.debug("sublogger3.debug")
sublogger3.info("sublogger3.info")
sublogger3.warning("sublogger3.warning")

sublogger3.subsublogger1.debug("sublogger3.subsublogger1.debug")
sublogger3.subsublogger1.info("sublogger3.subsublogger1.info")
sublogger3.subsublogger1.warning("sublogger3.subsublogger1.warning")

sublogger3.subsublogger2.debug("sublogger3.subsublogger2.debug")
sublogger3.subsublogger2.info("sublogger3.subsublogger2.info")
sublogger3.subsublogger2.warning("sublogger3.subsublogger2.warning")

# Remove handlers from root logger
root_logger = logging.getLogger()

## We ensure to remove all handlers, however, there is only a StreamHandler.
for h in [h for h in root_logger.handlers]:
    root_logger.removeHandler(h)


print("")

print("3. Enable only sublogger1: Only sublogger1 shows log")
wblog.start_logging("sublogger1", logging.DEBUG)
# - Root logger has logging.WARNING level.
# - Root logger has no handlers.
# - Package top level logger has NullHandler.
# - sublogger1 has loggong.DEBUG level.
# - sublogger1 has StreamHandler

logger.debug("logger.debug")
logger.info("logger.info")
logger.warning("logger.warning")

sublogger1.debug("sublogger1.debug")
sublogger1.info("sublogger1.info")
sublogger1.warning("sublogger1.warning")

sublogger2.debug("sublogger2.debug")
sublogger2.info("sublogger2.info")
sublogger2.warning("sublogger2.warning")

sublogger3.debug("sublogger3.debug")
sublogger3.info("sublogger3.info")
sublogger3.warning("sublogger3.warning")

sublogger3.subsublogger1.debug("sublogger3.subsublogger1.debug")
sublogger3.subsublogger1.info("sublogger3.subsublogger1.info")
sublogger3.subsublogger1.warning("sublogger3.subsublogger1.warning")

sublogger3.subsublogger2.debug("sublogger3.subsublogger2.debug")
sublogger3.subsublogger2.info("sublogger3.subsublogger2.info")
sublogger3.subsublogger2.warning("sublogger3.subsublogger2.warning")


# Stop logging
wblog.stop_logging("sublogger1")

print("")


print("4. Enable only sublogger3. sublogger3, subsublogger1, and subsublogger2 show logs")
wblog.start_logging("sublogger3")
# - Root logger has logging.WARNING level.
# - Root logger has no handlers.
# - Package top level logger has NullHandler.
# - sublogger3 has loggong.DEBUG level.
# - sublogger3 has StreamHandler

logger.debug("logger.debug")
logger.info("logger.info")
logger.warning("logger.warning")

sublogger1.debug("sublogger1.debug")
sublogger1.info("sublogger1.info")
sublogger1.warning("sublogger1.warning")

sublogger2.debug("sublogger2.debug")
sublogger2.info("sublogger2.info")
sublogger2.warning("sublogger2.warning")

sublogger3.debug("sublogger3.debug")
sublogger3.info("sublogger3.info")
sublogger3.warning("sublogger3.warning")

sublogger3.subsublogger1.debug("sublogger3.subsublogger1.debug")
sublogger3.subsublogger1.info("sublogger3.subsublogger1.info")
sublogger3.subsublogger1.warning("sublogger3.subsublogger1.warning")

sublogger3.subsublogger2.debug("sublogger3.subsublogger2.debug")
sublogger3.subsublogger2.info("sublogger3.subsublogger2.info")
sublogger3.subsublogger2.warning("sublogger3.subsublogger2.warning")


