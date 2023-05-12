import time
import datetime

def log(time):
    filename = str(time).replace(':', '_')
    with open(f'./output/{filename}.txt', 'w+') as f:
        f.write(time + '\n')

while True:
    log(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(10)