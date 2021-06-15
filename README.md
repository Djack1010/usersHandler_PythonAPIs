# Python Flask APIs to handle a small DB

Implement the APIs (files `app/api/endpoints/v1/login.py` and eventually `app/api/serializers.py`) and connect them to the MySQL DB to complete the exercise.

The tool run with `docker-compose` and can be setup with:

`docker-compose up --build`

It consists of 2 containers, one for the APIs (/app) and the other (/db) for the MySQL DB (see `docker-compose.yml`). 

The API container provides a web interface to test the implementation, available at `http://localhost:5000/api/v1/`.

Do not forget to set a new DB password in the `docker-compose.yml` and `app/utils/settings.py` files.
