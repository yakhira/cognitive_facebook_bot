import fbchat

class facebook(fbchat.Client):
    def __init__(self, email, password, debug=True, user_agent=None):
        self.author_id   = None
        self.author_name = None
        self.message     = None

        fbchat.Client.__init__(self, email, password, debug, user_agent)
    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid)
        self.markAsRead(author_id)
         
        self.author_id   = author_id
        self.author_name = author_name
        self.message     = message 
        self.audio_url   = ''
        
        if len(metadata['delta']['attachments']) > 0:
            if metadata['delta']['attachments'][0]['mimeType'] == 'audio/mpeg':
                self.audio_url =  metadata['delta']['attachments'][0]['mercury']['url']
                self.message   = ''
        self.listening = False
    def wait_for_message(self):
        if self.debug == False:
            print('Waiting for message...')
        self.listen()
    def get_message(self):
        user_info = self.getUserInfo(self.author_id)
        return user_info, self.message, self.audio_url
    def send_message(self, author_id, message):
        if str(author_id) != str(self.uid):
            return self.send(author_id, message)
        return None