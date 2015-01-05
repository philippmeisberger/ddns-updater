#!/usr/bin/env python3

from distutils.core import setup

setup(
    name            = 'ddns-updater',
    version         = '1.0',
    description     = 'DDNS client to register your dynamic IP address.',
    author          = 'Philipp Meisberger',
    author_email    = 'team@pm-codeworks.de',
    url             = 'http://www.pm-codeworks.de/ddns-updater.html',
    license         = 'BSD 3.0 License',
    package_dir     = {'': 'files'},
)
