sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
suddo ln -s /home/box/web/etc/myguni.conf /etc/gunicorn.d/
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
