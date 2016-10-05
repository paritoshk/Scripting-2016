from __future__ import print_function
import os
import sys
import re
import readline
import eyed3
from bs4 import BeautifulSoup
import requests
import sys

if (sys.version_info > (3, 0)):
    from urllib.parse import quote_plus as qp
    raw_input = input
    unicode = str
else:
    from urllib import quote_plus as qp

def extract_videos(html):
    soup = BeautifulSoup(html, 'html.parser')
    pattern = re.compile(r'/watch\?v=')
    found = soup.find_all('a', 'yt-uix-tile-link', href=pattern)
    return [(x.text.encode('utf-8'), x.get('href')) for x in found]

def makeRequest(url, hdr):
    http_proxy  = os.environ.get("HTTP_PROXY")
    https_proxy = os.environ.get("HTTPS_PROXY")
    ftp_proxy   = os.environ.get("FTP_PROXY")

    proxyDict = { 
        "http"  : http_proxy,
        "https" : https_proxy,
        "ftp"   : ftp_proxy
        }

    req = requests.get(url, headers=hdr, proxies=proxyDict)
    return req

def list_movies(movies):
    for idx, (title, _) in enumerate(movies):
        yield '{} - {}'.format(idx, title.decode('utf-8').encode(sys.stdout.encoding))

def search_videos(query):
    response = makeRequest('https://www.youtube.com/results?search_query=' + query, {})
    return extract_videos(response.content)

def query_and_download(search, has_prompts=True, is_quiet=False):    
    if not is_quiet:
        print('Searching...')

    available = search_videos(search)

    if not is_quiet:
        if not available:
            print('No results found matching your query.')
            sys.exit(2)
        else:
            if has_prompts:
                print('Found:', '\n'.join(list_movies(available)))
    return 'temp string'

def main():
    argument_string = ' '.join(sys.argv[1:])
    search = ''

    # to avoid empty inputs
    if not sys.argv[1:]:
        while search == '':
            search = raw_input('Enter query\n')
        search = qp(search)
        downloaded = query_and_download(search)

if __name__ == '__main__':
    main()