<p align="center">
  <img width="497" alt="Mykobot" src="https://user-images.githubusercontent.com/51316424/229366164-5d0d1244-4779-4422-bb42-c68a0f2e2609.png">
</p>

# Myko_Bot: personal NLP-powered Guide to navigating the Visa Application Process in Berlin!

### Business Goal Definition
ChatBots become increasingly integrated into daily life and public discourse. The idea of Mykobot is based on the well-known challenges and complexities during the visa application process in Berlin. While the www.berlin.de offers public available information on the subject, it can be a time-consuming and frustrating task for users to sift through and find the specific details relevant to their individual case. Therefore, an automated ChatBot that assist users with the entire Visa Application Process has been necessary for a long time.

### Main Features
The main features and/or characteristics of Mykobot are defined based on following:

1. identifying the end users or stakeholders
2. defining the aim of the Mykobot based on business goals
3. determination of whether it should learn or remain stable
4. identification of the type of data being used
5. structuring, locating and processing data
6. creation of user-friendly frontend

As a result default conditions for Mykobot include the use of text data, stability of the data without changes over time, minimal need for a learning process from previous interactions (NLP & ML), accurate responses due to predefined context and entities, and the ability to switch to AI-based models for more complex queries.

### Workflow
Following an assessment of the advantages and limitations, a workflow diagram was created:
![workflow](https://user-images.githubusercontent.com/51316424/229366152-cb2f8b36-8f58-41c3-91cc-a8bba4149b01.jpg)

### Libraries / Requirements
-- Data_Definition / Data_Translation / Data_Preprocessing

conda install python=3.7

conda install -c anaconda nltk

conda install -c anaconda beautifulsoup4

conda install -c anaconda lxml

conda install -c anaconda requests

pip install spacy==2.3.5

python -m spacy download en

-- Mykobot: for creation of chatterbot

pip install chatterbot

pip install chatterbot-corpus

-- Additional Steps: for creation of additional YAML file within chatterbot-corpus

pip install deep-translator

pip install PyYAML (PyYAML 6.0. Please note, that chatterbot-corpus 1.2.0 requires PyYAML<4.0)

### Tech Stack
The Tech Stack for this project includes Python, Postgres, PyCharm, GitHub, and Tableau.

Python and several libraries were mainly used in this project. The Chatterbot library was used for creating a conversational AI chatbot, while the Pillow library was used for some interface image processing. The BeautifulSoup library utilizedfor web scraping, requests for making HTTP requests to APIs and Spacy was utilized for natural language processing. Additionally, Tkinter library was implemented for creation of a graphical user interface (GUI), which enables users to interact with the application.

For data storage and management, Postgres was used as the open-source relational database management system. PyCharm, an integrated development environment (IDE) for Python, was used for coding, debugging, and testing. Code management and version control were done with GitHub and finally Tableau was used for interactive presentation of the project.

### Future Implementations
The next steps involve the implementation and integration of Selenium to enable automatic yearly data retrieval. Furthermore, visual interface of the web application should be refined and improved using Flask or Streamlit. Additionally, it is planned to add corresponed web links and pdf file download options within the interface. This can be complemented by the development of a chat tool that will be linked to a database containing contact information of volunteer visa application supporters, as well as a booking function for appointments. Finally, TensorFlow and Deep Learning should be integrated to enhance and improve the quality of the Mykobot conversations.

### Appendix
https://chatterbot.readthedocs.io/en/stable/index.html

https://realpython.com/build-a-chatbot-python-chatterbot/

https://pypi.org/

https://pypi.org/project/ChatterBot/

https://github.com/gunthercox/chatterbot-corpus

https://github.com/gunthercox/ChatterBot

https://spacy.io/api/doc

https://www.netomi.com/best-ai-chatbot

https://openai.com/blog/chatgpt

https://anaconda.org/anaconda

https://docs.python.org/3/library/tkinter.html
