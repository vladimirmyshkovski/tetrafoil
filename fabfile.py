# coding: utf-8
from fabric.api import run, env, cd, prefix, shell_env, local
from config import load_config

config = load_config()
host_string = config.HOST_STRING


def deploy():
    env.host_string = config.HOST_STRING
    run('sudo chmod -R 777 /var/www/tetrafoil/**/**/')
    print('!!! chmod in /var/www/tetrafoil/ changet to 777 !!!')
    with cd('/var/www/tetrafoil'):
        with shell_env(MODE='PRODUCTION'):
            #run('git reset --hard HEAD')
            #run('git pull')
            run('npm install')
            run('gulp')
            with prefix('source venv/bin/activate'):
                run('pip install -r requirements.txt')
                run('python manage.py db upgrade')
                run('python manage.py build')
            run('supervisorctl restart ttt')
            run('sudo chmod -R 654  /var/www/tetrafoil/**/**/')
            #run('sudo chmod 654 -R /var/www/tetrafoil')
            #print('!!! chmod in /var/www/tetrafoil changet to 654 !!!')


def create_db():
	env.host_string = config.HOST_STRING
	with cd('/var/www/tetrafoil'):
			with shell_env(MODE='PRODUCTION'):
				with prefix('source venv/bin/activate'):
					run('python manage.py db init')
					run('python manage.py db migrate')
					run('python manage.py db upgrade')


def restart():
    env.host_string = config.HOST_STRING
    run('supervisorctl restart ttt')
