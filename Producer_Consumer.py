import threading
import time
import random

# Shared memory variables
BUFFER_SIZE = 5
buffer = []
in_index = 0
out_index = 0

# Declaring semaphores
mutex = threading.Semaphore()
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)

# Producer Thread Function
def producer():
    global buffer, in_index
    
    for i in range(10):
        item = random.randint(1, 100)
        empty.acquire()
        mutex.acquire()
        
        buffer.append(item)
        in_index = (in_index + 1) % BUFFER_SIZE
        print(f'Producer produced item: {item}')
        
        mutex.release()
        full.release()
        
        time.sleep(random.random())

# Consumer Thread Function
def consumer():
    global buffer, out_index
    
    for i in range(10):
        full.acquire()
        mutex.acquire()
        
        item = buffer[out_index]
        out_index = (out_index + 1) % BUFFER_SIZE
        print(f'Consumer consumed item: {item}')
        buffer.remove(item)
        
        mutex.release()
        empty.release()
        
        time.sleep(random.random())

# Creating Threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Starting Threads
producer_thread.start()
consumer_thread.start()

# Waiting for threads to complete
producer_thread.join()
consumer_thread.join()
