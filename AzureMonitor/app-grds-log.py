import logging
from logging.handlers import RotatingFileHandler
import os

logger = logging.getLogger('grds_logger')
logDir =  "/omdev/log/grds/" + os.environ['HOSTNAME']
if not os.path.exists(logDir):
    os.makedirs(logDir)
fileName = "RDS-omdev-" + str(os.getpid()) + ".log"
logFile = os.path.join(logDir, fileName)
formatter = logging.Formatter('%(asctime)s|%(name)s|%(threadName)s|%(levelname)s|%(message)s')
handler = RotatingFileHandler(logFile, maxBytes=2000, backupCount=10)
handler.setFormatter(formatter)
logger.addHandler(handler)

for i in range(10):
    logger.warning('GRDS log message!  ' + str(i))
