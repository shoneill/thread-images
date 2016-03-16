#!/bin/python
#
# mass image downloader for *chans

import subprocess
import os
import urllib.request
import argparse
import time
from html.parser import HTMLParser
from urllib.parse import urlparse
from sys import argv

args = None

class Parser4(HTMLParser):
    def __init__(self):
        self.links = []
        self.base = 'https:'
        super().__init__()

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        try:
            if tag == "a":
                # Check the list of defined attributes.
                if len(attrs) > 1 and attrs[0] == ('class','fileThumb'):
                    self.links.append(self.base+attrs[1][1])
        except:
            pass

class Parser8(HTMLParser):
    def __init__(self):
        self.links = []
        super().__init__()

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                   base = 'https://media.8ch'
                   if base in value[:len(base)] and value not in self.links:
                       self.links.append(value)

class ParserLain(HTMLParser):
    def __init__(self):
        self.links = []
        self.base = "https://lainchan.org"
        super().__init__()

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
            if len(attrs) > 1 and attrs[1] == ('target','_blank'):
                fragment = attrs[0][1]
                if fragment[:4] != 'http':
                    link = self.base + fragment
                    if link not in self.links:
                        self.links.append(link)

class ParserGeneric(HTMLParser):
    def __init__(self):
        self.links = []
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
           for name, value in attrs:
               if name == "href" and \
                  '.jpg' in value or \
                  '.png' in value or \
                  '.gif' in value:
                   if value not in self.links:
                       self.links.append(value)

def main():
    global args
    thread = ""
    directory = c_time = time.strftime("%H%M%S")
    i = 0
    while os.path.isdir(directory):
        directory = c_time + '_' + i
    info = "image downloader for 4chan, 8chan, and lainchan"
    parser = argparse.ArgumentParser(description=info)
    parser.add_argument('-d', '--directory',
                        help='directory for the images',
                        action='store')
    parser.add_argument('thread',
                        help='directory for the images',
                        action='store')
    parser.add_argument('-v', '--verbose',
                        help='directory for the images',
                        action='store_true')
    parser.add_argument('-q', '--quiet',
                        help='directory for the images',
                        action='store_true')
    args = parser.parse_args()
    thread = args.thread
    if args.directory:
        directory = args.directory
        if not args.quiet: print("Found directory:",directory)
    links = parse(thread)
    download(links, directory)

def parse(thread):
    "parse and return list of links"
    parser = None
    parsed_uri = urlparse(thread)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    if "lainchan" in domain:
        if not args.quiet: print("Using Lainchan parser")
        parser = ParserLain()
    elif "8ch" in domain:
        if not args.quiet: print("Using 8chan parser")
        parser = Parser8()
    elif "4chan" in domain:
        if not args.quiet: print("Using 4chan parser")
        parser = Parser4()
    else:
        if not args.quiet: print("Unknown thread. Using generic parser")
        parser = ParserGeneric()
    try:
        page = proper_request(thread)
        parser.feed(str(page))
    except Exception as e:
        print(e)
    return parser.links

def download(links, directory):
    for url in links:
        if args.verbose: print("Downloading " + url + " to " + directory)
        subprocess.call(["wget","-q","-P",directory,url])
        
def proper_request(url):
    "spoofs agent, as to not be declined by the site"
    if not args.quiet: print("Requesting HTML")
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    if data:
        if not args.quiet: print("Recieved response")
    return data

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if not args.quiet: print("Keyboard Interupt found. Exiting...")
        exit()
