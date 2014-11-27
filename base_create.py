from sqlalchemy import create_engine

from thing import Base

def create():
    engine = create_engine('sqlite:///stuffbot.db')

    Base.metadata.create_all(engine)

create()
