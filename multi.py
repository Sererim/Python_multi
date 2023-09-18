"""
Image downloader that uses multiprocessing and threading⌈.
"""
import time
import requests
import concurrent.futures
from PIL import Image
from io import BytesIO
from multiprocessing import Process
from pars import parser


start_time = time.time()


def download_image(url: str):
    try:
        req = requests.get(url)
        img = Image.open(BytesIO(req.content))
        img.save(url.split('/')[-1])
        print(f"Downloaded from url - {url}\n"
              f"In {time.time() - start_time:.2f} seconds")
    except Exception as e:
        print(f"Exception: {e}\nURL: {url}")


def thread_tasks(urls: list[str]):
    with concurrent.futures.ThreadPoolExecutor() as exe:
        exe.map(download_image, urls)


def process_task(url_chunks):
    
    processes = []
    
    for urls in url_chunks:
        proc = Process(target=thread_tasks, args=(urls, ))
        processes.append(proc)
        proc.start()
    
    for proc in processes:
        proc.join()
    
    print(f"Program downloaded all images in {time.time() - start_time:.2f}")
    


if __name__ == "__main__":
    urls = parser.parse_args().urls
    url_chunks = [urls[i:i + 5] for i in range(0, len(urls), 5)]
    process_task(url_chunks)
