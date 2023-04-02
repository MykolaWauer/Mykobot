'''

This code is a Python program that creates GUI (Graphical User Interface) for basic interactions with Mykobot.

-> Dialog window where user give text input and/or question
-> Mykobot recieve the message and generates a response

-> GUI interface: Tkinter

'''

# REQUIRED LIBRARIES
from tkinter import *
import time

# IMPORT REFERENCES
from Category_Files import get_process_list
from Mykobot_Model import get_response

# DEFINE COLORS
BG_GRAY = '#ABB2B9'
BG_COLOR = '#17202A'
BG_ENTRY_COLOR = '#2C3E50'
TEXT_COLOR = '#EAECEE'

# DEFINE FONT
FONT = 'Helvetica 14'
FONT_BOLD = 'Helvetica 13 bold'

# GUI DEFINITION
# Function for typing simulation effect
def simulate_typing(response):
    # Separate response in words
    words = response.split()
    # # Print words with delay of 0.05 seconds
    for word in words:
        for i in word:
            text_widget.insert(END, i)
            text_widget.update()
            time.sleep(0.05)
        text_widget.insert(END, ' ')
        text_widget.update()
    text_widget.insert(END, '\n')
    text_widget.update()


# Function to print full list
def print_list(response):
    # Separate response in words
    text_widget.insert(END, response)
    text_widget.insert(END, '\n')
    text_widget.update()


# Function to send the user response
def send_response():
    msg = msg_entry.get()
    insert_message(msg, 'You')


def insert_message(msg, sender):
    if not msg:
        return

    user_input = msg_entry.get()
    question_list = str(user_input).split(',')
    try:
        option = question_list[0]
        question = question_list[1]
    except:
        question = user_input
        option = ''

    msg_entry.delete(0, END)
    msg_user = f'{sender}: {msg}' + '\n'  # Actual message to display

    text_widget.configure(state=NORMAL)  # Temporary enablement of the text area to insert the message
    text_widget.insert(END, msg_user)  # Put the message within the text area
    text_widget.configure(state=DISABLED)  # Disablement of the text area after the message insert

    text_widget.configure(state=NORMAL)  # Temporary enablement of the text area to insert the message
    text_widget.insert(END, 'Mykobot: ')

    # LOGIC
    # Including simulate typing in bot response
    final_response = get_response(question, option)
    if final_response != 'OPTION':
        simulate_typing(final_response)
    else:
        text = 'I\'m not yet trained to answer this but don\'t worry I\'ve prepared a list of topics for you, ' \
               'just write the number of the category'
        simulate_typing(text)
        # Show list with type of process
        process_list = get_process_list()
        for topic_sublist in process_list:
            print_list(topic_sublist[0] + '-' + topic_sublist[1])
        text_widget.see(END)
        text_widget.insert(END, 'Mykobot: ')
        text = 'Please, remember. Nowadays, I\'m only ' \
               'able to talk about its ' \
               'Description, ' \
               'Prerequisites, ' \
               'Documents required, ' \
               'Forms, Fees, ' \
               'Related Laws, ' \
               'Average time and ' \
               'Responsible Authorities'
        simulate_typing(text)
        text_widget.see(END)
        text = 'Please, remember. Add your question with this format Number, Question'
        simulate_typing(text)
        text_widget.see(END)

    text_widget.configure(state=DISABLED)  # Disablement of the text area after the message insert
    text_widget.see(END)

# Setting up the GUI window
window = Tk()
window.title('Mykobot')

# MAIN WINDOW
window.resizable(width=False, height=False)
window.configure(width=800, height=600, bg=BG_COLOR)
head_label = Label(window, bg=BG_COLOR, fg=TEXT_COLOR, text='Welcome to Mykobot', font=FONT_BOLD, pady=10)
head_label.place(relwidth=1)

# DIVIDER AREA
line = Label(window, width=880, bg=BG_GRAY)
line.place(relwidth=1, rely=0.07, relheight=0.012)

# TEXT WIDGET
text_widget = Text(window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
text_widget.configure(cursor='arrow', state=DISABLED)

# SCROLL BAR
scrollbar = Scrollbar(text_widget)
scrollbar.place(relheight=1, relx=0.974)
scrollbar.configure(command=text_widget.yview)

# BOTTOM LABEL
bottom_label = Label(window, bg=BG_GRAY, height=80)
bottom_label.place(relwidth=1, rely=0.825)

# MESSAGE ENTRY BOX
msg_entry = Entry(bottom_label, bg=BG_ENTRY_COLOR, fg=TEXT_COLOR, font=FONT)
msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
msg_entry.focus()  # To set focus on the component once the app start
msg_entry.bind('<Return>', lambda e: send_response())  # To send the message using ENTER

# SEND BUTTON
send_button = Button(bottom_label, text='Send', font=FONT_BOLD, width=20, bg=BG_GRAY, command=lambda: send_response())
send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

# Show the window using tkinter mainloop
window.mainloop()