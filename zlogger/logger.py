import logging
import os
import inspect
from functools import wraps
import logging.config

class ZLogger(logging.Logger):
    def __init__(self, name, config_file_path, level=logging.INFO):
        """
        Initialize the CustomLogger with a name, configuration file path, and logging level.
        """
        super().__init__(name, level)
        logging.config.fileConfig(config_file_path)
        self.logger = logging.getLogger(name)

    def log_decorator(func):
        """
        Decorator function that adds additional context information to log messages.
        """
        @wraps(func)
        def wrapper(self, message, request_id=None, module_name=None, *args, **kwargs):
            # Get the caller's frame information
            caller_frame = inspect.currentframe().f_back
            caller_func_name = caller_frame.f_code.co_name
            caller_file_name = caller_frame.f_code.co_filename

            # If the caller is the main module, use the file name as the function name
            if caller_func_name == "<module>":
                caller_func_name = os.path.splitext(os.path.basename(caller_file_name))[0]

            # Create the extra context dictionary
            extra_context = {
                'request_id': request_id if request_id is not None and module_name is not None else None,
                'function_name': caller_func_name,
                'file_path': caller_file_name,
                'module_name': module_name if request_id is not None and module_name is not None else None
            }

            # Call the original function with the additional context
            return func(self, message, extra=extra_context, *args, **kwargs)
        return wrapper

    @log_decorator
    def debug(self, message, *args, **kwargs):
        """
        Log a DEBUG message with additional context.
        """
        self.logger.debug(message, *args, **kwargs)

    @log_decorator
    def info(self, message, *args, **kwargs):
        """
        Log an INFO message with additional context.
        """
        self.logger.info(message, *args, **kwargs)

    @log_decorator
    def warning(self, message, *args, **kwargs):
        """
        Log a WARNING message with additional context.
        """
        self.logger.warning(message, *args, **kwargs)

    @log_decorator
    def error(self, message, *args, **kwargs):
        """
        Log an ERROR message with additional context.
        """
        self.logger.error(message, *args, **kwargs)

    @log_decorator
    def critical(self, message, *args, **kwargs):
        """
        Log a CRITICAL message with additional context.
        """
        self.logger.critical(message, *args, **kwargs)
        
        
        
        
        
        
        
        
        