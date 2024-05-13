from zlogger import ZLogger

LOG = ZLogger("odapi", "../docs/config/logging.conf")

LOG.info("Hello World")

LOG.warning("Hello World", request_id='23412_34234_34534', module_name="test_odapi1")
LOG.error("Hello World", request_id='23412_34234_34534', module_name="test_odapi1")

