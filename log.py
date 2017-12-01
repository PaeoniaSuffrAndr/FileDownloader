#encoding=utf-8
__author__ = 'Administrator'

import logging
import logging.handlers
import os
import time

class LOG:

    def __init__(self, filesize, dir = None): #初始化，fileszie为日志文件最大大小，如果超出，则日志写入到新的文件
        if(dir is None):
            self.PATH = os.path.join(os.getcwd(), 'log')
        else:
            self.PATH = os.path.join(os.getcwd(), dir)
        self.EXTNAME = '.log'
        self.FILESIZE = filesize
        self.logger = logging.getLogger()
        self.FILENAME = ''

    def __check(self, filename): #私有方法__check()，用于检测并生成日志文件名
        path = os.path.join(self.PATH, time.strftime('%Y%m%d'))
        if(not os.path.exists(path)):
            os.makedirs(path)
        LOG_FILENAME = os.path.join(path, filename + self.EXTNAME)
        if(os.path.exists(LOG_FILENAME)):
            filesize = os.path.getsize(LOG_FILENAME)
            if(filesize > self.FILESIZE):
                for i in range(1,100):
                    newFileName = filename + '(' + str(i) + ')'
                    LOG_FILENAME = os.path.join(path, newFileName + self.EXTNAME)
                    if(os.path.exists(LOG_FILENAME)):
                        filesize = os.path.getsize(LOG_FILENAME)
                        if(filesize < self.FILESIZE):
                            break
                    else:
                        break
        self.FILENAME = LOG_FILENAME

    def __info(self, content): #私有方法 __info()
        handler = logging.FileHandler(self.FILENAME)
        formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.level = logging.NOTSET
        self.logger.info(content)
        self.logger.removeHandler(handler)
        handler.close()

    def info(self, content): #公共方法 info() 写info日志
        self.__check('info')
        self.__info(content)

    def __debug(self, content): #私有方法 __debug
        handler = logging.FileHandler(self.FILENAME)
        formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.level = logging.NOTSET
        self.logger.debug(content)
        self.logger.removeHandler(handler)
        handler.close()

    def debug(self, content): #公共方法 debug() 写debug日志
        self.__check('debug')
        self.__debug(content)

    def __warning(self, content): #私有方法 __warning()
        handler = logging.FileHandler(self.FILENAME)
        formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.level = logging.NOTSET
        self.logger.warning(content)
        self.logger.removeHandler(handler)
        handler.close()

    def warning(self, content): #公共方法 warning() 写warning日志
        self.__check('warning')
        self.__warning(content)

    def __error(self, content): #私有方法 __error()
        handler = logging.FileHandler(self.FILENAME)
        formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.level = logging.NOTSET
        self.logger.error(content)
        self.logger.removeHandler(handler)
        handler.close()

    def error(self, content): #公共方法 error() 写error日志
        self.__check('error')
        self.__error(content)