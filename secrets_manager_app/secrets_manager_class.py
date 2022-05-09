# "pip install pytz" <-- install this to use timezones (python recommended)
import pytz
from datetime import datetime, timedelta
import time

class secrets_manager():
    def __init__(self, user, passwd):
        # Instance Variables: secret_user, secret_passwd, password_age
        self.user = user
        self.passwd = passwd
        # "time_now" will de erased after initialization
        time_now = datetime.now(tz=pytz.timezone('US/Eastern'))
        self.timeCreated = time_now
        self.passAge = 0

    def set_Passwd(self, passwd):
        self.passwd = passwd
        print("New password has been set for user:", self.user)

    def set_User(self, user):
        self.user = user
        print("New username has been set.")

    def get_User(self):
        return self.user

    def get_Passwd(self):
        return self.passwd

    def get_Age(self):
        past = self.timeCreated
        present = datetime.now(tz=pytz.timezone('US/Eastern'))
        self.passAge = int((present - past).total_seconds())
        return self.passAge

    def view(self, user):
        
        
