'''

This code is a Python script that defines functions for processing user input.
It uses spacy library for NLP and defines entities and responses in a conversation between user and Mykobot
using the text data from JSON files.

'''

# REQUIRED LIBRARIES
import difflib # for comparison and fining better match
import spacy
import json
from Settings import FINAL_FILE_PATH

# LOAD NLP MODEL
# Load the language model to use with SpaCy
nlp = spacy.load('en_core_web_sm')
# Definition of english stop words to delete connectors
en_stopwords = list(spacy.lang.en.stop_words.STOP_WORDS)
# Testing categories
categories_clean = ['description', 'prerequisite', 'document', 'form', 'fee', 'law', 'time', 'additional', 'authority']


# Function to get the JSON from the Conversations.json file
def get_conversation(file_name):
    # Load the JSON data from a file
    with open(file_name, 'r') as file:
        data = json.load(file)
    file.close()
    return data


# Function to get the user's intentions
def get_user_intentions(user_input):
    # DOCUMENT CREATION
    # Doc creation to save the information from the user question and input
    user_input_doc = nlp(user_input)
    # Identify nouns to identify entities in the conversation
    user_input_chunk = []
    for chunk in user_input_doc.noun_chunks: # doc.noun_chunks
        user_input_chunk.append(chunk)
    # Identify the possible tag within the user intents
    user_intentions = []
    for label in user_input_chunk:
        # Tokenize and remove stop words
        doc = nlp(str(label))
        for word in doc:
            if str(word) not in en_stopwords:  # Removing connectors within the user input
                if str(word) != str(word.lemma_):
                    user_intentions.append(str(word.lemma_))
                else:
                    user_intentions.append(str(word))
    return user_intentions


# Function to get the bot response
def get_bot_response(user_input, process_name):
    # Load the JSON data from a file
    process_conversation = get_conversation(FINAL_FILE_PATH)
    # Loop through the keys in the processes dictionary
    # tag is the key to find in the document this is part of the intention
    # Initial loop to look for within the document
    tags_user_input = get_user_intentions(user_input)
    bot_answers = []
    for process in process_conversation['intents']:
        if process_name == process['Process_name']:
            for key in process['tags']:
                match = difflib.get_close_matches(key, tags_user_input, n=1)
                if len(match) != 0:
                    bot_answers.append(process['tags'][key]['answer'])
            break

    return bot_answers



