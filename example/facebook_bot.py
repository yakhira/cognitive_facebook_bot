import sys
import signal

from watson_cognitive_facebook_bot import watson_conversation
from watson_cognitive_facebook_bot import watson_tone_analizer
from watson_cognitive_facebook_bot import watson_speach_to_text
from watson_cognitive_facebook_bot import facebook

__author__ = 'Ruslan Iakhin'

CONVERSATION_IBM_USERNAME = ''
CONVERSATION_IBM_PASSWORD = ''
CONVERSATION_IBM_WORKSPACE= ''

TONEANALIZER_IBM_USERNAME = ''
TONEANALIZER_IBM_PASSWORD = ''

SPEECHTOTEXT_IBM_USERNAME = ''
SPEECHTOTEXT_IBM_PASSWORD = ''

FACEBOOK_EMAIL    = ''
FACEBOOK_PASSWORD = ''

def main(argv):
    response     = {}
    conversation = {}
    
    toneanalizer = watson_tone_analizer(TONEANALIZER_IBM_USERNAME, TONEANALIZER_IBM_PASSWORD)
    speachtotext = watson_speach_to_text(SPEECHTOTEXT_IBM_USERNAME, SPEECHTOTEXT_IBM_PASSWORD)
    
    user_interface = facebook(FACEBOOK_EMAIL, FACEBOOK_PASSWORD, debug=True)

    while True:
        user_interface.wait_for_message()
        user_info, message, audio_url = user_interface.get_message()
        
        if audio_url != '':
            speachtotext.set_audio_from_url(audio_url)
            message = speachtotext.watson_speach_to_text_service()

        if user_info['id'] not in conversation:
            conversation[user_info['id']] = watson_conversation(CONVERSATION_IBM_USERNAME, CONVERSATION_IBM_PASSWORD, CONVERSATION_IBM_WORKSPACE)
            response[user_info['id']] = conversation[user_info['id']].watson_conversation_service('')
  
        conversation[user_info['id']].set_context('tone', toneanalizer.watson_tone_analizer(message))
        conversation[user_info['id']].set_context('username', user_info['firstName'])
        response[user_info['id']] = conversation[user_info['id']].watson_conversation_service(message)
        user_interface.send_message(user_info['id'], response[user_info['id']])

if __name__ == '__main__':
    signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))
    main(sys.argv)
