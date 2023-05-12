import time
import os

def show_logs():
    print('-------------------------------------------------')
    logs_directory = './output'
    for filename in os.listdir(logs_directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(logs_directory, filename)
            with open(file_path, 'r') as f:
                file_content = f.read()
            print('Log name:', filename)
            print('Log content:\n', file_content)

while True:
    show_logs()
    time.sleep(20)
