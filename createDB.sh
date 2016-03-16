mysql -uroot -e "create database if not exists stepic_db"
mysql -uroot -e "CREATE USER if not exists 'box'@'localhost' IDENTIFIED BY 'password';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'box'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"

bash ~/web/createDB.sh

