# Zlogger

## Description
Zlogger is a  customizable logging library for Python applications. It provides a flexible and extensible solution for logging messages with different severity levels, including custom levels like SUCCESS, REJECT, and FATAL. Zlogger supports logging to the console, files, and allows easy configuration of log formats, file rotation, and log archiving.

## Installation
To install Zlogger, you can use pip:
```python
pip install git+ssh://git@git.ghpcard.local:122/dbelii/zlogger.git
```
## Usage
To use Zlogger in your Python application, follow these steps:

1. Import the `ZLogger` class from the `zlogger` module.
2. Create an instance of `ZLogger` by providing a name and configuration settings.
3. Use the `with_request_id`, `with_module_name` and `with_additional_data` methods to add extra context to your log messages.
4. Call the appropriate logging methods (`fatal`, `reject`, `success`, `debug`, `info`, `warning`, `error`) to log messages with different severity levels.

#### Example

```python
from zlogger import ZLogger

path_file = "../docs/config/logging.ini"
config = configparser.ConfigParser()
config.read(path_file)

logger = ZLogger('my_app', config)

logger.with_request_id('123').with_module_name("resize").info('Request processing started')
logger.with_additional_data({'user_id': 456}).debug('User authenticated')
logger.success('Operation completed successfully')
logger.error('An error occurred')
```
