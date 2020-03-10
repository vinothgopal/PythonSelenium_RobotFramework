import logging
from sys import stdout
import datetime
import os
class BaseLogger(object):
    def log(self):
        logger=logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        time=str(datetime.datetime.today()).replace(':','-')
        path=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','Logs'))
        if not os.path.exists(path): os.mkdir(path)
        handler=logging.FileHandler(("{0}\log_{1}.html").format(path,time))
        formatter=logging.Formatter("%(message)s")
        logger.addHandler(handler)
        return logger