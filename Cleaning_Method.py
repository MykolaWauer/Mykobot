"""

This code is a Python script for preprocessing and/or cleaning the text data that is used
within process_name in Conversations.

"""

import re
from nltk.corpus import stopwords

# Method to clean data
def clean_data(text):
    # Remove special characters and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())

    # Remove unnecessary whitespace
    text = text.strip()

    # Remove line breaks
    text = re.sub(r'\n+', '.', text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in text.split() if word not in stop_words]
    text = ' '.join(words)

    return text
