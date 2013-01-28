from __future__ import with_statement
from fabric.api import local,settings, abort,run
from fabric.contrib.console import confirm


def prepare_deploy():
    local("python manage.py test webblog")
    # local("git add -A && git commit")
    local("echo `uname -a`")
    
def test():
    with settings(warn_only=True):
        result = local("python manage.py test webblog", capture=True)
    if result.failed and not confirm("Tests Faild. Continue anyway?"):
        abort("Aborting at user request.")
        

def uname():
    local("echo `uname -a`")

def deploy():
    pass


