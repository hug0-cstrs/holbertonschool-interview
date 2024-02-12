#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000): # 10k lines
    sleep(random.random()) # random sleep to simulate a real-world scenario
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format( # random IP, date, HTTP method and status code
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(), # current date and time
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]), # random status code
        random.randint(1, 1024) # random file size
    ))
    sys.stdout.flush() # flushes the buffer
