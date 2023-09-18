"""
Image downloader that uses threading.    
"""

import threading
import time
import requests
from PIL import Image
from io import BytesIO
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


def thmain(urls: list[str]):
    threads = []
    
    for url in urls:
        thread = threading.Thread(target=download_image, args=[url])
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Program downloaded all images in {time.time() - start_time:.2f}")


if __name__ == "__main__":
    args = parser.parse_args()
    thmain(args.urls)
 