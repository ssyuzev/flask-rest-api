# Flask REST API Starter template with cookiecutter


## Requirements
- Docker & Docker-compose
- Python3, cookiecutter
- Fabric3 (optional)


## Use cookiecutter to make a new project from this template
[Cookiecutter docs](https://cookiecutter.readthedocs.io/en/latest/)
```
pip install --user cookiecutter
cookiecutter https://github.com/ssyuzev/flask-rest-api
```


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

## Add some demo data such as users
```
fab seed_db
```

## Swagger & Redoc (example routes)
```
- http://127.0.0.1:5000/api/v1/docs
- http://127.0.0.1:5000/api/v1/redoc
```
