import time
import os


t = int(input("Enter Time in seconds! "))
while t:
    os.system('clear')
    mins, secs = divmod(t, 60)
    print('{}:{}'.format(mins , secs))
    time.sleep(1)
    t -= 1
print("Time's Up!")