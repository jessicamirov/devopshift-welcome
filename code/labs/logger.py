import logging
import json
import os 
import sys

class JsonFormatter(logging.Formatter):
    def format(self,record:logging.LogRecord) -> str:
        log = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage()
        }
        return json.dumps(log)

LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG")
LOG_FORMAT = os.environ.get("LOG_FORMAT", "JSON")

logger = logging.getLogger("myapp")
logger.setLevel(LOG_LEVEL)
stdout_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler("log.txt")

if LOG_FORMAT == "JSON":
    formatter = JsonFormatter()
else:
    formatter = logging.Formatter()

stdout_handler.setFormatter(formatter)
