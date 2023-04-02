'''

This code is a Python script that uses the ChatterBot library to create a ChatBot.
For the ML learning part is uses 3 adapters: SpecificResponseAdapter, BestMatch, and MathematicalEvaluation

'''

# REQUIRED LIBRARIES
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer # training based on existing data
from chatterbot.response_selection import get_random_response # creation of random responses

# IMPORT REFERENCES
import Conversations as Convo
from Category_Files import get_process_list

# INITIALIZATION
# Additionally implementation of 3 different logic adapters
myko_bot = ChatBot(name='Mykobot', read_only=True,
                   response_selection_method=get_random_response,
                   logic_adapters=[
                       {
                           'import_path': 'chatterbot.logic.SpecificResponseAdapter', # Specific answers to pre defined input
                           'input_text': 'empty',
                           'output_text': ''
                       },
                       {
                           'import_path': 'chatterbot.logic.BestMatch', # Selection of best match responses pre defined by maximum_similarity_threshold
                           'default_response': 'NONE',
                           'maximum_similarity_threshold': 0.9
                       },
                       {
                           'import_path': 'chatterbot.logic.MathematicalEvaluation' # Evaluates mathematical expressions entered by the user
                       }
                   ]
                   )

# TRAINING ON CORPUS
trainer = ChatterBotCorpusTrainer(myko_bot)
# chatterbot.corpus.english includes pre-defined chatterbot training text data
trainer.train(
    "chatterbot.corpus.english"
)

# Function to get visa type process by searching for it in the list of created processes fromm Category_Files
def get_process_name(process_code):
    process_name = ''
    process_list = get_process_list()
    for process in process_list:
        if process[0] == process_code:
            process_name = process[1]
    return process_name

# Function to take a question or user input and return a response form Mykobot
def get_response(question, option):
    full_answer = ''
    if option == '':
        # get response form predefined Mykobot
        initial_response = myko_bot.get_response(question).text
        if initial_response == 'NONE':
            # look for response in the Conversations
            if len(Convo.get_bot_response(question, option)) != 0:
                complete_answer = ''
                for answer in Convo.get_bot_response(question, ''):
                    complete_answer += str(answer) + ', '
                full_answer = str(complete_answer)
            # if there is no response return OPTION
            else:
                full_answer = 'OPTION'
        else:
            full_answer = str(initial_response)
    elif option != '' and question != '':
        process_name = get_process_name(option)
        if len(Convo.get_bot_response(question, process_name)) != 0:
            complete_answer = 'Sure, for the ' + process_name + ' '
            for answer in Convo.get_bot_response(question, process_name):
                complete_answer += str(answer) + ', '
            full_answer = complete_answer
        # if everything is empty return predefined answer text and try again
        else:
            full_answer = text = 'I\'m sorry, let\'s try again!'
    return full_answer