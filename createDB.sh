sudo /etc/init.d/mysql restart
mysql -uroot -e "create database if not exists stepic_db default character set utf8 collate utf8_general_ci;"
#mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'password';"
#mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'box'@'localhost';"
#mysql -uroot -e "FLUSH PRIVILEGES;"
sudo ~/web/ask/manage.py syncdb
mysql -uroot -e "insery into auth_user(id,username) values('1','admin');"

