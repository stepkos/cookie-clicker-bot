from enum import Enum
from datetime import datetime


class Logger:
    
    class TextStyle(Enum):
        PURPLE = '\033[95m'
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        ORANGE = '\033[93m'
        RED = '\033[91m'
        
        CLASSIC = '\033[0m'
        BOLD = '\033[1m'
        BOLD_AND_UNDERLINE = '\033[4m'


    @staticmethod
    def get_time():
        now = datetime.now()
        return '{:02d}:{:02d}:{:02d}'.format(now.hour, now.minute, now.second)


    @staticmethod
    def __log(type, message, color=TextStyle.CLASSIC):
        print('{hour}  {color}{type:7}{color_clear} | {message}'.format(
            color_clear=Logger.TextStyle.CLASSIC.value,
            hour=Logger.get_time(),
            message=message,
            color=color.value,
            type=type
        ))


    @staticmethod
    def info(message):
        Logger.__log('INFO', message, Logger.TextStyle.BLUE)


    @staticmethod
    def warning(message):
        Logger.__log('WARNING', message, Logger.TextStyle.ORANGE)


    @staticmethod
    def error(message):
        Logger.__log('ERROR', message, Logger.TextStyle.RED)    


    @staticmethod
    def success(message):
        Logger.__log('SUCCESS', message, Logger.TextStyle.GREEN)


    @staticmethod
    def debug(message):
        Logger.__log('DEBUG', message, Logger.TextStyle.PURPLE)
    

    
if __name__ == '__main__':
    Logger.info('Lorem ipsum dolor sit elit!')
    Logger.warning('Lorem ipsum dolor sit elit!')
    Logger.error('Lorem ipsum dolor sit elit!')
    Logger.success('Lorem ipsum dolor sit elit!')
    Logger.debug('Lorem ipsum dolor sit elit!')