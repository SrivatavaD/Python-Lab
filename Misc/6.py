import threading
import time

#indicated some tasks being alone
def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

time1 = time.perf_counter()   
# normal code
# func(4)
# func(2)
# func(1)


# same code using threads
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()

# calculating time
time2 = time.perf_counter()
print(time2 - time1)

# use of concurrent.futures 
import concurrent.futures
import time

def task(name, seconds):
    print(f"{name} started")
    time.sleep(seconds)
    print(f"{name} completed")
    return f"{name} result"

with concurrent.futures.ThreadPoolExecutor() as executor:
    future1 = executor.submit(task, "task1", 3)
    future2 = executor.submit(task, "task2", 2)

    print(future1.result())
    print(future2.result())



import concurrent.futures
import time

def download_file(name, seconds):
    print(f"Downloading {name}")
    time.sleep(seconds)
    return f"{name} downloaded"

files = [
    ("photo.png", 3),
    ("song.mp3", 2),
    ("notes.txt", 1),
]

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []

    for file_name, seconds in files:
        future = executor.submit(download_file, file_name, seconds)
        futures.append(future)

    for future in futures:
        print(future.result())


