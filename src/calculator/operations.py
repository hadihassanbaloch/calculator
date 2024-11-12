# src/calculator/operation.py

import sys
from src.exceptions import CustomException
from src.logger import logger  # Import the logger

class Calculations:
    

    def addition(self, a, b):
        try:
            result = a + b
            logger.info("Performed addition operation")
            return result        
        except Exception as e:
            logger.error("Addition Error Occurred")
            raise CustomException(str(e))
        
        
    def subtract(self, a, b):
        try:
            result = a - b
            logger.info("Performed subtraction operation")
            return result
        except Exception as e:
            logger.error("Subtraction Error Occurred")
            raise CustomException(str(e))
    def multiply(self, a, b):
        try:
            result = a * b
            logger.info(f"Multiplying {a}  {b} == {result}")
            return result
        except Exception as e:
            logger.error("Multiplication Error Occurred")
            raise CustomException(str(e))
    def divide(self, a, b):
        try:
            result = a // b
            logger.info(f"Division {a} {b} == {result}")       
            return result
        except Exception as e:
            raise CustomException(str(e))          
        
