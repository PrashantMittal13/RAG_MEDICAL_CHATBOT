import sys
from typing import Optional

class CustomException(Exception):
    def __init__(self, message: str, error_detail: Optional[Exception] = None):
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message, error_detail):
        _, _, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
        return f"{message} | Error: {error_detail} | File: {file_name} | Line: {line_number}"

    def __str__(self):
        return self.error_message
    

    # what is static method, what is super() function, what is exc_tb, what is exc_info






    '''exc_type, exc_value, exc_tb = sys.exc_info()

    exc_type: The type of the error (eg: <class 'ZeroDivisionError'>)
    exc_value: The actual error object (eg: ZeroDivisionError('division by zero'))
    exc_tb: The traceback object — tells where the error happened (eg:File name, line number, function name, etc. )
    '''