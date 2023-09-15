import argparse

parser = argparse.ArgumentParser(prog='Program that downloads images from urls.',
    description='Gets an url.\nExample: exmaple.com/image1.img.',
    epilog=f'Enter a correct url with a correct file extension. All base image foramts are supported', )
parser.add_argument('urls', type=str, nargs="*", help=f'Enter urls.')
