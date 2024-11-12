import sys
from src.logger import logger 

class CustomException(Exception):
    def __init__(self, error_message):
        
        # Capture traceback information
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        
         # Create a simplified error message
        self.error_message = f"Error in [{file_name}] at line [{line_number}]: {error_message}"
        
        logger.error(self.error_message)

    def __str__(self):
        return self.error_message