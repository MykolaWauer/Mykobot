"""

This code is a Python script for translation of German text to English.
It uses deep_translator and nltk libraries.

Thereby German text is splitted into sentences before translation.
Afterwords English translated is joined back.

"""

from deep_translator import GoogleTranslator
from nltk.tokenize import sent_tokenize


def preprocess_text(text, source_lang, target_lang):
    # SPLIT TEXT INTO SENTENCES
    sentences = sent_tokenize(text, language=source_lang)

    # VARIABLE INITIALIZATION
    translated_sentences = []

    # TRANSLATE
    for sentence in sentences:
        translated_sentence = GoogleTranslator(source=source_lang, target=target_lang).translate(sentence)
        translated_sentences.append(translated_sentence)
        print(f"Translated sentence: {sentence} -> {translated_sentence}")

    # JOIN TRANSLATED TEXT
    translated_text = ' '.join(translated_sentences)
    return translated_text


with open("Visa_types.csv", "r") as text_file:
    german_text = text_file.read()
    source_lang = 'german'
    target_lang = 'en'
    german_text = preprocess_text(german_text, source_lang, target_lang)

with open("Visa_types_translated.txt", "w") as output_file:
    output_file.write(german_text)