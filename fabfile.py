# Fabric File for britdoc site deployment
# to install fabric on osx - easy_install fabric

# typical usage
# fab deploy_production

import requests

# from fabric.api import env
from fabric.api import cd
# from fabric.api import run
from fabric.api import hosts
from fabric.api import sudo
from fabric.operations import local


production_host = ('lin-www-01.numbereight.org')


@hosts(production_host)
def deploy_production():
    with cd('/var/www/britdoc-site-production/'):
        sudo('git pull', user='root')
        sudo('source /home/ops/.virtualenvs/britdoc-site-production/bin/activate && ./manage.py migrate', user='ops')
        # sudo('source /home/ops/.virtualenvs/britdoc-site-production/bin/activate && pip install --upgrade -r requrements.txt', user='ops')
        # sudo('source /home/ops/.virtualenvs/britdoc-site-production/bin/activate && ./manage.py bower install', user='ops')
        sudo('source /home/ops/.virtualenvs/britdoc-site-production/bin/activate && ./manage.py collectstatic --noinput', user='ops')
        sudo('/usr/bin/supervisorctl restart britdoc-site-production')

@hosts(production_host)
def pull_production():
    with cd('/var/www/britdoc-site-production/'):
        sudo('git pull', user='root')
        sudo('source /home/ops/.virtualenvs/britdoc-site-production/bin/activate && ./manage.py collectstatic --noinput', user='ops')

def rollbar_record_deploy():
    access_token = '5abebb4353714078aedb82f45d233592'
    environment = 'production'
    local_username = local('whoami', capture=True)
    # fetch last committed revision in the locally-checked out branch
    revision = local('git log -n 1 --pretty=format:"%H"', capture=True)

    resp = requests.post('https://api.rollbar.com/api/1/deploy/', {
        'access_token': access_token,
        'environment': environment,
        'local_username': local_username,
        'revision': revision
    }, timeout=3)

    if resp.status_code == 200:
        print "Deploy recorded successfully."
    else:
        print "Error recording deploy:", resp.text
