#python manage.py runfcgi socket=/tmp/django/blog.sock method=prefork daemonize=true pidfile=/var/run/django/blog.pid
sudo python manage.py runfcgi socket=/tmp/django/blog.sock method=prefork pidfile=/var/run/django/blog.pid
