from sqlalchemy import create_engine #create_engine is a function that creates a new SQLAlchemy engine instance, which is used to connect to the database.
from sqlalchemy.orm import sessionmaker, declarative_base #orm is a module that provides tools for working with databases in an object-oriented way. sessionmaker is a factory for creating new Session objects, which are used to interact with the database. declarative_base is a function that returns a new base class from which all mapped classes should inherit.

DATABASE_URL = "postgresql://localhost:5432/terrace"

engine = create_engine(DATABASE_URL) #here the engine will be used to connect to the PostgreSQL database specified by the DATABASE_URL. The engine is a central object that manages the connection pool and provides a source of database connections for the application.

SessionLocal = sessionmaker(bind=engine) #this is how we send queries, save data, fetch data, etc.

Base = declarative_base() #this is what all models will inherit from. It provides a base class for our database models, allowing us to define tables and their relationships in an object-oriented way.