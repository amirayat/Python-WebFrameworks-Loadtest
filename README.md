# Python Web Application Framework Load Test

### Project Description

This project provides performance tests across some famous Python web application frameworks. The test criterion is receiving the list of records from the database(MongoDB and PostgreSQL) through REST API. You can find [data](https://github.com/dr5hn/countries-states-cities-database) in the directory ```/data``` and load them to the database. Here is the list of frameworks:

- Django
- FastAPI
- Flask
- Japronto
- Sanic

### Load Testing Tool

For each test, Apache Bench sends 5000 requests in batches of 100 concurrent by the following command.

```bash
ab -n 5000 -c 100 http://127.0.0.1:8000/countries/
```

### Result

The final document of each test is saved in the ```/result``` directory. The results may vary on different systems.

![](./assets/python-webframework-loadtest.png)


