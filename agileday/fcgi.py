#!/usr/bin/python

from django.core.management import execute_from_command_line

execute_from_command_line(
    argv=[
        '(agileday.fcgi)',
        'runfcgi',
        '--settings=agileday.settings',
        ],
    )
