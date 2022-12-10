from datetime import datetime


class Logger:
    
    class TextColors:
        HEADER = '\033[95m'     # Purple
        OKBLUE = '\033[94m'     # Blue
        OKCYAN = '\033[96m'     # Cyan
        OKGREEN = '\033[92m'    # Green
        WARNING = '\033[93m'    # Orange
        ERROR = '\033[91m'      # Red
        CLASSIC = '\033[0m'     # Classic
        BOLD = '\033[1m'        # Bold
        UNDERLINE = '\033[4m'   # Bold and Underline


    @staticmethod
    def get_time():
        now = datetime.now()
        return '{:02d}:{:02d}:{:02d}'.format(now.hour, now.minute, now.second)


    @staticmethod
    def __log(type, message, color=TextColors.CLASSIC):
        print('{hour}  {color}{type:7}{color_clear} | {message}'.format(
            color_clear=Logger.TextColors.CLASSIC,
            hour=Logger.get_time(),
            message=message,
            color=color,
            type=type
        ))


    @staticmethod
    def info(message):
        Logger.__log('INFO', message, Logger.TextColors.OKBLUE)


    @staticmethod
    def warning(message):
        Logger.__log('WARNING', message, Logger.TextColors.WARNING)


    @staticmethod
    def error(message):
        Logger.__log('ERROR', message, Logger.TextColors.ERROR)    


    @staticmethod
    def success(message):
        Logger.__log('SUCCESS', message, Logger.TextColors.OKGREEN)


    @staticmethod
    def debug(message):
        Logger.__log('DEBUG', message, Logger.TextColors.HEADER)
    

    
if __name__ == '__main__':
    Logger.info('Lorem ipsum dolor sit elit!')
    Logger.warning('Lorem ipsum dolor sit elit!')
    Logger.error('Lorem ipsum dolor sit elit!')
    Logger.success('Lorem ipsum dolor sit elit!')
    Logger.debug('Lorem ipsum dolor sit elit!')