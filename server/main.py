from fastapi import FastAPI
from config.database import db_config
from routes import users, movies

app = FastAPI()

db_config.Base.metadata.create_all(bind=db_config.engine)

app.include_router(users.router)
app.include_router(movies.router)




