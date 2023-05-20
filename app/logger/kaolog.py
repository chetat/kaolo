import logging
import json


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_object = {
            "level": record.levelname,
            "message": record.getMessage(),
            "time": self.formatTime(record),
            "source": record.pathname,
            "line": record.lineno,
            "function": record.funcName,
        }
        return json.dumps(log_object)


def get_logger(name):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())

    logger.addHandler(handler)
    return logger
