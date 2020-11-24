# {{cookiecutter.project_name}}
by {{cookiecutter.project_author}}

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

## Swagger & Redoc
```
- http://127.0.0.1:5000/api/v1/docs
- /api/v1/redoc
```
