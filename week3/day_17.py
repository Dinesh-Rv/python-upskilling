# import logging
# from logging.handlers import RotatingFileHandler

# logger = logging.getLogger("dinesh")
# prodLogger = logging.getLogger("prod")
# logger.setLevel(logging.DEBUG)

# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.WARNING)

# file_handler = logging.FileHandler("app.log")
# file_handler.setLevel(logging.DEBUG)

# formatter = logging.Formatter(
#     "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# )
# console_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)

# rotate_handler = RotatingFileHandler(
#     "prod.log", 
#     maxBytes=5 * 1024*1024, 
#     backupCount=3
# )
    
# logger.addHandler(console_handler)
# logger.addHandler(file_handler)

# logger.debug("This is a debug message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")
# logger.critical("This is a critical message")

# try:
#     result = 10 / 0
# except Exception as e:
#     logger.exception(f"An error occurred: {e}", exec_info=True)

import unittest
def calculate_tax(salary):
    if salary < 0:
        raise ValueError("Salary cannot be negative!")
    if salary <= 25000:
        return 0
    elif salary <= 500000:
        return (salary - 25000) * 0.05
    else:
        return (250000 * 0.05) + (salary - 500000) * 0.20

class TestCalculateTax(unittest.TestCase):

    def test_zero_tax(self):
        result = calculate_tax(200000)
        self.assertEqual(result, 0)

    def test_five_percent(self):
        result = calculate_tax(350000)
        self.assertEqual(result, 5000)

    def test_twenty_percent(self):
        result = calculate_tax(600000)
        self.assertEqual(result, 32500)

    def test_negative_salary(self):
        with self.assertRaises(ValueError):
            calculate_tax(-1000)


if __name__ == "__main__":
    unittest.main()