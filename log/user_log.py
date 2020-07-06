import logging
import os
import datetime
class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        #控制台输出日志
        # consle = logging.StreamHandler()
        # logger.addHandler(consle)
        # logging.debug('log控制台日志')
        # consle.close()
        # logger.removeHandler(consle)

        #文件名字
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,'logs')
        log_file = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
        log_name = log_dir +"\log_"+log_file


        #文件输入日志
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s : %(filename)s ----> %(funcName)s :%(levelno)s %(levelname)s ----> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)
        logging.debug('log文件日志')


    def get_log(self):
        return self.logger

    def close_handle(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)

if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('sdfad')
    user.close_handle()