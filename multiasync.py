"""
Image downloader that uses multiprocessing and async.
"""
import requests
import time
import multiprocessing
import asyncio
from PIL import Image
from io import BytesIO
from pars import parser


start_time = time.time()


async def download_image(url: str):
    try:
        req = requests.get(url)
        img = Image.open(BytesIO(req.content))
        img.save(url.split('/')[-1])
        print(f"Downloaded from url - {url}\n"
              f"In {time.time() - start_time:.2f} seconds")
    except Exception as e:
        print(f"Exception: {e}\nURL: {url}")


async def multiproceamain(urls: list[str]):
    manager = multiprocessing.Manager()
    queue = manager.Queue()
    
    for url in urls:
        task = asyncio.create_task(download_image(url))
    
    


if __name__ == "__main__":
    urls = parser.parse_args().urls
    try:
        loop = asyncio.get_running_loop()
    except:
        loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(multiproceamain(urls))
    except KeyboardInterrupt:
        pass
    print(f"Program downloaded all images in {time.time() - start_time:.2f}")
    