#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
from datetime import date

sys.path.append(os.curdir)
from data import *

AUTHOR = 'Flávia Lopes'
SITENAME = 'Flávia Lopes .Dev'
SITEURL = 'https://flavialopes.dev'
SITETITLE = 'Flávia Lopes'
SITEDESCRIPTION = 'Site pessoal e divulgação de projetos.'
BLOGKEYWORDS = ['python', 'python developer', 'web', 'pelican', 'github pages' 'data science', 'github', 'portfolio']
CURRENTYEAR = date.today().year
RELATIVE_URLS = True

PATH = 'content'
DEPLOY_PATH = 'deploy'
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git']
THEME = 'theme/card1'
LOAD_CONTENT_CACHE = False
# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt-br'

# global metadata to all the contents
DEFAULT_METADATA = {
    'favicon': 'images/ico.ico',
    'avatar': 'images/tea.jpg'
}
# Dados de redes sociais
GITHUB_URL = 'http://github.com/FlaviaLopes/'
SOCIALSHARE = (
    ('twitter',
     'https://twitter.com/share?text={}&url={}&hashtags={}'.format(
         INTRODUCTION[:170].strip(),
         SITEURL.strip(),
         ','.join([f'{"".join(it.split())}' for it in BLOGKEYWORDS])
     )
     ),
    ('facebook', 'https://www.facebook.com/sharer/sharer.php?u={}'.format(SITEURL)),
    ('linkedin', 'https://www.linkedin.com/sharing/share-offsite/?url={}'.format(SITEURL)),
    ('whatsapp', 'https://api.whatsapp.com/send?text={}'.format(SITEURL)),
)
