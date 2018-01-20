#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nick Timkovich'
SITENAME = 'Nick\'s Solutions'
SITETITLE = 'Nick\'s Solutions'
SITESUBTITLE = 'Fixing things, broken or not.'
SITEDESCRIPTION = 'asf'
SITEURL = 'https://nick.solutions'

SITELOGO = '/images/profile.jpg'

PATH = 'content'
THEME = 'theme'

#BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = '2016-2017'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    # ('Pelican', 'http://getpelican.com/'),
    # ('Python.org', 'http://python.org/'),
    # ('Jinja2', 'http://jinja.pocoo.org/'),
    # ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('linkedin', 'https://linkedin.com/in/nicktimkovich'),
    ('github', 'https://github.com/nicktimko'),
    ('twitter', 'https://twitter.com/nicktimko'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
