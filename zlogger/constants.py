# Constants for the application
from enum import Enum

# custom log levels
SUCCESS = 'SUCCESS'
REJECT = 'REJECT'
FATAL = 'FATA'

# logging configuration parameters
class LogConfig(Enum):
    LOG = 'log'
    LEVEL = 'level'
    LOG_STDOUT = 'log_stdout'
    LOG_STDERR = 'log_stderr'
    LOG_FILE = 'log_file'
    ENABLED = 'enabled'
    FILE_NAME = 'filename'
    FILE_EXTENSION = 'file_extension'
    LOG_PATH = 'log_path'
    MAX_FILE_SIZE = 'max_file_size'
    MAX_AGE_DAYS = 'max_age_days'
    MAX_STORAGE_SIZE = 'max_storage_size'
    ARCHIVE_PATH = 'archive_path'
    LOG_FILE_PATH = 'log_file_path'
    REQUEST_ID = 'request_id'
    MODULE_NAME = 'module_name'
    FUNCTION_NAME = 'function_name'
    FILE_PATH = 'file_path'
    LINE_NO = 'line_no'
    ASCTIME1 = 'asctime1'
    DATA = 'data'

class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

# default log levels
class LogLevel(ExtendedEnum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    SUCCESS = 'SUCCESS'
    REJECT = 'REJECT'
    FATAL = 'FATAL'


# error codes and their descriptions
ERROR_DESC = {
    "303": "Log filename cannot be empty",
    "305": "Log file extension cannot be empty",
    "310": "Log file path cannot be empty",
    "311": "Max file size cannot be empty",
    "312": "log_stdout and log_stderr must be boolean values",
    "313": "Max age days cannot be empty",
    "314": "Max storage size cannot be empty",
    "315": "Archive path cannot be empty",
}