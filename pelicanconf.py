#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PROFILE_IMAGE = 'profile.jpeg'
AUTHOR = 'Wayne J. Lee'
SITENAME = 'waynejlee @ S7RAY'
SITEURL = ''

STATIC_PATHS = ['images']

THEME = 'themes/pelican-hyde'

PATH = 'content'

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

BIO = "Wayne J. Lee | OSCP | Microsoft Certified Azure Administrator | BizDev & Tech Specialist @ Vigilant Asia"

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/wayneL_'),
          ('linkedin', 'https://linkedin.com/in/waynejlee'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
