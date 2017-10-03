#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name     = 'FlibustaDailySync',
    version  = '0.1.0',
    packages = find_packages(),
    requires = ['python (>= 2.5)'],
    description  = 'A script to synchronize daily archives from website Flibusta',
    long_description = open('Readme.md').read(),
    author       = 'Alexandr Mikhailenko a.k.a Alex M.A.K.',
    author_email = 'alex-m.a.k@yandex.kz',
    url          = 'https://github.com/mak-alex/FlibustaDailySync',
    download_url = 'https://github.com/mak-alex/FlibustaDailySync/archive/master.zip',
    license      = 'GPL3 License',
    keywords     = [
        'Flibusta.is', 'flibusta', 'sync', 'daily', 'daily archive', 'sync daily archive', 'sync daily archive from flibusta'
    ],
    install_requires=[
        'lxml',
        'tqdm',
        'urllib',
        'argparse'
        'requests==2.17.1',
    ],
)

