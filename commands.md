pip install fastapi fastapi-sqlalchemy pydantic alembic psycopg2 uvicorn python-dotenv

alembic init alembic

docker-compose build -----(1)
docker-compose up -----(2)
**** run migration command in virtual env
docker-compose run app alembic revision --autogenerate -m "New Migration" -------(3)
docker-compose run app alembic upgrade head #commit migration to the database ------(4)