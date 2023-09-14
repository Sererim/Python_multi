import argparse
import multiprocessing
import threading
import asyncio



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Program that donwloads images from urls.",
                                     description="Downloads all images from the url and saves it on the machine",
                                     epilog="Please enter a valid url with an image in it. All popular image formats are supported.")
    parser.add_argument('url', type=str, nargs="*", help="Enter valid urls to images. All images will be saved with their url names in the directory where program is.")
    args = parser.parse_args()
    