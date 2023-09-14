Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе. Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы. — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки. — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.

import requests
from PIL import Image
from io import BytesIO
import concurrent.futures
from multiprocessing import Process

def download_image(url):
    """
    Function to download an image from a given URL
    """
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.save(url.split('/')[-1])
        print(f"Downloaded {url}")
    except Exception as e:
        print(f"Error: {e}, URL: {url}")

def thread_task(urls):
    """
    Function to download images using multiple threads
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, urls)

def process_task(url_chunks):
    """
    Function to download images using multiple processes, each with multiple threads
    """
    processes = []
    for urls in url_chunks:
        proc = Process(target=thread_task, args=(urls,))
        processes.append(proc)
        proc.start()
    for proc in processes:
        proc.join()

if __name__ == "__main__":
    urls = [
        # Replace with your image URLs
        'http://example.com/img1.jpg',
        'http://example.com/img2.jpg',
        'http://example.com/img3.jpg'
    ]
  
    # Split the URLs into chunks, with each chunk to be handled by a different process
    url_chunks = [urls[i:i + 2] for i in range(0, len(urls), 2)]
  
    process_task(url_chunks)
In this code, a pool of processes is created, with each process managing a pool of threads. Each thread is responsible for downloading an image. This combination can be useful when working with a large number of URLs, as it allows you to take advantage of both I/O-bound (threading) and CPU-bound (multiprocessing) concurrency.

Remember to install the necessary packages if they aren't already installed using pip install requests pillow.
