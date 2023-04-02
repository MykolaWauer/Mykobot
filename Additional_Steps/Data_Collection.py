"""

This code is a Python script for Webscraping the visa types and requirements from www.berlin.de.
It uses BeautifulSoup, requests and csv libraries.

After definition of section titles it runs a for loop over the categories and visa types.
Next is sends get request to corresponding webpage following by data extraction and storage.

"""

# REQUIRED LIBRARIES
from bs4 import BeautifulSoup
import requests
import csv

# VARIABLE INITIALITATION
# Section titles for extract information from each visa type page.
SECTION_TITLES = ['voraussetzungen', 'erforderliche_unterlagen', 'formulare', 'gebuehren', 'rechtsgrundlagen', 'bearbeitungszeit',
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

# CSV OUTPUT
# Creation of csv file with first row of csv with column names VISA, URL, SECTION, and DESCRIPTION.
csv_file = open('Visa_types.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['VISA', 'URL', 'SECTION', 'DESCRIPTION'])

# VISA WebSites
# Extraction of information from each visa types that goes through categories, visas, lists and item
for category in content.find_all('div', class_='html5-section body'):
    for visa in category.find_all('div', class_='textile'):
        for listVisa in visa.find_all('ul'):
            for item in listVisa.find_all('li'):
                # URL name extraction
                URL = 'https://www.berlin.de' + item.a['href']
                pageName = item.a.text.strip()
                print("* " + pageName)

                # Website link
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

                # SECTIONS
                # get request to the current visa type page, extracts its HTML content, and uses BeautifulSoup to find the relevant content, including the title, details, and description.
                for title in SECTION_TITLES:
                    for section in contentDetails.find_all('div', class_='block'):
                        # SECTION TITLE
                        try:
                            sectionTitle = section.find('h2', id=title).text
                        except Exception as e:
                            sectionTitle = 'NONE'

                        if sectionTitle != 'NONE':
                            # SECTION DETAILS
                            try:
                                sectionDetails = section.text.replace(sectionTitle, '').strip()
                            except Exception as e:
                                sectionDetails = 'NONE'

                            csv_writer.writerow([pageName, URL, sectionTitle.upper(), sectionDetails])


# Closing file
csv_file.close()
