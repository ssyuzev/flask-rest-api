# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}


## Requirements
- Docker & Docker-compose
- Python3, cookiecutter
- Fabric3 (optional)


## Run locally with docker

Use docker-compose
```
docker-compose build
docker-compose up
```


## Initialise environment variables. 

Save `.env.example`  as a `.env` file.


## Run migrations

```
fab init_db
```
OR
```
docker-compose exec app /bin/bash ./scripts/run_migrations.sh
```

## Add some demo data such as users
```
fab seed_db
```
OR
```
docker-compose exec app python3 src/manage.py seed_db
```


## Swagger & Redoc
```
- http://127.0.0.1:5000/api/v1/docs
- /api/v1/redoc
```


(c) {{ cookiecutter.year }} {{ cookiecutter.project_author }}
version: {{ cookiecutter.version }}