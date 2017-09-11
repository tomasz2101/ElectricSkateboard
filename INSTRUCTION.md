# Backup
docker exec mysql /usr/bin/mysqldump -u root --password=root dbdatabase > backup.sql

# Restore
cat backup.sql | docker exec -i mysql /usr/bin/mysql -u root --password=root dbdatabase