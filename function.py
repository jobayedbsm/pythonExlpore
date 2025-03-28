# userAuth
class userAuth(username,password):
    def __init__(self):
        self.user={
            'username': 'jobayed'
        }
    def login(self,username,password):
        if username in self and self[username]==password:
            print('login successfully')
    def register(self,username,password):
        pass
    
    def resetPassword(self,username,password):
        if username in self.user:
            self['username']=password

users=userAuth()
userAuth.login('jobayed','hossen')