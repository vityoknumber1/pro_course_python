import os
import threading
from multiprocessing import Process
from time import perf_counter, sleep

import requests


# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    start = perf_counter()
    image_url = "https://vgorode.ua/img/article/3938/12_main-v1573686449.jpg"
    print(f"Processing image from {image_url} in process {os.getpid()}")
    sleep(5)
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]
    encryption_counter = perf_counter() - start
    print(f"Time taken for encryption task: {encryption_counter}")


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    start = perf_counter()
    print(
        f"Downloading image from {image_url} in"
        f"thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    download_counter = perf_counter() - start
    print(f"Time for I/O-bound task: {download_counter}")


if __name__ == "__main__":
    start = perf_counter()
    link = "https://vgorode.ua/img/article/3938/12_main-v1573686449.jpg"
    try:
        p1 = Process(target=encrypt_file, args=("path/to/file",))
        p2 = Process(
            target=download_image,
            args=(link,),
        )
    except Exception as e:
        print(f"Error occured: {e}")
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    time_total = perf_counter() - start
    print(f"Time taken for Total: {time_total} seconds")
