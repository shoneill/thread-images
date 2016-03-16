#!/usr/bin/python

import urllib.request
import os
import time
from sys import argv,exit

IMG_MARKER = "href=\"//i.4cdn.org/"
URL_START  = "\"//"

def extractURL(str_input):
    extracted_url = ""
    index = str_input.find(URL_START) + len(URL_START)
    for i in range(index, len(str_input) - 1):
        extracted_url += (str_input[i])
    return extracted_url

def dupe(fragment, imgs):
    if fragment in imgs:
        return True
    return False

def process(fragment, imgs):
    if IMG_MARKER in fragment:
        extracted = extractURL(fragment)
        if not dupe(extracted,imgs):
            imgs.append(extracted)

def download(img,directory):
    print("Downloading " + img)
    os.system("wget -q -P " + directory + " " + img)

def main():
    
    url = ""
    directory = ""
    imgs = []

    if len(argv) == 2:
        url = argv[1]
        directory = time.strftime("%H%M%S")
    elif len(argv) == 3:
        directory = argv[1]
        url = argv[2]
    else:
        print("Incorrect format. see README")
        exit(1)
    
    html = urllib.request.urlopen(url).read().decode().split()
    for fragment in html:
        if IMG_MARKER in fragment:
            process(fragment,imgs)

    for img in imgs:
        download(str(img),directory)

if __name__ == "__main__":
    main()
