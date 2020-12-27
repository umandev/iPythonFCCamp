Sample Module Repository
========================

project setup:
mysql setup via docker:
docker network create mysql-network
docker run --restart always --name mysqlserver --net mysql-network -v /Users/greenbook/mysql-data:/var/lib/mysql -p 3306:3306 -d -e MYSQL_ROOT_PASSWORD=xxx mysql:latest


This simple project is an example repo for Python projects.

`Learn more <http://www.kennethreitz.org/essays/repository-structure-and-python>`_.

---------------

If you want to learn more about ``setup.py`` files, check out `this repository <https://github.com/kennethreitz/setup.py>`_.
