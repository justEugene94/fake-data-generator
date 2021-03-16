# Installation

* #### Clone Project

```bash
cd /home/projects
sudo mkdir fake-data-generator
sudo chown {{YOUR_USER}}:{{YOUR_USER}} fake-data-generator

git clone git@github.com:justEugene94/fake-data-generator.git fake-data-generator/
```

* #### Add `init.sql` file

```bash
cp docker/mysql/docker-entrypoint-initdb.d/init.sql.example docker/mysql/docker-entrypoint-initdb.d/init.sql
```

* #### Build Docker

```bash
sudo service nginx stop
sudo service mysql stop

docker-compose up --build
```

* #### Enter in python container:
```bash
docker-compose exec python bash
```

* #### Migrations in python container:
```bash
python3 manage.py migrate
```

* #### Static in python container:
```bash
python3 manage.py collectstatic
```