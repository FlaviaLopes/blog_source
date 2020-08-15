#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Flávia Lopes'
SITENAME = 'Flávia Lopes .Dev'
SITEURL = 'https://flavialopes.dev'
CURRENTYEAR = date.today().year
RELATIVE_URLS = True
PATH = 'content'
DEPLOY_PATH = 'deploy'

### adicionado ###
SITETITLE = 'Flávia Lopes'
SITEDESCRIPTION = 'Site pessoal e divulgação de projetos.'
BLOGKEYWORDS = ['python', 'python developer', 'web', 'pelican', 'github pages' 'data science', 'github', 'portfolio']
GITHUB_URL = 'http://github.com/FlaviaLopes/'

# ----DATA---------------------------------------------------------------------------------------------------------#

OCCUPATION = 'Python Developer'
INTERESTS = 'Interessada em Ciência de Dados, Código limpo, Python, Cloud Computing'
SOCIAL = (('twitter', 'https://twitter.com/_flavialopes_'),
          ('linkedin', 'https://linkedin.com/in/lopesflavia'),
          ('github', 'https://github.com/FlaviaLopes'),
          ('instagram', 'https://instagram.com/_flavialopes_'),
          ('facebook', 'https://facebook.com/flavialopesads'),)

CURRICULUM = 'https://linkedin.com/in/lopesflavia'
TITLE = 'Bem-Vind@'
INTRODUCTION = '''
Olá, sou a Flávia. Desenvolvo soluções usando tecnologias. Uso Python como linguagem principal e atualmente estou me aperfeiçoando em Cloud Computing, Ciência de Dados.
Este site portfolio foi desenvolvido usando CSS, HTML e Python. Está hospedado no Github Pages. Exatamente, esta é uma página estática gerada utilizando o Pelican, um gerador de páginas estáticas escrito em Python. 
No card ao lado você pode ter acesso às minhas redes e currículo, abaixo você pode verificar alguns projetos meus publicados no GitHub.
'''
PROJECTS = [
    {
        'name': 'Genetic Algorithm with Python',
        'link': 'https://www.github.com/FlaviaLopes/Genetic-Algorithm-with-Python',
        'desc': '''Genetic Algorithm with Python'''
    },
    {
        'name': 'Acelera Dev Data Science',
        'link': 'https://www.github.com/FlaviaLopes/AceleraDev-Codenation-Data-Science',
        'desc': '''Descubra as melhores notas de matemática do ENEM 2016: Lógica, Análise de dados, Estatística e Regressão.'''
    },
    {
        'name': 'Elei&ccedil;&otilde;es 2018',
        'link': 'https://www.github.com/FlaviaLopes/Eleicoes-2018',
        'desc': '''Explorando dados das Eleições 2018. Dados oriundos do Repositório de Dados Eleitorais do TSE.'''
    },
    {
        'name': 'Student Performance Prediction MLR',
        'link': 'https://github.com/FlaviaLopes/Student-Performance-Prediction-MLR',
        'desc': '''Student Grade Prediction using MLR - Predicting the final score of portuguese discipline. Python, sklearn.'''
    }
]

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
### fim adicionado ###

### adicionado ###
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git']
THEME = 'theme/card1'

# global metadata to all the contents
DEFAULT_METADATA = {
    'favicon': 'images/favicon.ico',
    'avatarblog': 'images/avatar.png'
}

LOAD_CONTENT_CACHE = False
# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
### fim adicionado ###

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt_BR'
