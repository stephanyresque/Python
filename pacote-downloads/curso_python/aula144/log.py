# Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError(
            'Implemente o método log'
        )
    def log_error(self, msg):
        return self._log(f'error: {msg}')
    def log_sucess(self, msg):
        return self._log(f'sucess: {msg}')
    

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formata = f'{msg} {self.__class__.__name__}'
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formata)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lf = LogFileMixin()
    lf.log_error('qualquer coisa dnv')
    


