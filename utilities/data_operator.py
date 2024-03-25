''''''

import json
from utilities import log_setup
import traceback

logger = log_setup.getlogger()

def set_value_to_json(json_data,key,value):
    '''
    Set the value of a specific key in a JSON object. 
    Using Recursive search and update the JSON object.

    '''
    # Helper function to recursively search and update the JSON object
    def set_json(json_data,key,value):
        if isinstance(json_data,dict):
            for k,v in json_data.items():
                if k==key:
                    json_data[key]=value
                else:
                    set_json(v,key,value)
        if isinstance(json_data,list):
            for item in json_data:
                set_json(item,key,value)
    set_json(json_data,key,value)

    return json_data


def extract_file_json(file_path):
    '''Extract JSON content from a file. Mostly used to build input Payload of an API'''
    try:
        with open(file_path,'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        logger.error(f"Error Occured: File not found at path: {file_path}")
        logger.error("Error Occured: "+ traceback.format_exc())
        return None
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON file: {e}")
        return None