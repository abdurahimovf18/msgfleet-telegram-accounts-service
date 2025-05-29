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
