__title__ = 'django-qartez'
__version__ = '0.6'
__build__ = 0x000006
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'

from django.utils import version

if version.get_version() < 1.9:
    from sitemaps import *
