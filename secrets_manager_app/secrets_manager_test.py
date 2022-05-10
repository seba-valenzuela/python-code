# "pip install pytz" <-- install this to use timezones (python recommended)
import pytz
from datetime import datetime, timedelta
import time
from secrets_manager_class import secrets_manager

print()

past = datetime.now(tz=pytz.timezone('US/Eastern'))
# Wait 5 seconds
time.sleep(5)

present = datetime.now(tz=pytz.timezone('US/Eastern'))

diff_mins = int((present-past).total_seconds() / 60)
diff_sec = int((present-past).seconds)


print(diff_mins)
print(diff_sec)

# TEST
# secret = secrets_manager()     
# print()
# time.sleep(3)
# print(secret.get_Age())
# print()

print("   ** View a Secret **")
print("Type 'r' to look up by Ref. Number,")
action2 = input("or 'u' to look up by Username:")
action2 = action2.lower() # force lowercase
action2 = action2[0] # select only the 1st character
if action2 != 'r' or 'u':
    print("   Wrong option, try again.")