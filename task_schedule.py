# A reminder to Join my church vigil on DSTV Channel 349 every second saturday by 12:12 am.
import schedule
import time
import datetime

# Define a function to perform a task
# task1 = A reminder to Join my church vigil on DSTV Channel 349 every second saturday by 12:12 am.
def task1():
    today = datetime.datetime.today()
    if 8 <= today.day <= 14:
        print('We are Live now! Switch to channel 349 to join the vigil..')

# task2 = A reminder to call people to join
def task2():
    today = datetime.datetime.today()
    if 8 <= today.day <= 14:
        print('Call David and the rest to join the vigil.')

# task3 = Don't forget to write  down your prayer requests
def task3():
    today = datetime.datetime.today()
    if 8 <= today.day <= 14:
        print('My prayer requests..')


# Schedule the tasks
schedule.every().saturday.at("00:18").do(task1)
schedule.every().saturday.at("00:20").do(task2)
schedule.every().saturday.at("00:22").do(task3)

# Keep the script running to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)