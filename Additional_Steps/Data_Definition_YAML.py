"""

This code is a Python script for Webscraping the visa types from www.berlin.de, following by creation of YAML file per visa type.
It uses BeautifulSoup, requests and other libraries from Settings.py, Category_Files.py and Cleaning_Method.py.

After definition of section titles it runs a for loop over the categories and visa types with corresponded lists and items.
Next is extracts specific section from each visa type and send saves the information in YAML files located in visas_germany folder.

"""

# REQUIRED LIBRARIES
from bs4 import BeautifulSoup
import requests
import yaml

# VARIABLE INITIALITATION
# Section titles for extract information from each visa type page.
SECTION_TITLES = ['voraussetzungen', 'erforderliche_unterlagen', 'formulare', 'gebuehren', 'rechtsgrundlagen',
                  'bearbeitungszeit',
                  'weiterfuehrende_informationen', 'wohin']

# INITIAL WEBSITE LOOP
# Fetch the webpage HTML code
url = 'https://www.berlin.de/einwanderung/termine/unsere-dienstleistungen/artikel.873415.php'
response = requests.get(url)
html = response.text
# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# Page Content
content = soup.find('div', class_='html5-section body')

# CREATION OF YML FILE
def create_category_file(file_name, data):
    with open('./visas_germany/' + file_name + '.yml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

# ADDITIONAL Q&A
# Add more conversations with questions and answers to existing files
def add_conversation(file_name, conversation):
    # Load Existing File
    with open('./visas_germany/' + file_name + '.yml', 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    # Add new conversation
    data['conversations'] += conversation

    # Update file
    with open('./visas_germany/' + file_name + '.yml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)


file_counter = 0
category_file_data = {}
# VISA WebSites
# Extraction of information from each visa types that goes through categories, visas, lists and item
# Categories
for category in content.find_all('div', class_='html5-section body'):
    for visa in category.find_all('div', class_='textile'):
        for listVisa in visa.find_all('ul'):
            for item in listVisa.find_all('li'):
                try:
                    URL = 'https://www.berlin.de' + item.a['href'] + 'en/'

                    # WEBSITE LINK
                    source = requests.get(URL).text

                    contentTitle = ""
                    contentDescription = ""

                    # COMPLETE PAGE
                    soup = BeautifulSoup(source, 'lxml')

                    # PAGE CONTENT
                    contentVisa = soup.find('div', class_='html5-section article')

                    # TITLE
                    contentTitle = contentVisa.find('div', class_='html5-header header').h1.text.upper()

                    # DETAILS
                    contentDetails = contentVisa.find('div', class_='body dienstleistung')

                    # VISA DESCRIPTION
                    contentDescription = contentDetails.find('div', class_='block').text.strip()

                    # VARIABLE DEFINITION
                    pageName = contentTitle
                    context = pageName
                    descriptionVisa = contentDescription
                    question = ''
                    answer = ''

                    # Create File per Visa Type (Process)
                    file_counter = file_counter + 1
                    category_file_name = "Process_" + str(file_counter)

                    # ADD TAG DESCRIPTION
                    tag_name = "Description"
                    # QUESTION
                    question = "Tell me something about " + pageName
                    answer = descriptionVisa

                    category_file_data = {
                        'category': [context],
                        'conversations': [
                            [question, answer]
                        ]
                    }

                    create_category_file(category_file_name, category_file_data)

                    # VARIABLE INITIALIZATION
                    tag_name = ''
                    question = ''
                    answer = ''

                    # SECTIONS
                    for title in SECTION_TITLES:
                        for section in contentDetails.find_all('div', class_='block'):
                            # Section Title
                            try:
                                sectionTitle = section.find('h2', id=title).text
                                tag_name = sectionTitle
                                question = "Tell me something about " + tag_name
                            except Exception as e:
                                sectionTitle = 'NONE'

                            if sectionTitle != 'NONE':
                                # SECTION DETAILS
                                try:
                                    sectionDetails = section.text.replace(sectionTitle, '').strip()
                                    answer = sectionDetails
                                except Exception as e:
                                    sectionDetails = 'NONE'

                        conversation = [[question, answer]]
                        add_conversation(category_file_name, conversation)

                except Exception as e:
                    print(URL + " an exception occurred" + str(e))

