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