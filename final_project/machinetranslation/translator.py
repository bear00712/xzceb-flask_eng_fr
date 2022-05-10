'''
translate text using IBM
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

VERSION='2018-05-01'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VERSION,authenticator=authenticator)
language_translator.set_service_url(url)


def englishToFrench(english_text):
    '''
    translate english text to french
    '''
    #write the code here
    french_translation=language_translator.translate(
        text=english_text , model_id='en-fr').get_result()
    french_text = french_translation['translations'][0]['translation']
    return french_text


def frenchToEnglish(french_text):
    '''
    translate french text to english
    '''
    #write the code here
    eng_translation=language_translator.translate(
        text=french_text , model_id='fr-en').get_result()
    english_text = eng_translation['translations'][0]['translation']
    return english_text
