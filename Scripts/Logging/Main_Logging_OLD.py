import sys
import os
import json
from setup_logger import *
from configparser import RawConfigParser

root_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(root_directory)

# Read config file
config = RawConfigParser()
config.read(f'{root_directory}\Config\iconfig.ini')



# Ensure there are enough arguments
if len(sys.argv) != 6:
    print("Usage: python script.py <FILENAME> <BATCH_ID> <FILE_RECEIVED> <INPUT_DIR> <CONFIGSECNAME>")
#     sys.exit(1) # have added above so the same script can be used irrespective of the attributes.
    #i am assuming that all other logging part will be only with string state

    # Read the command-line arguments
    filename = sys.argv[1]  
    batch_id = sys.argv[2]  
    file_received = sys.argv[3] 
    input_dir = sys.argv[4]
    # Fetch the log message from the config
    log_message = config['logmessage'][f'{sys.argv[5]}']

    # Replace placeholders with command-line arguments
    log_message = log_message.replace("{FILENAME}", filename)
    log_message = log_message.replace("{BATCH_ID}", batch_id)
    log_message = log_message.replace("{FILE_RECEIVED}", file_received)
    log_message = log_message.replace("{INPUT_DIR}", input_dir)

# print(log_message)
# Setup Logger
log_filename = filename  # Change as needed
log_filename = f"{batch_id}_{filename.rsplit('.',1)[0]}.log"
logger = setup_logger(log_filename)
log_entries = json.loads(f"{log_message}")

# Iterate and log each message dynamically
for entry in log_entries:
    log_level = entry.get("log_level", "INFO").upper()
    log_message = entry.get("log_message", "")

    # Log based on level
    if log_level == "DEBUG":
        logger.debug(log_message)
    elif log_level == "INFO":
        logger.info(log_message)
    elif log_level == "WARNING":
        logger.warning(log_message)
    elif log_level == "ERROR":
        logger.error(log_message)
    elif log_level == "CRITICAL":
        logger.critical(log_message)
    else:
        logger.info(f"[UNKNOWN LEVEL] {log_message}")
