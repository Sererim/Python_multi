import asyncio
import requests
import time
from PIL import Image
from io import BytesIO
from pars import parser


async def download(url: str):
    try:
        req = requests.get(url)
        img = Image.open(BytesIO(req.content))
        img.save(url.split('/')[-1])
        print(f"Downloaded from url - {url}\n"
              f"In {time.time() - start_time:.2f} seconds")
    except Exception as e:
        print(f"Exception: {e}\nURL: {url}")


async def main(urls: list[str]):
    tasks = []
    
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f"Program downloaded all images in {time.time() - start_time:.2f}")

start_time = time.time()

if __name__ == "__main__":
    args = parser.parse_args()
    try:
        loop = asyncio.get_running_loop()
    except:
        loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main(args.urls))
    except KeyboardInterrupt:
        pass
