#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Flávia Lopes'
AUTHOR_CARD = {
    'title': 'Back-end Developer',
    'text': 'Interessada em Ciência de Dados, Código limpo, TDD, Python'
}

SITENAME = 'Flávia Lopes .Dev'
SITEURL = ''
RELATIVE_URLS = True

### adicionado ###
SITESUBTITLE = ''
SITEDESCRIPTION = 'Blog Pessoal.'
BLOGKEYWORDS = ['python','python developer', 'web', 'pelican', 'github pages' 'data science', 'github','portfolio']
### fim adicionado ###

PATH = 'content'
DEPLOY_PATH = 'deploy'

### adicionado ###
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git']
TYPOGRIFY = True
SLUGIFY_SOURCE = 'title'
DATE_FORMATS = {
'en': ('en_US','%a, %d %b %Y'),
'pt': ('pt_BR','%a, %d %B %Y'),
}
DEFAULT_DATE = 'fs'
THEME = 'themes/bootstrap-blog'

#how posts are displayed on home: {1: one-column, 2: two-column, 3: three-column, 4: four-column, 5: featured-posts, 6: full-width}
SWITCH_TEMPLATE = 1

STATIC_PATHS = [
    #'extra/robots.txt',
    'images',
    'notebooks',
    'pdfs',
    'pages']
STATIC_EXCLUDES = ['images/thumbnails']

DEFAULT_CATEGORY = 'python'
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{slug}/index.html'
ARTICLE_LANG_URL =  'posts/{date:%Y}/{date:%b}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{slug}-{lang}/index.html'
DRAFT_URL = 'drafts/{date:%Y}/{date:%b}/{slug}/'
DRAFT_SAVE_AS = 'drafts/{date:%Y}/{date:%b}/{slug}/index.html'
DRAFT_LANG_URL = 'drafts/{date:%Y}/{date:%b}/{slug}-{lang}/'
DRAFT_LANG_SAVE_AS = 'drafts/{date:%Y}/{date:%b}/{slug}-{lang}/index.html'

PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'
DRAFT_PAGE_URL =  'drafts/pages/{slug}.html'
DRAFT_PAGE_SAVE_AS =  'drafts/pages/{slug}.html'
DRAFT_PAGE_LANG_URL = 'drafts/pages/{slug}-{lang}.html'
DRAFT_PAGE_LANG_SAVE_AS = 'drafts/pages/{slug}-{lang}.html'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# Quando True as categorias são geradas conforme a organização das pastas
USE_FOLDER_AS_CATEGORY = True
SUMMARY_MAX_LENGTH = 20

GITHUB_URL = 'http://github.com/FlaviaLopes/'
GOOGLE_ANALYTICS = ''
TWITTER_USERNAME = '_flavialopes_'

REVERSE_CATEGORY_ORDER = True
DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True
COMMENT = True

PROJECTS = (('Genetic Algorithm with Python', 'https://www.github.com/FlaviaLopes/Genetic-Algorithm'),
         ('Acelera Dev Data Science', "https://www.github.com/FlaviaLopes/AceleraDev-Codenation-Data-Science"),
         ('Eleições 2018', "https://www.github.com/FlaviaLopes/Eleicoes-2018"),)

SOCIAL = (('twitter', 'https://twitter.com/_flavialopes_'),
          ('linkedin', 'https://linkedin.com/in/lopesflavia'),
          ('github', 'https://github.com/FlaviaLopes'),
          ('instagram', 'https://instagram.com/_flavialopes_'),
          ('facebook', 'https://facebook.com/flavialopesads'),)

# global metadata to all the contents
DEFAULT_METADATA = {
    'status': 'draft',
    'featured': False,
    'favicon': 'images/favicon.ico',
    'avatarblog': 'images/thumbnails/thumbnail_post/avatar.jpg'
}
LOAD_CONTENT_CACHE = False
# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
### fim adicionado ###

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt_BR'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ["_plugins"]

# plugin author_images gera a imagem ou avatar pra cada autor.
PLUGINS = ['author_images', 'readtime', 'related_posts', 'share_post', 'thumbnailer',
           'autopages', 'better_figures_and_images', 'subcategory','sub_parts']

#author_images plugin
AUTHOR_AVATARS = 'images/author_avatars'
AUTHOR_IMAGES = 'images/author_images'

#related_posts plugin
RELATED_POSTS_MAX = 4
RELATED_POSTS_SKIP_SAME_CATEGORY = False

#thumbnailer plugin
IMAGE_PATH = 'images/thumbnails/'
THUMBNAIL_DIR = 'images/thumbnails/'
THUMBNAIL_KEEP_NAME = True
# wxh - will resize to exactly wxh
# wx? - will resize so that the width is the specified size, and the height will scale to retain aspect ratio
# ?xh - same as wx? but will height being a set size
# s is a shorthand for wxh where w=h
THUMBNAIL_SIZES = {
    'thumbnail_cover': '?x100',
    'thumbnail_post': '?x250'
}

#autopages plugin
AUTHOR_PAGE_PATH = 'pages/authors'
CATEGORY_PAGE_PATH = 'pages/categories'
TAG_PAGE_PATH = 'pages/tags'

#better_figures_and_images plugin
RESPONSIVE_IMAGES = True

#subcategories plugin
PATH_METADATA = 'posts/(?P<subcategory_path>.*)/.*'

#sub_parts plugin
FILENAME_METADATA = '(?P<slug>(?P<date>\d{4}-\d{2}-\d{2})-[^.]+)'

