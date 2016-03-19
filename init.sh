sudo ln -s ~/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s ~/web/etc/gunicorn.conf /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo gunicorn  -c /etc/gunicorn.d/test -D hello:app
#sudo gunicorn -b 0.0.0.0:8000 ask.wsgi
cd ~/web/ask/
sudo gunicorn -c /etc/gunicorn.d/test ask.wsgi

