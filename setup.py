try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import threadimages

config = {
    'description': 'image downloader',
    'version': threadimages.__version__,
    'license': threadimages.__license__,
    'url': 'https://github.com/zeev0/thread-images',
    'download_url': 'https://github.com/zeev0/thread-images',
    'version': '1.0',
    'scripts':['bin/thread-images'],
    'packages': ['threadimages'],
    'name': 'thread-images'
}

setup(**config)
