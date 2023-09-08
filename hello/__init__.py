
import logging
import os

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ROOT_DIRNAME = os.path.dirname(os.path.realpath(__file__))
LOG_FILENAME = '/tmp/{}.log'.format(__name__)
