sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
suddo ln -s /home/box/web/etc/myguni.conf /etc/gunicorn.d/
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -c hello.py hello:app
