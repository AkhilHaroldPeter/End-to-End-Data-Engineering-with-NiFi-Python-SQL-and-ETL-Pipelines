##import logging
##import os
##import pandas as pd
##from datetime import datetime
##
### Directory for logs
### Get the root directory of your project
##root_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
##
##print(root_directory)
##print("ABSPATH")
##
### Define the log directory within the root directory
##log_directory = os.path.join(root_directory, 'logs')
##TEMP_LOG_DIR = f"{log_directory}/{pd.to_datetime(datetime.now()).strftime('%Y_%m_%d')}/"
###temp_logs_{pd.to_datetime(datetime.now()).strftime('%Y_%m_%d')}
####FINAL_LOG_DIR = "logs/final_logs"
##
####print(log_directory)
##print(TEMP_LOG_DIR)
##
### Ensure log directories exist
##os.makedirs(TEMP_LOG_DIR, exist_ok=True)
### os.makedirs(FINAL_LOG_DIR, exist_ok=True)
##
##def setup_logger(filename):
##    """Creates a logger for a specific file."""
##    filename = filename.rsplit('.',1)[0]
##    filename = f'{filename}.log'
##    log_path = os.path.join(TEMP_LOG_DIR, filename)
##    
##    logger = logging.getLogger(filename)
##    logger.setLevel(logging.INFO)
##
##    handler = logging.FileHandler(log_path)
##    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
##    handler.setFormatter(formatter)
##
##    logger.addHandler(handler)
##    return logger

import logging
import os
import pandas as pd
from datetime import datetime



def setup_logger(filename):
    # Directory for logs
    # Get the root directory of your project
    root_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    ##print(root_directory)
    ##print("ABSPATH")

    # Define the log directory within the root directory
    log_directory = os.path.join(root_directory, 'logs')
    TEMP_LOG_DIR = f"{log_directory}/{pd.to_datetime(datetime.now()).strftime('%Y_%m_%d')}/"
    ##FINAL_LOG_DIR = "logs/final_logs"

    ##print(log_directory)
    ##print(TEMP_LOG_DIR)

    # Ensure log directories exist
    os.makedirs(TEMP_LOG_DIR, exist_ok=True)
    # os.makedirs(FINAL_LOG_DIR, exist_ok=True)    
    """Creates a logger for a specific file."""
    filename = filename.rsplit('.', 1)[0]
    filename = f'{filename}.log'
    log_path = os.path.join(TEMP_LOG_DIR, filename)
    
    # Create the logger
    logger = logging.getLogger(filename)
    
    # Set the log level to DEBUG to capture all levels of log messages
    logger.setLevel(logging.DEBUG)

    # Create a file handler that appends to the log file
    handler = logging.FileHandler(log_path, mode='a')  # Use 'a' mode for appending
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger
