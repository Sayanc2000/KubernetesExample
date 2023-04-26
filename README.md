# Kubernetes Example

## FastAPI Application

### Local Build
* Use [Dockerfile.local](Dockerfile.local) for local docker build and running
* Use [docker-compose.local](docker-compose.local.yaml) for local environment

#### Local Environment variables
* SQLALCHEMY_DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres

### Testing
* Tests are written under [tests](app/tests) folder
* Run tests with command `pytest`
* To run tests and get print output from it run `pytest -s`