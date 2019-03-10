import asyncio
import threading
import time

def sleep1():
    print('hello')
    time.sleep(2)
    print('world')


threading._start_new_thread(sleep1)

time.sleep(4)