import sys
import os
import json
from setup_logger import *
from configparser import RawConfigParser

root_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(root_directory)

# Read config file
# Assuming root_directory is defined somewhere
config_file_path = f'{root_directory}/Config/logconfig.json'  # Use forward slashes or raw string

# Open and load the JSON file
with open(config_file_path, 'r') as f:
    config = json.load(f)  # This reads the JSON file correctly

# Extract command-line arguments (excluding script name)
args = sys.argv[1:]
# print(args)
# Validate argument count (at least filename and config_variable are required)
if len(args) < 2:
    raise ValueError("Usage(Example): python script.py <filename> [batch_id] [file_received] [input_dir] ... <config_variable>")

# Unpack mandatory and optional arguments
filename, *optional_args, config_variable = args  

# Check for duplicate arguments (optional_args can contain the same argument more than once)
seen_args = set()
for arg in optional_args:
    if arg in seen_args:
        raise ValueError(f"Duplicate argument detected: {arg}. Each argument should appear only once.")
    seen_args.add(arg)

# Ensure that the optional arguments have a minimum length of 3, fill with "N/A" if necessary
optional_args += ["N/A"] * (3 - len(optional_args))
# print(len(sys.argv))
# print(len(args))
# print('CHECKING len')


# Ensure there are enough arguments
if len(args) == 5:
    #print("Usage: python script.py <FILENAME> <BATCH_ID> <FILE_RECEIVED> <INPUT_DIR> <CONFIGSECNAME>")
         
    # Fetch the log message from the config
    log_message = config[f'{config_variable}']#config['logmessage'][f'{config_variable}']
    # Unpack the arguments into respective variables
    batch_id, file_received, input_dir, *additional_args = optional_args
    # Handling edge cases: validate types if needed (e.g., ensure batch_id is a string or integer)
    if not isinstance(batch_id, (str, int)):
        raise ValueError(f"Invalid type for batch_id: {batch_id}. Expected string or integer.")      
    
#     Additional arguments (e.g., status etc)
#     status = additional_args[0] if len(additional_args) > 0 else "N/A"
#     You can use this additional arguments if you want to add more and based on the len you can adjust this without breaking the script

#     # Optional: Provide guidance if there are unexpected inputs
#     if len(additional_args) > 3:
#         print(f"Warning: You provided more than 3 additional arguments. Extra arguments are ignored.")

    # Apply format to each log message in the list
    log_message = [
        {
            'log_level': log['log_level'],
            'log_message': log['log_message'].format(
                FILENAME=filename,
                BATCH_ID=batch_id,
                FILE_RECEIVED_AT=file_received,
                INPUT_DIR=input_dir
            )
        }
        for log in log_message
    ]    



elif len(args) == 8:
    #print("Usage: python script.py <FILENAME>  <STATUS> <DURATION> <SOURCE_SYSTEM> <RECORD_COUNT> <ERROR_TYPE> <STACKTRACE> <CONFIGSECNAME>")

    log_message = config[f'{config_variable}'] #config['logmessage'][f'{config_variable}']
    # Unpack the arguments into respective variables
    status, duration, source_system, record_count, error_type, stacktrace, *additional_args = optional_args    
    
        
#     Additional arguments (e.g., status etc)
#     status = additional_args[0] if len(additional_args) > 0 else "N/A"
#     You can use this additional arguments if you want to add more and based on the len you can adjust this without breaking the script
  

#     # Optional: Provide guidance if there are unexpected inputs
#     if len(additional_args) > 3:
#         print(f"Warning: You provided more than 3 additional arguments. Extra arguments are ignored.")    
    
    
    # Apply format to each log message in the list
    log_message = [
        {
            'log_level': log['log_level'],
            'log_message': log['log_message'].format(
                STATUS=status,
                DURATION=duration,
                SOURCE_SYSTEM=source_system,
                RECORD_COUNT=record_count,
                ERROR_TYPE=error_type,
                STACKTRACE=stacktrace
            )
        }
        for log in log_message
    ] 
 
# print(log_message)
# Setup Logger
log_filename = filename  # Change as needed
log_filename = f"{batch_id}_{filename.rsplit('.',1)[0]}.log"
logger = setup_logger(log_filename)
log_entries = log_message#json.loads(f"{log_message}")

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
