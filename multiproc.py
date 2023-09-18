from multiprocessing import Process, Pool
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


if __name__ == "__main__":
    args = parser.parse_args()
    urls: list[str] = args.urls
    processes = []
    
    for url in urls:
        process = Process(target=download_image, args=(url,))
        processes.append(process)
        process.start()
        
    for process in processes:
        process.join()
