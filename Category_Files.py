'''

This code is a Python script that defines several functions for creation of needed JSON files, which will
contain conversation text data (Q&A).
Additionally files can be moved between directories using libraries like os.

'''

# REQUIRED LIBRARIES
import os
import json
# INTERNAL IMPORT
from Settings import FINAL_FILE_PATH

# FUNCTION DEFINITIONS
# Function to add new process to the JSON file
def add_process(process_name, process_code):

    # Create a new process
    new_process = {
        "Process_name": process_name,
        "Process_code": process_code,
        "tags": {}
    }

    # Create file if not exists
    if not os.path.isfile(FINAL_FILE_PATH):
        with open(FINAL_FILE_PATH, 'w') as f:
            json.dump({"intents": []}, f) #json.dump for writing in JSON format

    # Load the data to the JSON
    with open(FINAL_FILE_PATH, 'r') as f:
        data = json.load(f)

    # Add new process to the list
    data['intents'].append(new_process)

    # Save the new structure
    with open(FINAL_FILE_PATH, 'w') as f:
        json.dump(data, f, indent=4)


# Function to add tags to a process
def add_tag(process_name, tag_name, question, answer):
    # Load the file created
    with open(FINAL_FILE_PATH, 'r') as f:
        data = json.load(f)

    # Look for the process by name
    for process in data['intents']:
        if process['Process_name'] == process_name:
            # Add the new tag
            process['tags'][tag_name] = {
                "question": question,
                "answer": answer
            }
            break

    # Save the new structure
    with open(FINAL_FILE_PATH, 'w') as f:
        json.dump(data, f, indent=4)


# Function to get list of processes
def get_process_list():
    # Load the data to the JSON
    process_list = []
    counter = 0
    with open(FINAL_FILE_PATH, 'r') as f:
        data = json.load(f)

    # Add new process to the list
    for process in data['intents']:
        counter += 1
        process_list.append([str(counter), process['Process_name']])

    return process_list
