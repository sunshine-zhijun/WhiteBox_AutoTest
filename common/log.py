from loguru import logger
TRACE = 5
DEBUG = 10
INFO = 20
SUCCESS = 25
WARNING = 30
ERROR = 40
CRITICAL = 50
fail = 'FAIL'
display = 'DIS'
logger.level(fail, no=100, color='<red><bold>', icon='x')
logger.level(display, no=21, color='<yellow><bold>')
logger.add('log/runtime_{time:YYYY-MM-DD_HH-mm-ss}.log', retention='1 days', level=5)
logger.add('log/test.log', retention='7 days', rotation='50 MB', compression='zip')