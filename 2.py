import datetime
from datetime import timedelta

x = datetime.datetime.now()

print ("Yesterday: " + str(datetime.datetime.now() - timedelta(days = 1)))
print ("Today: " + str(datetime.datetime.now()))
print ("Tomorrow: " + str(datetime.datetime.now() + timedelta(days = 1)))
