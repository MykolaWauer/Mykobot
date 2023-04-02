"""

This code is a Python script for Webscraping visa types from www.berlin.de, following by creation of JSON file per visa type.
It uses BeautifulSoup, requests and other libraries from Settings.py, Category_Files.py and Cleaning_Method.py.

After definition of section titles it runs several for loops over the categories and visa types
with corresponded lists and items. Next is extracts specific section from each visa type, applies the predefined cleaning method
and saves the information in JSON files located in Process_Data folder.

"""

# REQUIRED LIBRARIES
from bs4 import BeautifulSoup
import requests
import re

# IMPORT REFERENCES
from Settings import SECTION_TITLES, MAIN_WEBSITE_URL, ROOT_WEBSITE_URL
from Category_Files import add_process, add_tag
from Cleaning_Method import clean_data


# Function to clean tags with predefined definition
def clean_tag(tag_name):
    tag = ''
    if tag_name == 'documents required':
        tag = 'document'
    elif tag_name == 'legal basis':
        tag = 'law'
    elif tag_name == 'average time process request':
        tag = 'law'
    elif tag_name == 'information':
        tag = 'additional'
    elif tag_name == 'responsible authorities':
        tag = 'authority'
    elif tag_name == 'prerequisites':
        tag = 'prerequisite'
    elif tag_name == 'fees':
        tag = 'fee'
    elif tag_name == 'forms':
        tag = 'form'
    else:
        tag = tag_name
    return tag

# WEB SCRAPING
# Fetch the webpage HTML code
main_website_source = requests.get(MAIN_WEBSITE_URL).text
# Parse the HTML code using BeautifulSoup
soupAmt = BeautifulSoup(main_website_source, 'lxml')
# Page Content
content = soupAmt.find('div', class_='html5-section body')  # Page Content identification

# VISA WEBSITES
# Extraction of information from each visa types that goes through categories, visas, lists and item
for category in content.find_all('div', class_='html5-section body'):
    for visa in category.find_all('div', class_='textile'):
        for listVisa in visa.find_all('ul'):
            for item in listVisa.find_all('li'):
                try:
                    # Variable initialization for each type of visa process
                    contentTitle = ''  # Page name
                    contentDescription = ''  # Description for each type of visa process
                    question = ''  # Content of the initial training question
                    answer = ''  # Content from to website to answer the question

                    # WEBSITE STRUCTURE
                    URL = ROOT_WEBSITE_URL + item.a['href'] + 'en/'  # URL definition for each visa process type
                    source = requests.get(URL).text  # Full get information by request website
                    # COMPLETE PAGE
                    soup = BeautifulSoup(source, 'lxml')
                    # PAGE CONTENT
                    contentVisa = soup.find('div', class_='html5-section article')  # Page complete content scrapping
                    # TITLE
                    contentTitle = contentVisa.find('div', class_='html5-header header').h1.text.upper()
                    # DETAILS
                    contentDetails = contentVisa.find('div', class_='body dienstleistung')
                    # VISA DESCRIPTION
                    contentDescription = contentDetails.find('div', class_='block').text.strip()

                    # Add Name and Content dictionary for each section
                    # First add DESCRIPTION based on page structure
                    pageName = clean_data(contentTitle)
                    # Add dictionary topics
                    add_process(pageName, str(item.a['href']).split('/')[5])
                    section_name = clean_data('Description')
                    section_content = re.sub(r'\n+', '.', contentDescription)
                    # Add description conversation
                    question = 'Tell me something about the ' + pageName
                    answer = section_content
                    add_tag(pageName, section_name, question, answer)

                    # Cleaning variable after very first run
                    section_name = ''
                    section_content = ''
                    question = ''
                    answer = ''

                    # SECTIONS
                    # Processing section for each visa type process
                    for title in SECTION_TITLES:
                        for section in contentDetails.find_all('div', class_='block'):
                            # Section Title (name) scrapping
                            try:
                                section_name = section.find('h2', id=title).text
                                section_name = clean_data(section_name)
                            except Exception as e:
                                section_name = 'NONE'
                            if section_name != 'NONE':
                                # Section Details (content) scrapping
                                try:
                                    section_content = section.text.replace(section_name, '').strip()
                                    section_content = re.sub(r'\n+', '.', section_content)
                                except Exception as e:
                                    section_content = 'NONE'

                            # Adding other section for each process (Visa type)
                            if section_name != 'NONE' and section_content != 'NONE':
                                question = 'Tell me about the ' + section_name + ' for ' + pageName
                                answer = section_content
                                add_tag(pageName, clean_tag(section_name), question, answer)

                except Exception as e:
                    print(URL + " an exception occurred" + str(e))


