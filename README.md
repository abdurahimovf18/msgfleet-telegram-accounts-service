This repository holds code of the part of the micro-service based application: "MsgFleet". 

## Responsibility
This Service is responsible for managing Telegram user account, via telegram client
respecting telegram limits and lows.


## Tech-Stacks

### FastAPI
An Instrument to get the API requests from abroad and handle them with low-latency and
Python friendly annotation via Pydantic.

### SqlAlchemy
A flexable ORM to integrate with internal database of the service (Used with Alembic)

### Alembic
Migration manager to keep tables up-to-date.

### Pydantic
An excellent type annotation and validation library. Pydantic is used to communicate
between functions and methods as this diogram shows: ```DTO -> Logic -> DTO```

### alembic-postgresql-enum
Normalizes alembic enums working with postgresql. Alembic does not support postgresql
enums natively well.

### RabbitMQ 
An message Broker which is actively used to communicate between micro-services and
Used as a Celery Broker.

### Redis
A low-latency NoSQL database which is used as a Cache and the Celery Backend

### Celery
An Asynchronous service which is used to concurently manage a long term tasks

Uses:
  - ```Redis``` - backend
  - ```RabbitMQ``` - Broker

### HTTPX
A library which is used to keep communication between services due to flexibility,
support of web-socket and http2 natively.

### Poetry
A version controller wildly used to execute developer runs and tests.

### Telethon
A Telegram-Client manager.

## How to run

### Development

#### Install Python
```bash
# Update apt
sudo apt update

# Install Python
sudo apt install python3 -y
```

#### Install Poetry

```bash

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Export paths
export PATH="$HOME/.local/bin:$PATH"

# Test It!
poetry --version
# You should see something like:
# Poetry (version 2.1.2)


```


#### Production



This service is a part of the application called msgfleet. This service responsible for handling logic of telegram-user related account handling and security concerns.


Tech-Stacks:
  - FastAPI (As a main API handler)
  - SqlAlchemy (Fully used as a ORM and core sql like syntax)
  - Alembic (Migrations)
  - Pydantic (Used to safely validate data between query, flow and endpoints and via FastAPI)
  - alembic-postgresql-enum (to solve errors of Alembic related to postgresql enums)
  - RabbitMQ (As a Message Broker and Celery broker)
  - Redis (will be used to cache and/or celery backend.)
  - Celery (To send messages)
  - Httpx (To send communicate between services)
  - Poetry (As a version controller)
  - Telethon (Telegram-Client)

Responsibility:
  - Handling Telegram User account.

How To Run:
  - Install Python and Poetry.
  - Configure all of the configurations in the secrets file.
  - Install Dependencies via: "poetry install"
  - run command: "poetry run dev"
  - If you are running the application in the production environment then use Gunicorn.
  - Set the nginx if using this micro-service stand-alone.
