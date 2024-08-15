import logging
from logging.handlers import RotatingFileHandler
import os

logger = logging.getLogger('gis_logger')
logDir =  "/omdev/log/gis/" + os.environ['HOSTNAME']
if not os.path.exists(logDir):
    os.makedirs(logDir)
fileName = "GIS-omdev-" + str(os.getpid()) + ".log"
logFile = os.path.join(logDir, fileName)
formatter = logging.Formatter('%(asctime)s|%(name)s|%(threadName)s|%(levelname)s|%(message)s')
handler = RotatingFileHandler(logFile, maxBytes=2000, backupCount=10)
handler.setFormatter(formatter)
logger.addHandler(handler)

for i in range(10):
    logger.warning('GIS log message!  ' + str(i))
