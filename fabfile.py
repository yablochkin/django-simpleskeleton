# -*- coding: utf-8 -*-
from __future__ import with_statement

from fabric.api import *

env.hosts = ['user@server']


def deploy():
    local('git push')

    code_dir = '/home/sites/coolsite'
    with cd(code_dir):
        run('git pull')

    # uwsgi touch graceful reload
    run('touch /tmp/coolsite.txt')


def status():
    run('supervisorctl status')


def uptime():
    run('uptime')
