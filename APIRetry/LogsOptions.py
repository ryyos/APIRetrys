from Exceptions.LogsOptionsEx import PathExceptions

class LogsOptions:
    def __init__(self) -> None:
        pass

    def add_options(self, show_log: bool = False, save_logs: bool = False, path: str = None):
        self.show_log = show_log
        self.save_logs = save_logs
        if self.save_logs: 
            if not path: raise PathExceptions(message='if you turn on save_logs then you must include the path where you save the logs')
        self.path = path