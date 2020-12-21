#!/usr/bin/env python3
import os
import sys
import requests
import argparse
from tqdm import tqdm
from lxml import html
from urllib.request import urlopen


# todo: не забыть проверить на работоспособность и поправить
class Flibusta:
    '''A script to synchronize daily archives from website Flibusta

    Dependencies:
        * requests - pip install requests --user (mandatory)
        * tqdm - pip install tqdm --user (mandatory)
        * lxml - pip install lxml --user (mandatory)
        * urllib - pip install urllib --user (mandatory)

    Usage: flibusta_daily.py [-h] [-u URL] [-p PATH]

    A script to synchronize daily archives from website Flibusta

    optional arguments:
    -h, --help            show this help message and exit
    -u URL, --url URL     URL address, default: https://flibusta.is/
    -p PATH, --path PATH  The directory in which we will synchronize, default:
                            /tmp/
    '''
    def __init__(self, url, path):
        self.url = url + '/daily/'
        self.path = path
        self.URLS = []

    def download_daily_zip(self, url):
        '''Saving daily archive.

        url - URL daily archive
        '''
        dst = url.split('/')[-1]
        file_size = int(urlopen(url).info().get('Content-Length', -1))

        if os.path.exists(dst):
            first_byte = os.path.getsize(dst)
        else:
            first_byte = 0

        if first_byte >= file_size:
            return file_size

        header = {"Range": "bytes={}-{}".format(first_byte, file_size)}
        pbar = tqdm(
            total=file_size, initial=first_byte,
            unit='B', unit_scale=True, desc=url.split('/')[-1]
        )
        try:
            req = requests.get(url, headers=header, stream=True)
        except requests.exceptions.Timeout:
            print(e)
            sys.exit(1)
        except requests.exceptions.TooManyRedirects:
            print(e)
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        with(open(self.path + dst, 'ab')) as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    pbar.update(1024)

        pbar.close()

        return file_size

    def get_daily_links(self,):
        try:
            resp = requests.get(self.url).text
        except requests.exceptions.Timeout:
            print(e)
            sys.exit(1)
        except requests.exceptions.TooManyRedirects:
            print(e)
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        try:
            links = html.fromstring(resp).xpath('//a')
        except Exception as e:
            return '', ''

        for link in links:
            for k, v in link.items():
                self.URLS.append(self.url+v)

    def update_local_library(self,):
        self.get_daily_links()
        sys.stderr.write("\x1b[2J\x1b[H")

        for i in tqdm(self.URLS):
            self.download_daily_zip(i)

        sys.stdout.flush()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A script to synchronize daily archives from website Flibusta')
    parser.add_argument('-u', '--url', dest='url', help='URL address, default: https://flibusta.is/', default='https://flibusta.is/')
    parser.add_argument('-p', '--path', dest='path', help='The directory in which we will synchronize, default: /tmp/', default='/tmp/')

    args = parser.parse_args()
    try:
        if args.path is None:
            print('You did not specify a directory to sync')
            sys.exit(-1)

        flibusta = Flibusta(args.url, args.path)
        flibusta.update_local_library()
    except KeyboardInterrupt:
        print('You interrupted program execution, see you soon ;-)')
        sys.exit(1)
