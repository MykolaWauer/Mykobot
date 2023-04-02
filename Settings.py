'''

This code is a definition of settings which would be used in the following Python script
for data collection and definition.

'''

# Array with the title of the sections within the website.
SECTION_TITLES = ['voraussetzungen', 'erforderliche_unterlagen', 'formulare', 'gebuehren', 'rechtsgrundlagen',
                  'bearbeitungszeit', 'weiterfuehrende_informationen', 'wohin']
# Website root URL to extract the information
ROOT_WEBSITE_URL = 'https://www.berlin.de'
# Main website to identify the list of process with in the org
MAIN_WEBSITE_URL = 'https://www.berlin.de/einwanderung/termine/unsere-dienstleistungen/artikel.873415.php'
# Process_Data path to save the information of the processes
FINAL_FILE_PATH = './Process_Data/Topics/Conversations.json'


