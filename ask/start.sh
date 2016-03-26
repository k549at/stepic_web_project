sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql restart
sudo gunicorn -c /etc/gunicorn.d/test ask.wsgi
